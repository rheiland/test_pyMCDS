from pyMCDS_rwh import pyMCDS

mcds = pyMCDS('output00000001.xml','.')
#_read_xml: self.bbox_coords=  [-20. -20. -10.  20.  20.  10.]

x,y=-10,-10
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=10,-10
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=-10,10
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=10,10
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=15,15
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=0,0
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

x,y=19,19
conc = mcds.get_concentrations_at(x=x, y=y, z=0)
print("----- ",x,y," = ",conc)

try:
    x,y=-20,-20
    print("----- Doing an on-the-outer-domain-boundary cell position test ",x,y)
    conc = mcds.get_concentrations_at(x=x, y=y, z=0)
    print("----- ",x,y," = ",conc)
except Exception as e: 
    print(e)

try:
    x,y=20,20
    print("----- Doing an on-the-outer-domain-boundary cell position test ",x,y)
    conc = mcds.get_concentrations_at(x=x, y=y, z=0)
    print("----- ",x,y," = ",conc)
except Exception as e: 
    print(e)

try:
    x,y=21,21
    print("----- Doing an out-of-domain cell position test ",x,y)
    conc = mcds.get_concentrations_at(x=x, y=y, z=0)
    print("----- ",x,y," = ",conc)
except Exception as e: 
    print(e)
#/Users/heiland/git/test_pyMCDS/PhysiCell/out_2x2/pyMCDS_rwh.py:120: RuntimeWarning: invalid value encountered in double_scalars
#  dz = (Z.max() - Z.min()) / (Z.shape[0] - 1)
# print(conc)
