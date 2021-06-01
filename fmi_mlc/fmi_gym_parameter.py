def get_default_parameter():
    '''
    Returns the default parameters for fmi_gym. Description:
    
    fmi_gym parameter:
        precision (str): Precision of data exchange, default 'float32'.
        seed (int): Seed for np.random, default None.
        preprocessor (#class): Custom Python function to pre-process data before FMU, default None.
        postprocessor (#class): Custom Python function to post-process data after FMU, default None.
        reset_on_init (bool): Reset environment when initializing, default False. 
        store_data (bool): Store inputs, FMU outputs, and reward in self.data, default False.
        init_fmu (bool): Initialize FMU when fmi_gym resets, default True.
        resetprocessor (#class): Custom Python function executed on fmi_gym reset, default None.
    fmu parameter:
        fmu_step_size (int): Step size of the FMU in seconds, default 60*60.
        fmu_path (str): Path to the .fmu file, default ''.
        fmu_start_time (float): Start time of the FMU in seconds, default 0.
        fmu_final_time (float): Final time of the FMU in seconds, default 24*60*60.
        fmu_loglevel (int): Log level of the fmu with 0: none and 5: debug, default 4.
        fmu_kind (str): Type of FMU where currently only co-simulation is supported, default 'cs'.
        fmu_tolerance (float): Internal tolerance of the FMU solver, default 1e-6.
        fmu_param (dict): Parameters of the FMU to be set on initialize, default {}.
    data exchange parameter:
        inputs (dict): Static inputs of the FMU to be set on do_step, default {}.
        inputs_map (dict): Renaming of fmi_gym inputs to FMU inputs, default {}.
        input_labels (list): Lables of fmi_gym inputs, default [].
        action_names (list): Lables of fmi_gym actions, default [].
        action_min (np.array): Lower action limit, default -1e6.
        action_max (np.array): Upper action limit, default 1e6.
        observation_names (list): Lables of fmi_gym observations, default [].
        observation_min (np.array): Lower observation limit, default -1e6.
        observation_max (np.array): Upper observation limit, default -1e6.
        internal_observation_names (list): List of additional observations not returned through fmi_mlc, default [].
        reward_names (list): Lables of fmi_gym rewards, default [].
        
    The #class must be defined as:
    
    # Initialize (fmi_gym_parameter: dict)
    x = yourclass(fmi_gym_parameter)
    # Evaluate (data: pd.DataFrame, init: bool)
    data = x.do_calc(data, init)
        
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
    parameter['init_fmu'] = True
    parameter['resetprocessor'] = None
    
    # fmu parameter
    parameter['fmu_step_size'] = 60*60
    parameter['fmu_path'] = ''
    parameter['fmu_start_time'] = 0
    parameter['fmu_final_time'] = 24*60*60
    parameter['fmu_loglevel'] = 4
    parameter['fmu_kind'] = 'cs'
    parameter['fmu_tolerance'] = 1e-6
    parameter['fmu_param'] = {}
    
    # data exchange parameter
    parameter['inputs'] = {}
    parameter['inputs_map'] = {}
    parameter['input_labels'] = []
    parameter['action_names'] = []
    parameter['action_min'] = -1e6
    parameter['action_max'] = 1e6
    parameter['observation_names'] = []
    parameter['observation_min'] = -1e6
    parameter['observation_max'] = 1e6
    parameter['internal_observation_names'] = []
    parameter['reward_names'] = []
    return parameter