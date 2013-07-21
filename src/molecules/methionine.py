

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


Atoms.append(Atom(0,'oh',1.207000,0.084000,-0.690000,np.array([1.207000,0.084000,-0.690000]),[1,10],[0,9,2],[1,10,3,4,5],-0.600100))
Atoms.append(Atom(1,'c',2.323000,0.029000,0.061000,np.array([2.323000,0.029000,0.061000]),[0,9,2],[1,10,3,4,5],[0,2,6,9,11,12,13,14],0.585100))
Atoms.append(Atom(2,'c3',3.056000,-1.320000,0.006000,np.array([3.056000,-1.320000,0.006000]),[1,5,4,3],[0,2,6,9,11,12,13,14],[1,3,4,5,7,10,15,16],0.138500))
Atoms.append(Atom(3,'h1',3.605000,-1.345000,-0.943000,np.array([3.605000,-1.345000,-0.943000]),[2],[1,3,4,5],[0,2,6,9,11,12,13,14],0.093700))
Atoms.append(Atom(4,'n3',4.044000,-1.386000,1.109000,np.array([4.044000,-1.386000,1.109000]),[2,11,12],[1,3,4,5],[0,2,6,9,11,12,13,14],-0.895800))
Atoms.append(Atom(5,'c3',2.084000,-2.507000,0.077000,np.array([2.084000,-2.507000,0.077000]),[2,6,13,14],[1,3,4,5,7,15,16],[0,2,6,8,9,11,12,13,14],-0.065400))
Atoms.append(Atom(6,'c3',2.802000,-3.853000,-0.001000,np.array([2.802000,-3.853000,-0.001000]),[5,7,15,16],[8,2,14,13,6],[1,3,4,5,7,15,16,17,18,19],-0.007300))
Atoms.append(Atom(7,'ss',1.581000,-5.206000,-0.077000,np.array([1.581000,-5.206000,-0.077000]),[6,8],[5,7,15,16,17,18,19],[8,2,14,13,6],-0.300200))
Atoms.append(Atom(8,'c3',2.730000,-6.601000,-0.143000,np.array([2.730000,-6.601000,-0.143000]),[7,17,18,19],[8,6],[5,7,15,16,17,18,19],-0.039000))
Atoms.append(Atom(9,'o',2.702000,1.022000,0.667000,np.array([2.702000,1.022000,0.667000]),[1],[0,9,2],[1,10,3,4,5],-0.558000))
Atoms.append(Atom(10,'ho',0.874000,0.995000,-0.562000,np.array([0.874000,0.995000,-0.562000]),[0],[1,10],[0,9,2],0.446000))
Atoms.append(Atom(11,'hn',3.542000,-1.317000,1.998000,np.array([3.542000,-1.317000,1.998000]),[4],[2,11,12],[1,3,4,5],0.366800))
Atoms.append(Atom(12,'hn',4.601000,-0.526000,1.077000,np.array([4.601000,-0.526000,1.077000]),[4],[2,11,12],[1,3,4,5],0.366800))
Atoms.append(Atom(13,'hc',1.373000,-2.430000,-0.757000,np.array([1.373000,-2.430000,-0.757000]),[5],[2,14,13,6],[1,3,4,5,7,15,16],0.071200))
Atoms.append(Atom(14,'hc',1.490000,-2.445000,0.999000,np.array([1.490000,-2.445000,0.999000]),[5],[2,14,13,6],[1,3,4,5,7,15,16],0.071200))
Atoms.append(Atom(15,'h1',3.433000,-4.009000,0.880000,np.array([3.433000,-4.009000,0.880000]),[6],[16,15,5,7],[8,2,14,13,6],0.068700))
Atoms.append(Atom(16,'h1',3.430000,-3.898000,-0.897000,np.array([3.430000,-3.898000,-0.897000]),[6],[16,15,5,7],[8,2,14,13,6],0.068700))
Atoms.append(Atom(17,'h1',2.162000,-7.533000,-0.202000,np.array([2.162000,-7.533000,-0.202000]),[8],[17,18,19,7],[8,6],0.063367))
Atoms.append(Atom(18,'h1',3.349000,-6.627000,0.757000,np.array([3.349000,-6.627000,0.757000]),[8],[17,18,19,7],[8,6],0.063367))
Atoms.append(Atom(19,'h1',3.368000,-6.527000,-1.027000,np.array([3.368000,-6.527000,-1.027000]),[8],[17,18,19,7],[8,6],0.063367))
Bonds.append(Bond(0,'oh-c',0,1,111))
Bonds.append(Bond(1,'oh-ho',0,10,111))
Bonds.append(Bond(2,'c-o',1,9,111))
Bonds.append(Bond(3,'c-c3',1,2,111))
Bonds.append(Bond(4,'c3-c3',2,5,111))
Bonds.append(Bond(5,'c3-n3',2,4,111))
Bonds.append(Bond(6,'c3-h1',2,3,111))
Bonds.append(Bond(7,'n3-hn',4,11,111))
Bonds.append(Bond(8,'n3-hn',4,12,111))
Bonds.append(Bond(9,'c3-c3',5,6,111))
Bonds.append(Bond(10,'c3-hc',5,13,111))
Bonds.append(Bond(11,'c3-hc',5,14,111))
Bonds.append(Bond(12,'c3-ss',6,7,111))
Bonds.append(Bond(13,'c3-h1',6,15,111))
Bonds.append(Bond(14,'c3-h1',6,16,111))
Bonds.append(Bond(15,'ss-c3',7,8,111))
Bonds.append(Bond(16,'c3-h1',8,17,111))
Bonds.append(Bond(17,'c3-h1',8,18,111))
Bonds.append(Bond(18,'c3-h1',8,19,111))
Angles.append(Angle(0,'c-oh-ho',1,0,10,222))
Angles.append(Angle(1,'oh-c-o',0,1,9,222))
Angles.append(Angle(2,'oh-c-c3',0,1,2,222))
Angles.append(Angle(3,'o-c-c3',9,1,2,222))
Angles.append(Angle(4,'c-c3-c3',1,2,5,222))
Angles.append(Angle(5,'c-c3-n3',1,2,4,222))
Angles.append(Angle(6,'c-c3-h1',1,2,3,222))
Angles.append(Angle(7,'c3-c3-n3',5,2,4,222))
Angles.append(Angle(8,'c3-c3-h1',5,2,3,222))
Angles.append(Angle(9,'c3-c3-c3',2,5,6,222))
Angles.append(Angle(10,'c3-c3-hc',2,5,13,222))
Angles.append(Angle(11,'c3-c3-hc',2,5,14,222))
Angles.append(Angle(12,'n3-c3-h1',4,2,3,222))
Angles.append(Angle(13,'c3-n3-hn',2,4,11,222))
Angles.append(Angle(14,'c3-n3-hn',2,4,12,222))
Angles.append(Angle(15,'hn-n3-hn',11,4,12,222))
Angles.append(Angle(16,'c3-c3-hc',6,5,13,222))
Angles.append(Angle(17,'c3-c3-hc',6,5,14,222))
Angles.append(Angle(18,'c3-c3-ss',5,6,7,222))
Angles.append(Angle(19,'c3-c3-h1',5,6,15,222))
Angles.append(Angle(20,'c3-c3-h1',5,6,16,222))
Angles.append(Angle(21,'hc-c3-hc',13,5,14,222))
Angles.append(Angle(22,'ss-c3-h1',7,6,15,222))
Angles.append(Angle(23,'ss-c3-h1',7,6,16,222))
Angles.append(Angle(24,'c3-ss-c3',6,7,8,222))
Angles.append(Angle(25,'h1-c3-h1',15,6,16,222))
Angles.append(Angle(26,'ss-c3-h1',7,8,17,222))
Angles.append(Angle(27,'ss-c3-h1',7,8,18,222))
Angles.append(Angle(28,'ss-c3-h1',7,8,19,222))
Angles.append(Angle(29,'h1-c3-h1',17,8,18,222))
Angles.append(Angle(30,'h1-c3-h1',17,8,19,222))
Angles.append(Angle(31,'h1-c3-h1',18,8,19,222))
Torsions.append(Torsion(0,'o-c-oh-ho',9,1,0,10,333))
Torsions.append(Torsion(1,'c3-c-oh-ho',2,1,0,10,333))
Torsions.append(Torsion(2,'oh-c-c3-c3',0,1,2,5,333))
Torsions.append(Torsion(3,'oh-c-c3-n3',0,1,2,4,333))
Torsions.append(Torsion(4,'oh-c-c3-h1',0,1,2,3,333))
Torsions.append(Torsion(5,'o-c-c3-c3',9,1,2,5,333))
Torsions.append(Torsion(6,'o-c-c3-n3',9,1,2,4,333))
Torsions.append(Torsion(7,'o-c-c3-h1',9,1,2,3,333))
Torsions.append(Torsion(8,'oh-c-c3-c3',0,1,2,5,333))
Torsions.append(Torsion(9,'o-c-c3-c3',9,1,2,5,333))
Torsions.append(Torsion(10,'c-c3-c3-c3',1,2,5,6,333))
Torsions.append(Torsion(11,'c-c3-c3-hc',1,2,5,13,333))
Torsions.append(Torsion(12,'c-c3-c3-hc',1,2,5,14,333))
Torsions.append(Torsion(13,'oh-c-c3-n3',0,1,2,4,333))
Torsions.append(Torsion(14,'o-c-c3-n3',9,1,2,4,333))
Torsions.append(Torsion(15,'c-c3-n3-hn',1,2,4,11,333))
Torsions.append(Torsion(16,'c-c3-n3-hn',1,2,4,12,333))
Torsions.append(Torsion(17,'oh-c-c3-h1',0,1,2,3,333))
Torsions.append(Torsion(18,'o-c-c3-h1',9,1,2,3,333))
Torsions.append(Torsion(19,'c3-c3-c3-n3',6,5,2,4,333))
Torsions.append(Torsion(20,'hc-c3-c3-n3',13,5,2,4,333))
Torsions.append(Torsion(21,'hc-c3-c3-n3',14,5,2,4,333))
Torsions.append(Torsion(22,'c3-c3-n3-hn',5,2,4,11,333))
Torsions.append(Torsion(23,'c3-c3-n3-hn',5,2,4,12,333))
Torsions.append(Torsion(24,'c3-c3-c3-h1',6,5,2,3,333))
Torsions.append(Torsion(25,'hc-c3-c3-h1',13,5,2,3,333))
Torsions.append(Torsion(26,'hc-c3-c3-h1',14,5,2,3,333))
Torsions.append(Torsion(27,'c-c3-c3-c3',1,2,5,6,333))
Torsions.append(Torsion(28,'c3-c3-c3-ss',2,5,6,7,333))
Torsions.append(Torsion(29,'c3-c3-c3-h1',2,5,6,15,333))
Torsions.append(Torsion(30,'c3-c3-c3-h1',2,5,6,16,333))
Torsions.append(Torsion(31,'c-c3-c3-hc',1,2,5,13,333))
Torsions.append(Torsion(32,'c-c3-c3-hc',1,2,5,14,333))
Torsions.append(Torsion(33,'hn-n3-c3-h1',11,4,2,3,333))
Torsions.append(Torsion(34,'hn-n3-c3-h1',12,4,2,3,333))
Torsions.append(Torsion(35,'c-c3-n3-hn',1,2,4,11,333))
Torsions.append(Torsion(36,'c3-c3-n3-hn',5,2,4,11,333))
Torsions.append(Torsion(37,'c-c3-n3-hn',1,2,4,12,333))
Torsions.append(Torsion(38,'c3-c3-n3-hn',5,2,4,12,333))
Torsions.append(Torsion(39,'ss-c3-c3-hc',7,6,5,13,333))
Torsions.append(Torsion(40,'h1-c3-c3-hc',15,6,5,13,333))
Torsions.append(Torsion(41,'h1-c3-c3-hc',16,6,5,13,333))
Torsions.append(Torsion(42,'ss-c3-c3-hc',7,6,5,14,333))
Torsions.append(Torsion(43,'h1-c3-c3-hc',15,6,5,14,333))
Torsions.append(Torsion(44,'h1-c3-c3-hc',16,6,5,14,333))
Torsions.append(Torsion(45,'c3-c3-c3-ss',2,5,6,7,333))
Torsions.append(Torsion(46,'c3-c3-ss-c3',5,6,7,8,333))
Torsions.append(Torsion(47,'c3-c3-c3-h1',2,5,6,15,333))
Torsions.append(Torsion(48,'c3-c3-c3-h1',2,5,6,16,333))
Torsions.append(Torsion(49,'c3-ss-c3-h1',8,7,6,15,333))
Torsions.append(Torsion(50,'c3-ss-c3-h1',8,7,6,16,333))
Torsions.append(Torsion(51,'c3-c3-ss-c3',5,6,7,8,333))
Torsions.append(Torsion(52,'c3-ss-c3-h1',6,7,8,17,333))
Torsions.append(Torsion(53,'c3-ss-c3-h1',6,7,8,18,333))
Torsions.append(Torsion(54,'c3-ss-c3-h1',6,7,8,19,333))
Torsions.append(Torsion(55,'c3-ss-c3-h1',6,7,8,17,333))
Torsions.append(Torsion(56,'c3-ss-c3-h1',6,7,8,18,333))
Torsions.append(Torsion(57,'c3-ss-c3-h1',6,7,8,19,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)