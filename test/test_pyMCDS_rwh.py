#####
# title: test_pyMCDS_rwh.py
#
# language: python3
# author: bue, rwh
# date: 2022-11-11
# license: BSD 3-Clause
#
# description:
#   pytest unit test library for pyMCDS.py
#   + https://docs.pytest.org/
#
#   note:
#   assert actual == expected, message
#   == value equality
#   is reference equality
#   pytest.approx for real values
#####

### load library part 1 ###
import os
import sys

### run PhysiCell ###
os.chdir('../PhysiCell')
os.system('make')
os.system('test_pymcds config/config_2x2voxels.xml')
os.chdir('../test')

### load library part 2 ###
os.chdir('..')
sys.path.insert(0, os.getcwd())
import pyMCDS_rwh as pc
os.chdir('test')

# const
s_path_2x2 = '../PhysiCell/out_2x2'
s_file_2x2 = 'output00000001.xml'
#s_pathfile_2x2 = f'{s_path_3d}/{s_file_3d}'


### run unit tests ###
class TestPyMcdsRwh(object):
    ''' test for pyMCDS class form pcDataLoader version 2 branch '''
    mcds = pc.pyMCDS(s_file_2x2, s_path_2x2)

    def test_pyMCDS(self, mcds=mcds):
        assert str(type(mcds)) == "<class 'pyMCDS_rwh.pyMCDS'>"

    def test_mcds_get_concentration_at(self, mcds=mcds):
        a_sw = mcds.get_concentrations_at(x=-10, y=-10, z=0)
        a_se = mcds.get_concentrations_at(x=10, y=-10, z=0)
        a_nw = mcds.get_concentrations_at(x=-10, y=10, z=0)
        a_ne = mcds.get_concentrations_at(x=10, y=10, z=0)
        assert (str(type(a_sw)) == "<class 'numpy.ndarray'>") and \
               (str(type(a_se)) == "<class 'numpy.ndarray'>") and \
               (str(type(a_nw)) == "<class 'numpy.ndarray'>") and \
               (str(type(a_ne)) == "<class 'numpy.ndarray'>") and \
               a_sw == [40] and \
               a_se == [41] and \
               a_nw == [42] and \
               a_ne == [43]

