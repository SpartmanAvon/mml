

from collections import namedtuple

import numpy as np

Atom = namedtuple('Atom','index type x y z vec fnn snn tnn charge')
Bond = namedtuple('Bond','index label i j length')
Angle = namedtuple('Angle','index label i j k angle')
Torsion = namedtuple('Torsion','index label i j k l angle')

Sysdata = namedtuple('Sysdata','Atoms,Bonds,Angles,Torsions')


Atoms = []
Bonds = []
Angles = []
Torsions = []


Atoms.append(Atom(0,'ca',-0.748000,1.170000,-0.056000,np.array([-0.748000,1.170000,-0.056000]),[5,1,7],[0,8,2,4,6],[1,3,5,7,9,11,12,13,14],-0.131000))
Atoms.append(Atom(1,'ca',0.645000,1.243000,0.004000,np.array([0.645000,1.243000,0.004000]),[0,2,8],[1,3,9,5,7],[0,2,4,6,8,10],-0.127000))
Atoms.append(Atom(2,'ca',1.405000,0.076000,0.038000,np.array([1.405000,0.076000,0.038000]),[1,3,9],[0,8,2,4,10],[1,3,5,7,9,11],-0.135000))
Atoms.append(Atom(3,'ca',0.773000,-1.166000,0.011000,np.array([0.773000,-1.166000,0.011000]),[2,4,10],[11,1,3,5,9],[0,2,4,6,8,10],-0.127000))
Atoms.append(Atom(4,'ca',-0.619000,-1.240000,-0.049000,np.array([-0.619000,-1.240000,-0.049000]),[3,5,11],[0,2,4,10,6],[1,3,5,7,9,11,12,13,14],-0.131000))
Atoms.append(Atom(5,'ca',-1.392000,-0.072000,-0.080000,np.array([-1.392000,-0.072000,-0.080000]),[0,4,6],[1,3,5,7,11,12,13,14],[0,2,4,6,8,10],-0.077300))
Atoms.append(Atom(6,'c3',-2.887000,-0.166000,-0.153000,np.array([-2.887000,-0.166000,-0.153000]),[5,12,13,14],[0,4,6],[1,3,5,7,11,12,13,14],-0.053800))
Atoms.append(Atom(7,'ha',-1.326000,2.091000,-0.084000,np.array([-1.326000,2.091000,-0.084000]),[0],[1,5,7],[0,8,2,4,6],0.130000))
Atoms.append(Atom(8,'ha',1.137000,2.212000,0.024000,np.array([1.137000,2.212000,0.024000]),[1],[0,8,2],[1,3,9,5,7],0.130000))
Atoms.append(Atom(9,'ha',2.489000,0.134000,0.085000,np.array([2.489000,0.134000,0.085000]),[2],[1,3,9],[0,8,2,4,10],0.130000))
Atoms.append(Atom(10,'ha',1.365000,-2.077000,0.036000,np.array([1.365000,-2.077000,0.036000]),[3],[2,4,10],[11,1,3,5,9],0.130000))
Atoms.append(Atom(11,'ha',-1.100000,-2.216000,-0.072000,np.array([-1.100000,-2.216000,-0.072000]),[4],[11,3,5],[0,2,4,10,6],0.130000))
Atoms.append(Atom(12,'hc',-3.355000,0.822000,-0.091000,np.array([-3.355000,0.822000,-0.091000]),[6],[12,5,14,13],[0,4,6],0.044033))
Atoms.append(Atom(13,'hc',-3.270000,-0.768000,0.677000,np.array([-3.270000,-0.768000,0.677000]),[6],[12,5,14,13],[0,4,6],0.044033))
Atoms.append(Atom(14,'hc',-3.189000,-0.625000,-1.100000,np.array([-3.189000,-0.625000,-1.100000]),[6],[12,5,14,13],[0,4,6],0.044033))
Bonds.append(Bond(0,'ca-ca',0,5,111))
Bonds.append(Bond(1,'ca-ca',0,1,111))
Bonds.append(Bond(2,'ca-ha',0,7,111))
Bonds.append(Bond(3,'ca-ca',1,2,111))
Bonds.append(Bond(4,'ca-ha',1,8,111))
Bonds.append(Bond(5,'ca-ca',2,3,111))
Bonds.append(Bond(6,'ca-ha',2,9,111))
Bonds.append(Bond(7,'ca-ca',3,4,111))
Bonds.append(Bond(8,'ca-ha',3,10,111))
Bonds.append(Bond(9,'ca-ca',4,5,111))
Bonds.append(Bond(10,'ca-ha',4,11,111))
Bonds.append(Bond(11,'ca-c3',5,6,111))
Bonds.append(Bond(12,'c3-hc',6,12,111))
Bonds.append(Bond(13,'c3-hc',6,13,111))
Bonds.append(Bond(14,'c3-hc',6,14,111))
Angles.append(Angle(0,'ca-ca-ca',5,0,1,222))
Angles.append(Angle(1,'ca-ca-ha',5,0,7,222))
Angles.append(Angle(2,'ca-ca-ca',0,5,4,222))
Angles.append(Angle(3,'ca-ca-c3',0,5,6,222))
Angles.append(Angle(4,'ca-ca-ha',1,0,7,222))
Angles.append(Angle(5,'ca-ca-ca',0,1,2,222))
Angles.append(Angle(6,'ca-ca-ha',0,1,8,222))
Angles.append(Angle(7,'ca-ca-ha',2,1,8,222))
Angles.append(Angle(8,'ca-ca-ca',1,2,3,222))
Angles.append(Angle(9,'ca-ca-ha',1,2,9,222))
Angles.append(Angle(10,'ca-ca-ha',3,2,9,222))
Angles.append(Angle(11,'ca-ca-ca',2,3,4,222))
Angles.append(Angle(12,'ca-ca-ha',2,3,10,222))
Angles.append(Angle(13,'ca-ca-ha',4,3,10,222))
Angles.append(Angle(14,'ca-ca-ca',3,4,5,222))
Angles.append(Angle(15,'ca-ca-ha',3,4,11,222))
Angles.append(Angle(16,'ca-ca-ha',5,4,11,222))
Angles.append(Angle(17,'ca-ca-c3',4,5,6,222))
Angles.append(Angle(18,'ca-c3-hc',5,6,12,222))
Angles.append(Angle(19,'ca-c3-hc',5,6,13,222))
Angles.append(Angle(20,'ca-c3-hc',5,6,14,222))
Angles.append(Angle(21,'hc-c3-hc',12,6,13,222))
Angles.append(Angle(22,'hc-c3-hc',12,6,14,222))
Angles.append(Angle(23,'hc-c3-hc',13,6,14,222))
Torsions.append(Torsion(0,'ca-ca-ca-ca',4,5,0,1,333))
Torsions.append(Torsion(1,'c3-ca-ca-ca',6,5,0,1,333))
Torsions.append(Torsion(2,'ca-ca-ca-ca',5,0,1,2,333))
Torsions.append(Torsion(3,'ca-ca-ca-ha',5,0,1,8,333))
Torsions.append(Torsion(4,'ca-ca-ca-ha',4,5,0,7,333))
Torsions.append(Torsion(5,'c3-ca-ca-ha',6,5,0,7,333))
Torsions.append(Torsion(6,'ca-ca-ca-ca',0,5,4,3,333))
Torsions.append(Torsion(7,'ca-ca-ca-ha',0,5,4,11,333))
Torsions.append(Torsion(8,'ca-ca-c3-hc',0,5,6,12,333))
Torsions.append(Torsion(9,'ca-ca-c3-hc',0,5,6,13,333))
Torsions.append(Torsion(10,'ca-ca-c3-hc',0,5,6,14,333))
Torsions.append(Torsion(11,'ca-ca-ca-ha',2,1,0,7,333))
Torsions.append(Torsion(12,'ha-ca-ca-ha',8,1,0,7,333))
Torsions.append(Torsion(13,'ca-ca-ca-ca',5,0,1,2,333))
Torsions.append(Torsion(14,'ca-ca-ca-ca',0,1,2,3,333))
Torsions.append(Torsion(15,'ca-ca-ca-ha',0,1,2,9,333))
Torsions.append(Torsion(16,'ca-ca-ca-ha',5,0,1,8,333))
Torsions.append(Torsion(17,'ca-ca-ca-ha',3,2,1,8,333))
Torsions.append(Torsion(18,'ha-ca-ca-ha',9,2,1,8,333))
Torsions.append(Torsion(19,'ca-ca-ca-ca',0,1,2,3,333))
Torsions.append(Torsion(20,'ca-ca-ca-ca',1,2,3,4,333))
Torsions.append(Torsion(21,'ca-ca-ca-ha',1,2,3,10,333))
Torsions.append(Torsion(22,'ca-ca-ca-ha',0,1,2,9,333))
Torsions.append(Torsion(23,'ca-ca-ca-ha',4,3,2,9,333))
Torsions.append(Torsion(24,'ha-ca-ca-ha',10,3,2,9,333))
Torsions.append(Torsion(25,'ca-ca-ca-ca',1,2,3,4,333))
Torsions.append(Torsion(26,'ca-ca-ca-ca',2,3,4,5,333))
Torsions.append(Torsion(27,'ca-ca-ca-ha',2,3,4,11,333))
Torsions.append(Torsion(28,'ca-ca-ca-ha',1,2,3,10,333))
Torsions.append(Torsion(29,'ca-ca-ca-ha',5,4,3,10,333))
Torsions.append(Torsion(30,'ha-ca-ca-ha',11,4,3,10,333))
Torsions.append(Torsion(31,'ca-ca-ca-ca',2,3,4,5,333))
Torsions.append(Torsion(32,'ca-ca-ca-c3',3,4,5,6,333))
Torsions.append(Torsion(33,'ca-ca-ca-ha',2,3,4,11,333))
Torsions.append(Torsion(34,'ca-ca-ca-ha',0,5,4,11,333))
Torsions.append(Torsion(35,'c3-ca-ca-ha',6,5,4,11,333))
Torsions.append(Torsion(36,'ca-ca-ca-c3',3,4,5,6,333))
Torsions.append(Torsion(37,'ca-ca-c3-hc',4,5,6,12,333))
Torsions.append(Torsion(38,'ca-ca-c3-hc',4,5,6,13,333))
Torsions.append(Torsion(39,'ca-ca-c3-hc',4,5,6,14,333))
Torsions.append(Torsion(40,'ca-ca-c3-hc',0,5,6,12,333))
Torsions.append(Torsion(41,'ca-ca-c3-hc',4,5,6,12,333))
Torsions.append(Torsion(42,'ca-ca-c3-hc',0,5,6,13,333))
Torsions.append(Torsion(43,'ca-ca-c3-hc',4,5,6,13,333))
Torsions.append(Torsion(44,'ca-ca-c3-hc',0,5,6,14,333))
Torsions.append(Torsion(45,'ca-ca-c3-hc',4,5,6,14,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)