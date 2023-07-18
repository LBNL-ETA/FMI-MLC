"""
FMI-MLC default configuration.
"""

def get_default_parameter():
    '''
    Returns the default parameters for fmi_gym. Description:

    fmi_gym parameter:
        precision (str): Precision of data exchange, default 'float32'.
        seed (int): Seed for np.random, default None.
        preprocessor (#classA): Custom Python function to pre-process data
                                before FMU, default None.
        postprocessor (#classA): Custom Python function to post-process data
                                 after FMU, default None.
        reset_on_init (bool): Reset environment when initializing, default False.
        store_data (bool): Store inputs, FMU outputs, and reward in self.data, default False.
        store_all_data (bool): Store all episode data in self.data_all.
                               The flag "store_data" must be set to True. Default False.
        init_fmu (bool): Initialize FMU when fmi_gym resets, default True.
        stateprocessor (#classA): Custom Python function to midify state object, default None.
        resetprocessor (#classB): Custom Python function executed on fmi_gym reset, default None.
        ignore_reset (bool): Ignore the reset command (keep fmu/states), default False.
        store_warmup (bool): Store the data collected during warmup, default False.
    fmu parameter:
        fmu_step_size (int): Step size of the FMU in seconds, default 60*60.
        fmu_path (str): Path to the .fmu file, default ''.
        fmu_start_time (float): Start time of the FMU in seconds, default 0.
        fmu_warmup_time (float): The warmup time of the FMU in seconds, default None.
        fmu_final_time (float): Final time of the FMU in seconds, default 24*60*60.
        fmu_episode_duration (float): Define episode duration. The default (None)
                                      automatrically uses the "fmu_final_time" to determine the
                                      end of an episode. This parameter is mainly used when
                                      multiple episodes are performed sequentially, in
                                      conjunction with the "ignore_reset" flag.
        fmu_loglevel (int): Log level of the fmu with 0: none and 5: debug, default 4.
        fmu_kind (str): Type of FMU where currently only co-simulation is supported, default 'cs'.
        fmu_tolerance (float): Internal tolerance of the FMU solver, default 1e-6.
        fmu_param (dict): Parameters of the FMU to be set on initialize, default {}.
    data exchange parameter:
        inputs (dict): Static inputs of the FMU to be set on do_step, default {}.
        inputs_map (dict): Renaming of fmi_gym inputs to FMU inputs, default {}.
        hidden_input_names (list): Labes of inputs not passed to the FMU, default [].
        action_names (list): Lables of fmi_gym actions, default [].
        action_min (np.array): Lower action limit, default -1e6.
        action_max (np.array): Upper action limit, default 1e6.
        observation_names (list): Lables of fmi_gym observations, default [].
        observation_min (np.array): Lower observation limit, default -1e6.
        observation_max (np.array): Upper observation limit, default -1e6.
        hidden_observation_names (list): List of hidden observations acquired but
                                         not returned as state, default [].
        external_observations (dict): Observations which are calculated outside of FMU
                                      and default values, default {}.
        reward_names (list): Lables of fmi_gym rewards, default [].

    The #classA must be defined as:

    # Initialize (fmi_gym_parameter: dict)
    x = yourclass(fmi_gym_parameter)
    # Evaluate (data: pd.DataFrame, init: bool)
    data = x.do_calc(data, init)

    The #classB must be defined as:

    # Initialize (fmi_gym_parameter: dict)
    x = yourclass(fmi_gym_parameter)
    # Evaluate (data: pd.DataFrame, init: bool)
    data, fmi_gym_parameter = x.do_calc(data, fmi_gym_parameter, init)

    Returns
    -------
    parameter (dict): Dictionary of parameters.
    '''
    parameter = {}

    # fmi_gym parameter
    parameter['precision'] = 'float64'
    parameter['seed'] = None
    parameter['preprocessor'] = None
    parameter['postprocessor'] = None
    parameter['reset_on_init'] = False
    parameter['store_data'] = False
    parameter['store_all_data'] = False
    parameter['init_fmu'] = True
    parameter['stateprocessor'] = None
    parameter['resetprocessor'] = None
    parameter['ignore_reset'] = False
    parameter['store_warmup'] = False

    # fmu parameter
    parameter['fmu_step_size'] = 60*60
    parameter['fmu_path'] = ''
    parameter['fmu_start_time'] = 0
    parameter['fmu_warmup_time'] = None
    parameter['fmu_final_time'] = 24*60*60
    parameter['fmu_episode_duration'] = None
    parameter['fmu_loglevel'] = 4
    parameter['fmu_kind'] = 'cs'
    parameter['fmu_tolerance'] = 1e-6
    parameter['fmu_param'] = {}

    # data exchange parameter
    parameter['inputs'] = {}
    parameter['inputs_map'] = {}
    parameter['hidden_input_names'] = []
    parameter['action_names'] = []
    parameter['action_min'] = -1e6
    parameter['action_max'] = 1e6
    parameter['observation_names'] = []
    parameter['observation_min'] = -1e6
    parameter['observation_max'] = 1e6
    parameter['hidden_observation_names'] = []
    parameter['external_observations'] = {}
    parameter['reward_names'] = []
    return parameter
