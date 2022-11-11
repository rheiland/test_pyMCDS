from pyMCDS_rwh import pyMCDS

mcds = pyMCDS('output00000001.xml','.')
#_read_xml: self.bbox_coords=  [-20. -20. -10.  20.  20.  10.]

conc = mcds.get_concentrations_at(x=-10, y=-10, z=0)
#/Users/heiland/git/test_pyMCDS/PhysiCell/out_2x2/pyMCDS_rwh.py:120: RuntimeWarning: invalid value encountered in double_scalars
#  dz = (Z.max() - Z.min()) / (Z.shape[0] - 1)
print(conc)
