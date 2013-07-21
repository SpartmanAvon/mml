

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


Atoms.append(Atom(0,'n3',0.880000,0.198000,-0.170000,np.array([0.880000,0.198000,-0.170000]),[1,14,15],[0,3,2,11],[1,4,12,13,14,15,16,17],-0.905800))
Atoms.append(Atom(1,'c3',2.352000,0.133000,-0.049000,np.array([2.352000,0.133000,-0.049000]),[0,11,3,2],[1,4,12,13,14,15,16,17],[0,2,3,5,10,11,23],0.090500))
Atoms.append(Atom(2,'h1',2.655000,0.876000,0.697000,np.array([2.655000,0.876000,0.697000]),[1],[0,3,2,11],[1,4,12,13,14,15,16,17],0.108700))
Atoms.append(Atom(3,'c3',2.847000,-1.273000,0.351000,np.array([2.847000,-1.273000,0.351000]),[1,4,16,17],[0,2,3,5,10,11],[1,4,6,9,12,13,14,15,16,17,18,22],-0.026100))
Atoms.append(Atom(4,'ca',2.354000,-1.871000,1.654000,np.array([2.354000,-1.871000,1.654000]),[3,5,10],[1,4,6,9,16,17,18,22],[0,2,3,5,7,10,11,19,21],-0.124300))
Atoms.append(Atom(5,'ca',2.559000,-3.245000,1.872000,np.array([2.559000,-3.245000,1.872000]),[4,6,18],[19,10,3,5,7],[1,4,6,8,9,16,17,18,22],-0.078000))
Atoms.append(Atom(6,'ca',2.142000,-3.854000,3.057000,np.array([2.142000,-3.854000,3.057000]),[5,7,19],[8,9,18,4,6],[3,5,7,10,19,20,21],-0.187000))
Atoms.append(Atom(7,'ca',1.522000,-3.095000,4.037000,np.array([1.522000,-3.095000,4.037000]),[6,9,8],[5,7,10,19,20,21],[4,6,8,9,18,22],0.130100))
Atoms.append(Atom(8,'oh',1.121000,-3.728000,5.176000,np.array([1.121000,-3.728000,5.176000]),[7,20],[8,9,6],[5,7,10,19,20,21],-0.496100))
Atoms.append(Atom(9,'ca',1.323000,-1.731000,3.857000,np.array([1.323000,-1.731000,3.857000]),[7,10,21],[8,9,4,22,6],[3,5,7,10,19,20,21],-0.187000))
Atoms.append(Atom(10,'ca',1.745000,-1.122000,2.671000,np.array([1.745000,-1.122000,2.671000]),[4,9,22],[10,3,21,5,7],[1,4,6,8,9,16,17,18,22],-0.078000))
Atoms.append(Atom(11,'c',3.051000,0.525000,-1.363000,np.array([3.051000,0.525000,-1.363000]),[1,13,12],[0,3,2,11,23],[1,4,12,13,14,15,16,17],0.570100))
Atoms.append(Atom(12,'oh',2.194000,0.779000,-2.382000,np.array([2.194000,0.779000,-2.382000]),[11,23],[1,12,13],[0,3,2,11,23],-0.582100))
Atoms.append(Atom(13,'o',4.263000,0.597000,-1.504000,np.array([4.263000,0.597000,-1.504000]),[11],[1,12,13],[0,3,2,11,23],-0.479000))
Atoms.append(Atom(14,'hn',0.456000,-0.567000,-0.686000,np.array([0.456000,-0.567000,-0.686000]),[0],[1,14,15],[0,3,2,11],0.363800))
Atoms.append(Atom(15,'hn',0.501000,1.123000,-0.347000,np.array([0.501000,1.123000,-0.347000]),[0],[1,14,15],[0,3,2,11],0.363800))
Atoms.append(Atom(16,'hc',3.944000,-1.256000,0.406000,np.array([3.944000,-1.256000,0.406000]),[3],[16,1,4,17],[0,2,3,5,10,11],0.054200))
Atoms.append(Atom(17,'hc',2.591000,-1.970000,-0.460000,np.array([2.591000,-1.970000,-0.460000]),[3],[16,1,4,17],[0,2,3,5,10,11],0.054200))
Atoms.append(Atom(18,'ha',3.050000,-3.854000,1.115000,np.array([3.050000,-3.854000,1.115000]),[5],[18,4,6],[19,10,3,5,7],0.139000))
Atoms.append(Atom(19,'ha',2.302000,-4.918000,3.212000,np.array([2.302000,-4.918000,3.212000]),[6],[19,5,7],[8,9,18,4,6],0.143500))
Atoms.append(Atom(20,'ho',0.697000,-3.076000,5.758000,np.array([0.697000,-3.076000,5.758000]),[8],[20,7],[8,9,6],0.420000))
Atoms.append(Atom(21,'ha',0.844000,-1.126000,4.620000,np.array([0.844000,-1.126000,4.620000]),[9],[10,21,7],[8,9,4,6,22],0.143500))
Atoms.append(Atom(22,'ha',1.579000,-0.054000,2.558000,np.array([1.579000,-0.054000,2.558000]),[10],[9,4,22],[10,3,5,21,7],0.139000))
Atoms.append(Atom(23,'ho',1.276000,0.648000,-2.079000,np.array([1.276000,0.648000,-2.079000]),[12],[11,23],[1,12,13],0.423000))
Bonds.append(Bond(0,'n3-c3',0,1,111))
Bonds.append(Bond(1,'n3-hn',0,14,111))
Bonds.append(Bond(2,'n3-hn',0,15,111))
Bonds.append(Bond(3,'c3-c',1,11,111))
Bonds.append(Bond(4,'c3-c3',1,3,111))
Bonds.append(Bond(5,'c3-h1',1,2,111))
Bonds.append(Bond(6,'c3-ca',3,4,111))
Bonds.append(Bond(7,'c3-hc',3,16,111))
Bonds.append(Bond(8,'c3-hc',3,17,111))
Bonds.append(Bond(9,'ca-ca',4,5,111))
Bonds.append(Bond(10,'ca-ca',4,10,111))
Bonds.append(Bond(11,'ca-ca',5,6,111))
Bonds.append(Bond(12,'ca-ha',5,18,111))
Bonds.append(Bond(13,'ca-ca',6,7,111))
Bonds.append(Bond(14,'ca-ha',6,19,111))
Bonds.append(Bond(15,'ca-ca',7,9,111))
Bonds.append(Bond(16,'ca-oh',7,8,111))
Bonds.append(Bond(17,'oh-ho',8,20,111))
Bonds.append(Bond(18,'ca-ca',9,10,111))
Bonds.append(Bond(19,'ca-ha',9,21,111))
Bonds.append(Bond(20,'ca-ha',10,22,111))
Bonds.append(Bond(21,'c-o',11,13,111))
Bonds.append(Bond(22,'c-oh',11,12,111))
Bonds.append(Bond(23,'oh-ho',12,23,111))
Angles.append(Angle(0,'c3-n3-hn',1,0,14,222))
Angles.append(Angle(1,'c3-n3-hn',1,0,15,222))
Angles.append(Angle(2,'n3-c3-c',0,1,11,222))
Angles.append(Angle(3,'n3-c3-c3',0,1,3,222))
Angles.append(Angle(4,'n3-c3-h1',0,1,2,222))
Angles.append(Angle(5,'hn-n3-hn',14,0,15,222))
Angles.append(Angle(6,'c-c3-c3',11,1,3,222))
Angles.append(Angle(7,'c-c3-h1',11,1,2,222))
Angles.append(Angle(8,'c3-c-o',1,11,13,222))
Angles.append(Angle(9,'c3-c-oh',1,11,12,222))
Angles.append(Angle(10,'c3-c3-h1',3,1,2,222))
Angles.append(Angle(11,'c3-c3-ca',1,3,4,222))
Angles.append(Angle(12,'c3-c3-hc',1,3,16,222))
Angles.append(Angle(13,'c3-c3-hc',1,3,17,222))
Angles.append(Angle(14,'ca-c3-hc',4,3,16,222))
Angles.append(Angle(15,'ca-c3-hc',4,3,17,222))
Angles.append(Angle(16,'c3-ca-ca',3,4,5,222))
Angles.append(Angle(17,'c3-ca-ca',3,4,10,222))
Angles.append(Angle(18,'hc-c3-hc',16,3,17,222))
Angles.append(Angle(19,'ca-ca-ca',5,4,10,222))
Angles.append(Angle(20,'ca-ca-ca',4,5,6,222))
Angles.append(Angle(21,'ca-ca-ha',4,5,18,222))
Angles.append(Angle(22,'ca-ca-ca',4,10,9,222))
Angles.append(Angle(23,'ca-ca-ha',4,10,22,222))
Angles.append(Angle(24,'ca-ca-ha',6,5,18,222))
Angles.append(Angle(25,'ca-ca-ca',5,6,7,222))
Angles.append(Angle(26,'ca-ca-ha',5,6,19,222))
Angles.append(Angle(27,'ca-ca-ha',7,6,19,222))
Angles.append(Angle(28,'ca-ca-ca',6,7,9,222))
Angles.append(Angle(29,'ca-ca-oh',6,7,8,222))
Angles.append(Angle(30,'ca-ca-oh',9,7,8,222))
Angles.append(Angle(31,'ca-ca-ca',7,9,10,222))
Angles.append(Angle(32,'ca-ca-ha',7,9,21,222))
Angles.append(Angle(33,'ca-oh-ho',7,8,20,222))
Angles.append(Angle(34,'ca-ca-ha',10,9,21,222))
Angles.append(Angle(35,'ca-ca-ha',9,10,22,222))
Angles.append(Angle(36,'o-c-oh',13,11,12,222))
Angles.append(Angle(37,'c-oh-ho',11,12,23,222))
Torsions.append(Torsion(0,'c-c3-n3-hn',11,1,0,14,333))
Torsions.append(Torsion(1,'c3-c3-n3-hn',3,1,0,14,333))
Torsions.append(Torsion(2,'h1-c3-n3-hn',2,1,0,14,333))
Torsions.append(Torsion(3,'c-c3-n3-hn',11,1,0,15,333))
Torsions.append(Torsion(4,'c3-c3-n3-hn',3,1,0,15,333))
Torsions.append(Torsion(5,'h1-c3-n3-hn',2,1,0,15,333))
Torsions.append(Torsion(6,'n3-c3-c-o',0,1,11,13,333))
Torsions.append(Torsion(7,'n3-c3-c-oh',0,1,11,12,333))
Torsions.append(Torsion(8,'n3-c3-c3-ca',0,1,3,4,333))
Torsions.append(Torsion(9,'n3-c3-c3-hc',0,1,3,16,333))
Torsions.append(Torsion(10,'n3-c3-c3-hc',0,1,3,17,333))
Torsions.append(Torsion(11,'o-c-c3-c3',13,11,1,3,333))
Torsions.append(Torsion(12,'oh-c-c3-c3',12,11,1,3,333))
Torsions.append(Torsion(13,'c-c3-c3-ca',11,1,3,4,333))
Torsions.append(Torsion(14,'c-c3-c3-hc',11,1,3,16,333))
Torsions.append(Torsion(15,'c-c3-c3-hc',11,1,3,17,333))
Torsions.append(Torsion(16,'o-c-c3-h1',13,11,1,2,333))
Torsions.append(Torsion(17,'oh-c-c3-h1',12,11,1,2,333))
Torsions.append(Torsion(18,'n3-c3-c-o',0,1,11,13,333))
Torsions.append(Torsion(19,'n3-c3-c-oh',0,1,11,12,333))
Torsions.append(Torsion(20,'c3-c-oh-ho',1,11,12,23,333))
Torsions.append(Torsion(21,'ca-c3-c3-h1',4,3,1,2,333))
Torsions.append(Torsion(22,'hc-c3-c3-h1',16,3,1,2,333))
Torsions.append(Torsion(23,'hc-c3-c3-h1',17,3,1,2,333))
Torsions.append(Torsion(24,'n3-c3-c3-ca',0,1,3,4,333))
Torsions.append(Torsion(25,'c-c3-c3-ca',11,1,3,4,333))
Torsions.append(Torsion(26,'c3-c3-ca-ca',1,3,4,5,333))
Torsions.append(Torsion(27,'c3-c3-ca-ca',1,3,4,10,333))
Torsions.append(Torsion(28,'n3-c3-c3-hc',0,1,3,16,333))
Torsions.append(Torsion(29,'c-c3-c3-hc',11,1,3,16,333))
Torsions.append(Torsion(30,'n3-c3-c3-hc',0,1,3,17,333))
Torsions.append(Torsion(31,'c-c3-c3-hc',11,1,3,17,333))
Torsions.append(Torsion(32,'ca-ca-c3-hc',5,4,3,16,333))
Torsions.append(Torsion(33,'ca-ca-c3-hc',10,4,3,16,333))
Torsions.append(Torsion(34,'ca-ca-c3-hc',5,4,3,17,333))
Torsions.append(Torsion(35,'ca-ca-c3-hc',10,4,3,17,333))
Torsions.append(Torsion(36,'c3-c3-ca-ca',1,3,4,5,333))
Torsions.append(Torsion(37,'c3-ca-ca-ca',3,4,5,6,333))
Torsions.append(Torsion(38,'c3-ca-ca-ha',3,4,5,18,333))
Torsions.append(Torsion(39,'c3-c3-ca-ca',1,3,4,10,333))
Torsions.append(Torsion(40,'c3-ca-ca-ca',3,4,10,9,333))
Torsions.append(Torsion(41,'c3-ca-ca-ha',3,4,10,22,333))
Torsions.append(Torsion(42,'ca-ca-ca-ca',6,5,4,10,333))
Torsions.append(Torsion(43,'ha-ca-ca-ca',18,5,4,10,333))
Torsions.append(Torsion(44,'ca-ca-ca-ca',5,4,10,9,333))
Torsions.append(Torsion(45,'ca-ca-ca-ha',5,4,10,22,333))
Torsions.append(Torsion(46,'c3-ca-ca-ca',3,4,5,6,333))
Torsions.append(Torsion(47,'ca-ca-ca-ca',4,5,6,7,333))
Torsions.append(Torsion(48,'ca-ca-ca-ha',4,5,6,19,333))
Torsions.append(Torsion(49,'c3-ca-ca-ha',3,4,5,18,333))
Torsions.append(Torsion(50,'c3-ca-ca-ca',3,4,10,9,333))
Torsions.append(Torsion(51,'ca-ca-ca-ca',5,4,10,9,333))
Torsions.append(Torsion(52,'ca-ca-ca-ca',4,10,9,7,333))
Torsions.append(Torsion(53,'ca-ca-ca-ha',4,10,9,21,333))
Torsions.append(Torsion(54,'c3-ca-ca-ha',3,4,10,22,333))
Torsions.append(Torsion(55,'ca-ca-ca-ha',5,4,10,22,333))
Torsions.append(Torsion(56,'ca-ca-ca-ha',7,6,5,18,333))
Torsions.append(Torsion(57,'ha-ca-ca-ha',19,6,5,18,333))
Torsions.append(Torsion(58,'ca-ca-ca-ca',4,5,6,7,333))
Torsions.append(Torsion(59,'ca-ca-ca-ca',5,6,7,9,333))
Torsions.append(Torsion(60,'ca-ca-ca-oh',5,6,7,8,333))
Torsions.append(Torsion(61,'ca-ca-ca-ha',4,5,6,19,333))
Torsions.append(Torsion(62,'ca-ca-ca-ha',9,7,6,19,333))
Torsions.append(Torsion(63,'oh-ca-ca-ha',8,7,6,19,333))
Torsions.append(Torsion(64,'ca-ca-ca-ca',5,6,7,9,333))
Torsions.append(Torsion(65,'ca-ca-ca-ca',6,7,9,10,333))
Torsions.append(Torsion(66,'ca-ca-ca-ha',6,7,9,21,333))
Torsions.append(Torsion(67,'ca-ca-ca-oh',5,6,7,8,333))
Torsions.append(Torsion(68,'ca-ca-oh-ho',6,7,8,20,333))
Torsions.append(Torsion(69,'ca-ca-ca-oh',10,9,7,8,333))
Torsions.append(Torsion(70,'ha-ca-ca-oh',21,9,7,8,333))
Torsions.append(Torsion(71,'ca-ca-oh-ho',9,7,8,20,333))
Torsions.append(Torsion(72,'ca-ca-ca-ca',6,7,9,10,333))
Torsions.append(Torsion(73,'ca-ca-ca-ha',7,9,10,22,333))
Torsions.append(Torsion(74,'ca-ca-ca-ha',6,7,9,21,333))
Torsions.append(Torsion(75,'ca-ca-oh-ho',6,7,8,20,333))
Torsions.append(Torsion(76,'ca-ca-oh-ho',9,7,8,20,333))
Torsions.append(Torsion(77,'ca-ca-ca-ha',4,10,9,21,333))
Torsions.append(Torsion(78,'ha-ca-ca-ha',22,10,9,21,333))
Torsions.append(Torsion(79,'ca-ca-ca-ha',7,9,10,22,333))
Torsions.append(Torsion(80,'o-c-oh-ho',13,11,12,23,333))
Torsions.append(Torsion(81,'c3-c-oh-ho',1,11,12,23,333))
Torsions.append(Torsion(82,'o-c-oh-ho',13,11,12,23,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)