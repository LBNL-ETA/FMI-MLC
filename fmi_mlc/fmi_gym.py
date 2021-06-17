import os
import sys
import gym
from gym import spaces
import numpy as np
import pandas as pd

root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root)
from fmi_gym_parameter import get_default_parameter

class fmi_gym(gym.Env):

    def __init__(self, parameter={}, pyfmi=None):
        '''
        Setup the FMI-MLC gym environment.
        
        Inputs
        ------
        parameter (dict): Configuration dictionary, default see help(get_default_parameter).
        pyfmi (class): Specifies FMU handler, default None. None defaults to PyFMI package.       
        '''
        super(fmi_gym, self).__init__()
        
        # Setup
        self.parameter = get_default_parameter()
        self.parameter.update(parameter)
        self.init = True
        
        # Parse Configuration
        self.seed = self.parameter['seed']
        self.precision = eval('np.{}'.format(self.parameter['precision']))
        
        self.fmu_time = 0
        self.data = pd.DataFrame()
        self.fmu_loaded = False

        # FMI interface (load FMU)
        self.setup_pyfmi(pyfmi)
            
        # Use Python preprocessing before calling FMU
        if self.parameter['preprocessor']:
            self.preprocessor = self.parameter['preprocessor'](self.parameter)
        else:
            self.preprocessor = None
            
        # Use Python postprocessing after calling FMU
        if self.parameter['postprocessor']:
            self.postprocessor = self.parameter['postprocessor'](self.parameter)
        else:
            self.postprocessor = None
            
        # Function to process on reset
        if self.parameter['resetprocessor']:
            self.resetprocessor = self.parameter['resetprocessor'](self.parameter)
        else:
            self.resetprocessor = None
            
        self.action_space = spaces.Box(low=self.parameter['action_min'],
                                       high=self.parameter['action_max'],
                                       shape=(1, len(self.parameter['action_names'])),
                                       dtype=self.precision)
        self.action_space.np_random.seed(self.seed)

        self.observation_space = spaces.Box(low=self.parameter['observation_min'],
                                            high=self.parameter['observation_max'],
                                            shape=(1, len(self.parameter['observation_names'])),
                                            dtype=self.precision)
        self.observation_space.np_random.seed(self.seed)
        
        if self.parameter['reset_on_init']:
            self.state = self.reset()
        else:
            self.state = np.array([[np.nan]*len(self.parameter['observation_names'])])        
        
    def setup_pyfmi(self, pyfmi):
        '''
        Setup PyFMI or custom handler.
        
        Inputs
        ------
        pyfmi (fun): Hander for fmu evaluation.
        '''
        if pyfmi != None:
            self.load_fmu = pyfmi            
        else:
            from pyfmi import load_fmu
            self.load_fmu = load_fmu
            
    def configure_fmu(self):
        '''
        Load and setup the FMU.
        
        Inputs
        ------
        ext_param (dict): External parameter outside of this class.
        start_time (float): Start time of the model, in sceonds.
        '''
        # Load FMU
        self.fmu = self.load_fmu(self.parameter['fmu_path'],
                                 log_level=self.parameter['fmu_loglevel'],
                                 kind=self.parameter['fmu_kind'])
        
        # Parameterize FMU
        param = self.parameter['fmu_param']
        param.update(self.parameter['inputs'])
        if param != {}:
            self.fmu.set(list(param.keys()), list(param.values()))
            
        # Initizlaize FMU
        self.fmu.setup_experiment(start_time=self.parameter['fmu_start_time'],
                                  stop_time=self.parameter['fmu_final_time'],
                                  stop_time_defined=False,
                                  tolerance=self.parameter['fmu_tolerance'])
        self.fmu.initialize()
        self.fmu_loaded = True
        
        # Warmup
        self.fmu_time = self.fmu.time
        step_size = self.parameter['fmu_warmup_time'] - self.fmu_time
        self.fmu.do_step(current_t=self.fmu_time, step_size=step_size)
        self.fmu_time = self.fmu.time
        
    def evaluate_fmu(self, inputs):
        ''' evaluate the fmu '''
        inputs = inputs.copy()
        if self.parameter['inputs_map']:
            inputs = inputs.rename(columns={v:k for k,v in self.parameter['inputs_map'].items()})
        del inputs['time']
        
        # Set inputs
        self.fmu.set(inputs.columns.values, inputs.values[0])

        # Compute FMU
        step_size = inputs.index[0] - self.fmu_time
        self.fmu.do_step(current_t=self.fmu_time, step_size=step_size)
        
        # Results
        self.fmu_time = self.fmu.time
        names = self.parameter['observation_names'] + self.parameter['internal_observation_names'] + \
            self.parameter['reward_names']
        res = self.fmu.get(names)
        res = pd.Series(res, index=names)

        return res

    def step(self, action):
        ''' do step '''
        
        # Get internal FMU inputs
        data = pd.DataFrame({'time': [self.fmu_time+self.parameter['fmu_step_size']]})
        
        # Parse inputs
        action = pd.DataFrame(action, columns=self.parameter['input_labels'])
        data = pd.concat([data, action], axis=1)
        data.index = data['time'].values
        
        # Compute preprocessing (if specified)
        if self.preprocessor:
            data = self.preprocessor.do_calc(data, self.init)
        
        # Evaluate FMU 
        res = self.evaluate_fmu(data)
        for k,v in res.items():
            data[k] = v
            
        # Compute postprocessing (if specified)
        if self.postprocessor:
            data = self.postprocessor.do_calc(data, self.init)
            
        # Compute reward
        if self.parameter['reward_names']:
            data['reward'] = data[self.parameter['reward_names']].sum(axis=1)
        
        # Outputs
        reward = data['reward'].values[0]
        info = {'data': data}
        self.state = data[self.parameter['observation_names']].values
        if self.fmu_time >= self.parameter['fmu_final_time']:
            done = True
        else:
            done = False
        self.init = False
        if self.parameter['store_data']:
            if self.data.empty:
                self.data = data
            else:
                self.data = pd.concat([self.data, data])
        
        return self.state, reward, done, info
    
    def reset(self):
        ''' reset environment '''
        self.fmu_loaded = False
        self.init = True
        self.data = pd.DataFrame()
        # Load FMU
        if not self.fmu_loaded and self.parameter['init_fmu']:
            self.configure_fmu()
        self.state = self.fmu.get(self.parameter['observation_names'])
        if self.resetprocessor:
            self.data = self.resetprocessor.do_calc(self.data, self.init)
        return self.state
        
    def render(self):
        ''' render environment '''
        return False
        
    def close(self):
        ''' unload fmu here '''
        try:
            self.fmu.terminate()
        except Exception as e:
            print(e)
        self.fmu=None