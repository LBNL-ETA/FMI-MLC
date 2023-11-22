"""
Function to export exmaple FMUs.
"""

import os
import sys

pymodelica_path = os.path.join(os.environ.get('JMODELICA_HOME'), 'Python')
sys.path.append(pymodelica_path)
try:
    from pymodelica import compile_fmu
except:
    raise ImportError('Cannot find "pymodelica" in "{}"' \
        .format(pymodelica_path))

root = os.path.dirname(os.path.abspath(__file__))

PATH_SCOODER = '/home/Christoph/Documents/PublicRepos/SCooDER/SCooDER/package.mo'

# Export PVandBatt
def export_PVandBatt(log='error', target='cs'):
    """Export PV and Battery FMU form SCooDER."""
    mopath = [PATH_SCOODER]
    modelpath = 'SCooDER.Systems.Examples.PVandBatt'
    libraries = os.environ.get('MODELICAPATH')
    fmupath = compile_fmu(modelpath, mopath, compiler_log_level=log,
                          compiler_options={'extra_lib_dirs':libraries},
                          compile_to=os.path.join(root, 'PVandBatt.fmu'),
                          version='2.0', target=target)
    return fmupath

if __name__ == '__main__':
    print('Exporting FMUs...')
    export_PVandBatt()
    print('done.')
