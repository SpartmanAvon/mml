

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


Atoms.append(Atom(0,'o',4.516000,0.449000,-0.871000,np.array([4.516000,0.449000,-0.871000]),[1],[0,8,2],[16,1,3,4,7],-0.509000))
Atoms.append(Atom(1,'c',4.147000,-0.710000,-0.978000,np.array([4.147000,-0.710000,-0.978000]),[0,8,2],[16,1,3,4,7],[0,2,5,6,8,9,10,15],0.632100))
Atoms.append(Atom(2,'c3',3.099000,-1.389000,-0.084000,np.array([3.099000,-1.389000,-0.084000]),[7,4,3,1],[0,2,5,6,8,9,10,15],[1,3,4,5,6,7,11,12,13,14,16],0.071500))
Atoms.append(Atom(3,'h1',2.164000,-0.824000,-0.169000,np.array([2.164000,-0.824000,-0.169000]),[2],[1,3,4,7],[0,2,5,6,8,9,10,15],0.079700))
Atoms.append(Atom(4,'c3',3.588000,-1.486000,1.354000,np.array([3.588000,-1.486000,1.354000]),[2,5,9,10],[1,3,4,6,7,11,12],[0,2,5,6,7,8,9,10,13,14,15],-0.090400))
Atoms.append(Atom(5,'c3',4.049000,-2.925000,1.487000,np.array([4.049000,-2.925000,1.487000]),[4,6,11,12],[2,5,7,9,10,13,14],[1,2,3,4,6,7,11,12,15],-0.104400))
Atoms.append(Atom(6,'c3',3.070000,-3.668000,0.604000,np.array([3.070000,-3.668000,0.604000]),[5,7,13,14],[2,4,6,11,12,15],[1,2,3,4,5,7,9,10,13,14],0.147800))
Atoms.append(Atom(7,'n3',2.900000,-2.796000,-0.566000,np.array([2.900000,-2.796000,-0.566000]),[2,6,15],[1,3,4,5,7,13,14],[0,2,4,5,6,8,9,10,11,12,15],-0.822200))
Atoms.append(Atom(8,'oh',4.638000,-1.567000,-1.911000,np.array([4.638000,-1.567000,-1.911000]),[1,16],[0,8,2],[16,1,3,4,7],-0.574100))
Atoms.append(Atom(9,'hc',2.751000,-1.311000,2.041000,np.array([2.751000,-1.311000,2.041000]),[4],[9,2,10,5],[1,3,4,6,7,11,12],0.068200))
Atoms.append(Atom(10,'hc',4.389000,-0.784000,1.605000,np.array([4.389000,-0.784000,1.605000]),[4],[9,2,10,5],[1,3,4,6,7,11,12],0.068200))
Atoms.append(Atom(11,'hc',5.071000,-3.033000,1.106000,np.array([5.071000,-3.033000,1.106000]),[5],[12,11,4,6],[2,5,7,9,10,13,14],0.054700))
Atoms.append(Atom(12,'hc',4.028000,-3.274000,2.523000,np.array([4.028000,-3.274000,2.523000]),[5],[12,11,4,6],[2,5,7,9,10,13,14],0.054700))
Atoms.append(Atom(13,'h1',3.442000,-4.654000,0.311000,np.array([3.442000,-4.654000,0.311000]),[6],[13,5,14,7],[2,4,6,11,12,15],0.052700))
Atoms.append(Atom(14,'h1',2.110000,-3.796000,1.118000,np.array([2.110000,-3.796000,1.118000]),[6],[13,5,14,7],[2,4,6,11,12,15],0.052700))
Atoms.append(Atom(15,'hn',1.940000,-2.893000,-0.911000,np.array([1.940000,-2.893000,-0.911000]),[7],[2,6,15],[1,3,4,5,7,13,14],0.368800))
Atoms.append(Atom(16,'ho',4.172000,-2.427000,-1.745000,np.array([4.172000,-2.427000,-1.745000]),[8],[16,1],[8,0,2],0.447000))
Bonds.append(Bond(0,'o-c',0,1,111))
Bonds.append(Bond(1,'c-oh',1,8,111))
Bonds.append(Bond(2,'c3-n3',2,7,111))
Bonds.append(Bond(3,'c3-c3',2,4,111))
Bonds.append(Bond(4,'c3-h1',2,3,111))
Bonds.append(Bond(5,'c3-c',2,1,111))
Bonds.append(Bond(6,'c3-c3',4,5,111))
Bonds.append(Bond(7,'c3-hc',4,9,111))
Bonds.append(Bond(8,'c3-hc',4,10,111))
Bonds.append(Bond(9,'c3-c3',5,6,111))
Bonds.append(Bond(10,'c3-hc',5,11,111))
Bonds.append(Bond(11,'c3-hc',5,12,111))
Bonds.append(Bond(12,'c3-n3',6,7,111))
Bonds.append(Bond(13,'c3-h1',6,13,111))
Bonds.append(Bond(14,'c3-h1',6,14,111))
Bonds.append(Bond(15,'n3-hn',7,15,111))
Bonds.append(Bond(16,'oh-ho',8,16,111))
Angles.append(Angle(0,'o-c-oh',0,1,8,222))
Angles.append(Angle(1,'o-c-c3',0,1,2,222))
Angles.append(Angle(2,'oh-c-c3',8,1,2,222))
Angles.append(Angle(3,'c-oh-ho',1,8,16,222))
Angles.append(Angle(4,'n3-c3-c3',7,2,4,222))
Angles.append(Angle(5,'n3-c3-h1',7,2,3,222))
Angles.append(Angle(6,'n3-c3-c',7,2,1,222))
Angles.append(Angle(7,'c3-n3-c3',2,7,6,222))
Angles.append(Angle(8,'c3-n3-hn',2,7,15,222))
Angles.append(Angle(9,'c3-c3-h1',4,2,3,222))
Angles.append(Angle(10,'c3-c3-c',4,2,1,222))
Angles.append(Angle(11,'c3-c3-c3',2,4,5,222))
Angles.append(Angle(12,'c3-c3-hc',2,4,9,222))
Angles.append(Angle(13,'c3-c3-hc',2,4,10,222))
Angles.append(Angle(14,'h1-c3-c',3,2,1,222))
Angles.append(Angle(15,'c3-c3-hc',5,4,9,222))
Angles.append(Angle(16,'c3-c3-hc',5,4,10,222))
Angles.append(Angle(17,'c3-c3-c3',4,5,6,222))
Angles.append(Angle(18,'c3-c3-hc',4,5,11,222))
Angles.append(Angle(19,'c3-c3-hc',4,5,12,222))
Angles.append(Angle(20,'hc-c3-hc',9,4,10,222))
Angles.append(Angle(21,'c3-c3-hc',6,5,11,222))
Angles.append(Angle(22,'c3-c3-hc',6,5,12,222))
Angles.append(Angle(23,'c3-c3-n3',5,6,7,222))
Angles.append(Angle(24,'c3-c3-h1',5,6,13,222))
Angles.append(Angle(25,'c3-c3-h1',5,6,14,222))
Angles.append(Angle(26,'hc-c3-hc',11,5,12,222))
Angles.append(Angle(27,'n3-c3-h1',7,6,13,222))
Angles.append(Angle(28,'n3-c3-h1',7,6,14,222))
Angles.append(Angle(29,'c3-n3-hn',6,7,15,222))
Angles.append(Angle(30,'h1-c3-h1',13,6,14,222))
Torsions.append(Torsion(0,'o-c-oh-ho',0,1,8,16,333))
Torsions.append(Torsion(1,'o-c-c3-n3',0,1,2,7,333))
Torsions.append(Torsion(2,'o-c-c3-c3',0,1,2,4,333))
Torsions.append(Torsion(3,'o-c-c3-h1',0,1,2,3,333))
Torsions.append(Torsion(4,'ho-oh-c-c3',16,8,1,2,333))
Torsions.append(Torsion(5,'oh-c-c3-n3',8,1,2,7,333))
Torsions.append(Torsion(6,'oh-c-c3-c3',8,1,2,4,333))
Torsions.append(Torsion(7,'oh-c-c3-h1',8,1,2,3,333))
Torsions.append(Torsion(8,'o-c-oh-ho',0,1,8,16,333))
Torsions.append(Torsion(9,'c3-n3-c3-c3',6,7,2,4,333))
Torsions.append(Torsion(10,'hn-n3-c3-c3',15,7,2,4,333))
Torsions.append(Torsion(11,'n3-c3-c3-c3',7,2,4,5,333))
Torsions.append(Torsion(12,'n3-c3-c3-hc',7,2,4,9,333))
Torsions.append(Torsion(13,'n3-c3-c3-hc',7,2,4,10,333))
Torsions.append(Torsion(14,'c3-n3-c3-h1',6,7,2,3,333))
Torsions.append(Torsion(15,'hn-n3-c3-h1',15,7,2,3,333))
Torsions.append(Torsion(16,'c3-n3-c3-c',6,7,2,1,333))
Torsions.append(Torsion(17,'hn-n3-c3-c',15,7,2,1,333))
Torsions.append(Torsion(18,'c3-n3-c3-c3',2,7,6,5,333))
Torsions.append(Torsion(19,'c3-n3-c3-h1',2,7,6,13,333))
Torsions.append(Torsion(20,'c3-n3-c3-h1',2,7,6,14,333))
Torsions.append(Torsion(21,'c3-c3-c3-h1',5,4,2,3,333))
Torsions.append(Torsion(22,'hc-c3-c3-h1',9,4,2,3,333))
Torsions.append(Torsion(23,'hc-c3-c3-h1',10,4,2,3,333))
Torsions.append(Torsion(24,'c3-c3-c3-c',5,4,2,1,333))
Torsions.append(Torsion(25,'hc-c3-c3-c',9,4,2,1,333))
Torsions.append(Torsion(26,'hc-c3-c3-c',10,4,2,1,333))
Torsions.append(Torsion(27,'n3-c3-c3-c3',7,2,4,5,333))
Torsions.append(Torsion(28,'c3-c3-c3-c3',2,4,5,6,333))
Torsions.append(Torsion(29,'c3-c3-c3-hc',2,4,5,11,333))
Torsions.append(Torsion(30,'c3-c3-c3-hc',2,4,5,12,333))
Torsions.append(Torsion(31,'n3-c3-c3-hc',7,2,4,9,333))
Torsions.append(Torsion(32,'n3-c3-c3-hc',7,2,4,10,333))
Torsions.append(Torsion(33,'c3-c3-c3-hc',6,5,4,9,333))
Torsions.append(Torsion(34,'hc-c3-c3-hc',11,5,4,9,333))
Torsions.append(Torsion(35,'hc-c3-c3-hc',12,5,4,9,333))
Torsions.append(Torsion(36,'c3-c3-c3-hc',6,5,4,10,333))
Torsions.append(Torsion(37,'hc-c3-c3-hc',11,5,4,10,333))
Torsions.append(Torsion(38,'hc-c3-c3-hc',12,5,4,10,333))
Torsions.append(Torsion(39,'c3-c3-c3-c3',2,4,5,6,333))
Torsions.append(Torsion(40,'c3-c3-c3-n3',4,5,6,7,333))
Torsions.append(Torsion(41,'c3-c3-c3-h1',4,5,6,13,333))
Torsions.append(Torsion(42,'c3-c3-c3-h1',4,5,6,14,333))
Torsions.append(Torsion(43,'c3-c3-c3-hc',2,4,5,11,333))
Torsions.append(Torsion(44,'c3-c3-c3-hc',2,4,5,12,333))
Torsions.append(Torsion(45,'n3-c3-c3-hc',7,6,5,11,333))
Torsions.append(Torsion(46,'h1-c3-c3-hc',13,6,5,11,333))
Torsions.append(Torsion(47,'h1-c3-c3-hc',14,6,5,11,333))
Torsions.append(Torsion(48,'n3-c3-c3-hc',7,6,5,12,333))
Torsions.append(Torsion(49,'h1-c3-c3-hc',13,6,5,12,333))
Torsions.append(Torsion(50,'h1-c3-c3-hc',14,6,5,12,333))
Torsions.append(Torsion(51,'c3-c3-c3-n3',4,5,6,7,333))
Torsions.append(Torsion(52,'c3-c3-n3-hn',5,6,7,15,333))
Torsions.append(Torsion(53,'c3-c3-c3-h1',4,5,6,13,333))
Torsions.append(Torsion(54,'c3-c3-c3-h1',4,5,6,14,333))
Torsions.append(Torsion(55,'c3-n3-c3-h1',2,7,6,13,333))
Torsions.append(Torsion(56,'hn-n3-c3-h1',15,7,6,13,333))
Torsions.append(Torsion(57,'c3-n3-c3-h1',2,7,6,14,333))
Torsions.append(Torsion(58,'hn-n3-c3-h1',15,7,6,14,333))
Torsions.append(Torsion(59,'c3-c3-n3-hn',5,6,7,15,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)
