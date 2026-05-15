

def datasets_path(dataset_name='', task_name='', speeds='4000r', ele_frequency='1600Hz', vib_frequency='1600Hz'):
    if dataset_name == 'PU_datasets_4classes_4096_1samples':
        class_numbers = 4
        data_root = r'./dataset/PU_datasets_4classes_4096_1samples/'  # PU_datasets_4classes_4096_1samples
        if task_name == 'T1':
            source_dataset_path_list = ['PU_N15_M01_F10', 'PU_N15_M07_F04', 'PU_N15_M07_F10']
            target_dataset_path = 'PU_N09_M07_F10'
        elif task_name == 'T2':
            source_dataset_path_list = ['PU_N09_M07_F10', 'PU_N15_M07_F04', 'PU_N15_M07_F10']
            target_dataset_path = 'PU_N15_M01_F10'
        elif task_name == 'T3':
            source_dataset_path_list = ['PU_N09_M07_F10', 'PU_N15_M01_F10', 'PU_N15_M07_F10']
            target_dataset_path = 'PU_N15_M07_F04'
        elif task_name == 'T0':
            source_dataset_path_list = ['PU_N09_M07_F10', 'PU_N15_M01_F10', 'PU_N15_M07_F04']
            target_dataset_path = 'PU_N15_M07_F10'
    elif dataset_name == 'BJUT_WT_datasets_IFAC':
        class_numbers = 5
        data_root = r'./dataset/BJUT_WT_64_samples_all_speed/'  # BJUT_WT_4096_64samples_norm
        if task_name == 'T20':
            source_dataset_path_list = ['BJUT_25Hz_5', 'BJUT_30Hz_5', 'BJUT_35Hz_5']
            target_dataset_path = 'BJUT_20Hz_5'
        elif task_name == 'T25':
            source_dataset_path_list = ['BJUT_20Hz_5', 'BJUT_30Hz_5', 'BJUT_35Hz_5']
            target_dataset_path = 'BJUT_25Hz_5'
        elif task_name == 'T30':
            source_dataset_path_list = ['BJUT_20Hz_5', 'BJUT_25Hz_5', 'BJUT_35Hz_5']
            target_dataset_path = 'BJUT_30Hz_5'
        elif task_name == 'T35':
            source_dataset_path_list = ['BJUT_20Hz_5', 'BJUT_25Hz_5', 'BJUT_30Hz_5']
            target_dataset_path = 'BJUT_35Hz_5'

    return data_root, source_dataset_path_list[0], source_dataset_path_list[1], source_dataset_path_list[2], \
        target_dataset_path, class_numbers

