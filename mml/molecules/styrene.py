

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


Atoms.append(Atom(0,'ca',-0.667000,1.205000,-0.043000,np.array([-0.667000,1.205000,-0.043000]),[5,1,8],[0,9,2,4,6],[1,3,5,7,8,10,12,13],-0.118500))
Atoms.append(Atom(1,'ca',0.731000,1.229000,0.021000,np.array([0.731000,1.229000,0.021000]),[0,2,9],[8,1,10,3,5],[0,2,4,6,9,11],-0.131000))
Atoms.append(Atom(2,'ca',1.451000,0.038000,0.045000,np.array([1.451000,0.038000,0.045000]),[1,3,10],[0,9,2,11,4],[1,3,5,8,10,12],-0.127000))
Atoms.append(Atom(3,'ca',0.775000,-1.178000,0.005000,np.array([0.775000,-1.178000,0.005000]),[2,4,11],[1,10,3,12,5],[0,2,4,6,9,11],-0.131000))
Atoms.append(Atom(4,'ca',-0.621000,-1.200000,-0.060000,np.array([-0.621000,-1.200000,-0.060000]),[3,5,12],[0,2,11,4,6],[1,3,5,7,8,10,12,13],-0.118500))
Atoms.append(Atom(5,'ca',-1.364000,-0.010000,-0.085000,np.array([-1.364000,-0.010000,-0.085000]),[0,4,6],[1,3,5,7,8,12,13],[0,2,4,6,9,11,14,15],-0.057800))
Atoms.append(Atom(6,'ce',-2.833000,-0.105000,-0.154000,np.array([-2.833000,-0.105000,-0.154000]),[5,7,13],[0,4,14,6,15],[1,3,5,7,8,12,13],-0.113200))
Atoms.append(Atom(7,'c2',-3.702000,0.915000,-0.180000,np.array([-3.702000,0.915000,-0.180000]),[6,14,15],[13,5,7],[0,4,14,6,15],-0.209000))
Atoms.append(Atom(8,'ha',-1.193000,2.155000,-0.061000,np.array([-1.193000,2.155000,-0.061000]),[0],[8,1,5],[0,9,2,4,6],0.131500))
Atoms.append(Atom(9,'ha',1.254000,2.181000,0.052000,np.array([1.254000,2.181000,0.052000]),[1],[0,9,2],[8,1,10,3,5],0.131000))
Atoms.append(Atom(10,'ha',2.536000,0.058000,0.095000,np.array([2.536000,0.058000,0.095000]),[2],[1,10,3],[0,9,2,11,4],0.131000))
Atoms.append(Atom(11,'ha',1.332000,-2.111000,0.023000,np.array([1.332000,-2.111000,0.023000]),[3],[2,11,4],[1,10,3,12,5],0.131000))
Atoms.append(Atom(12,'ha',-1.123000,-2.166000,-0.090000,np.array([-1.123000,-2.166000,-0.090000]),[4],[3,12,5],[0,2,11,4,6],0.131500))
Atoms.append(Atom(13,'ha',-3.240000,-1.114000,-0.189000,np.array([-3.240000,-1.114000,-0.189000]),[6],[13,5,7],[0,4,14,6,15],0.123000))
Atoms.append(Atom(14,'ha',-3.401000,1.956000,-0.150000,np.array([-3.401000,1.956000,-0.150000]),[7],[14,6,15],[13,5,7],0.113500))
Atoms.append(Atom(15,'ha',-4.768000,0.719000,-0.233000,np.array([-4.768000,0.719000,-0.233000]),[7],[14,6,15],[13,5,7],0.113500))
Bonds.append(Bond(0,'ca-ca',0,5,111))
Bonds.append(Bond(1,'ca-ca',0,1,111))
Bonds.append(Bond(2,'ca-ha',0,8,111))
Bonds.append(Bond(3,'ca-ca',1,2,111))
Bonds.append(Bond(4,'ca-ha',1,9,111))
Bonds.append(Bond(5,'ca-ca',2,3,111))
Bonds.append(Bond(6,'ca-ha',2,10,111))
Bonds.append(Bond(7,'ca-ca',3,4,111))
Bonds.append(Bond(8,'ca-ha',3,11,111))
Bonds.append(Bond(9,'ca-ca',4,5,111))
Bonds.append(Bond(10,'ca-ha',4,12,111))
Bonds.append(Bond(11,'ca-ce',5,6,111))
Bonds.append(Bond(12,'ce-c2',6,7,111))
Bonds.append(Bond(13,'ce-ha',6,13,111))
Bonds.append(Bond(14,'c2-ha',7,14,111))
Bonds.append(Bond(15,'c2-ha',7,15,111))
Angles.append(Angle(0,'ca-ca-ca',5,0,1,222))
Angles.append(Angle(1,'ca-ca-ha',5,0,8,222))
Angles.append(Angle(2,'ca-ca-ca',0,5,4,222))
Angles.append(Angle(3,'ca-ca-ce',0,5,6,222))
Angles.append(Angle(4,'ca-ca-ha',1,0,8,222))
Angles.append(Angle(5,'ca-ca-ca',0,1,2,222))
Angles.append(Angle(6,'ca-ca-ha',0,1,9,222))
Angles.append(Angle(7,'ca-ca-ha',2,1,9,222))
Angles.append(Angle(8,'ca-ca-ca',1,2,3,222))
Angles.append(Angle(9,'ca-ca-ha',1,2,10,222))
Angles.append(Angle(10,'ca-ca-ha',3,2,10,222))
Angles.append(Angle(11,'ca-ca-ca',2,3,4,222))
Angles.append(Angle(12,'ca-ca-ha',2,3,11,222))
Angles.append(Angle(13,'ca-ca-ha',4,3,11,222))
Angles.append(Angle(14,'ca-ca-ca',3,4,5,222))
Angles.append(Angle(15,'ca-ca-ha',3,4,12,222))
Angles.append(Angle(16,'ca-ca-ha',5,4,12,222))
Angles.append(Angle(17,'ca-ca-ce',4,5,6,222))
Angles.append(Angle(18,'ca-ce-c2',5,6,7,222))
Angles.append(Angle(19,'ca-ce-ha',5,6,13,222))
Angles.append(Angle(20,'c2-ce-ha',7,6,13,222))
Angles.append(Angle(21,'ce-c2-ha',6,7,14,222))
Angles.append(Angle(22,'ce-c2-ha',6,7,15,222))
Angles.append(Angle(23,'ha-c2-ha',14,7,15,222))
Torsions.append(Torsion(0,'ca-ca-ca-ca',4,5,0,1,333))
Torsions.append(Torsion(1,'ce-ca-ca-ca',6,5,0,1,333))
Torsions.append(Torsion(2,'ca-ca-ca-ca',5,0,1,2,333))
Torsions.append(Torsion(3,'ca-ca-ca-ha',5,0,1,9,333))
Torsions.append(Torsion(4,'ca-ca-ca-ha',4,5,0,8,333))
Torsions.append(Torsion(5,'ce-ca-ca-ha',6,5,0,8,333))
Torsions.append(Torsion(6,'ca-ca-ca-ca',0,5,4,3,333))
Torsions.append(Torsion(7,'ca-ca-ca-ha',0,5,4,12,333))
Torsions.append(Torsion(8,'ca-ca-ce-c2',0,5,6,7,333))
Torsions.append(Torsion(9,'ca-ca-ce-ha',0,5,6,13,333))
Torsions.append(Torsion(10,'ca-ca-ca-ha',2,1,0,8,333))
Torsions.append(Torsion(11,'ha-ca-ca-ha',9,1,0,8,333))
Torsions.append(Torsion(12,'ca-ca-ca-ca',5,0,1,2,333))
Torsions.append(Torsion(13,'ca-ca-ca-ca',0,1,2,3,333))
Torsions.append(Torsion(14,'ca-ca-ca-ha',0,1,2,10,333))
Torsions.append(Torsion(15,'ca-ca-ca-ha',5,0,1,9,333))
Torsions.append(Torsion(16,'ca-ca-ca-ha',3,2,1,9,333))
Torsions.append(Torsion(17,'ha-ca-ca-ha',10,2,1,9,333))
Torsions.append(Torsion(18,'ca-ca-ca-ca',0,1,2,3,333))
Torsions.append(Torsion(19,'ca-ca-ca-ca',1,2,3,4,333))
Torsions.append(Torsion(20,'ca-ca-ca-ha',1,2,3,11,333))
Torsions.append(Torsion(21,'ca-ca-ca-ha',0,1,2,10,333))
Torsions.append(Torsion(22,'ca-ca-ca-ha',4,3,2,10,333))
Torsions.append(Torsion(23,'ha-ca-ca-ha',11,3,2,10,333))
Torsions.append(Torsion(24,'ca-ca-ca-ca',1,2,3,4,333))
Torsions.append(Torsion(25,'ca-ca-ca-ca',2,3,4,5,333))
Torsions.append(Torsion(26,'ca-ca-ca-ha',2,3,4,12,333))
Torsions.append(Torsion(27,'ca-ca-ca-ha',1,2,3,11,333))
Torsions.append(Torsion(28,'ca-ca-ca-ha',5,4,3,11,333))
Torsions.append(Torsion(29,'ha-ca-ca-ha',12,4,3,11,333))
Torsions.append(Torsion(30,'ca-ca-ca-ca',2,3,4,5,333))
Torsions.append(Torsion(31,'ca-ca-ca-ce',3,4,5,6,333))
Torsions.append(Torsion(32,'ca-ca-ca-ha',2,3,4,12,333))
Torsions.append(Torsion(33,'ca-ca-ca-ha',0,5,4,12,333))
Torsions.append(Torsion(34,'ce-ca-ca-ha',6,5,4,12,333))
Torsions.append(Torsion(35,'ca-ca-ca-ce',3,4,5,6,333))
Torsions.append(Torsion(36,'ca-ca-ce-c2',4,5,6,7,333))
Torsions.append(Torsion(37,'ca-ca-ce-ha',4,5,6,13,333))
Torsions.append(Torsion(38,'ca-ca-ce-c2',0,5,6,7,333))
Torsions.append(Torsion(39,'ca-ca-ce-c2',4,5,6,7,333))
Torsions.append(Torsion(40,'ca-ce-c2-ha',5,6,7,14,333))
Torsions.append(Torsion(41,'ca-ce-c2-ha',5,6,7,15,333))
Torsions.append(Torsion(42,'ca-ca-ce-ha',0,5,6,13,333))
Torsions.append(Torsion(43,'ca-ca-ce-ha',4,5,6,13,333))
Torsions.append(Torsion(44,'ha-c2-ce-ha',14,7,6,13,333))
Torsions.append(Torsion(45,'ha-c2-ce-ha',15,7,6,13,333))
Torsions.append(Torsion(46,'ca-ce-c2-ha',5,6,7,14,333))
Torsions.append(Torsion(47,'ca-ce-c2-ha',5,6,7,15,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)