

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


Atoms.append(Atom(0,'oh',3.533000,-0.685000,3.604000,np.array([3.533000,-0.685000,3.604000]),[1,10],[0,9,2],[3,1,10,11,12],-0.639100))
Atoms.append(Atom(1,'c',3.773000,-2.004000,3.469000,np.array([3.773000,-2.004000,3.469000]),[0,9,2],[3,1,10,11,12],[0,2,4,5,6,9],0.637100))
Atoms.append(Atom(2,'c3',2.876000,-2.715000,2.493000,np.array([2.876000,-2.715000,2.493000]),[1,11,12,3],[0,2,4,5,6,9],[1,3,7,8,10,11,12,13,14],-0.133400))
Atoms.append(Atom(3,'c3',2.086000,-1.764000,1.595000,np.array([2.086000,-1.764000,1.595000]),[5,4,6,2],[1,3,7,8,11,12,13,14],[0,2,4,5,6,9,15],0.097500))
Atoms.append(Atom(4,'h1',1.506000,-1.061000,2.202000,np.array([1.506000,-1.061000,2.202000]),[3],[2,4,5,6],[1,3,7,8,11,12,13,14],0.094700))
Atoms.append(Atom(5,'n3',1.125000,-2.517000,0.762000,np.array([1.125000,-2.517000,0.762000]),[3,13,14],[2,4,5,6],[1,3,7,8,11,12,13,14],-0.892800))
Atoms.append(Atom(6,'c',3.061000,-0.985000,0.687000,np.array([3.061000,-0.985000,0.687000]),[3,8,7],[2,4,5,6,15],[1,3,7,8,11,12,13,14],0.576100))
Atoms.append(Atom(7,'oh',2.967000,0.361000,0.822000,np.array([2.967000,0.361000,0.822000]),[6,15],[8,3,7],[2,4,5,6,15],-0.573100))
Atoms.append(Atom(8,'o',3.846000,-1.497000,-0.098000,np.array([3.846000,-1.497000,-0.098000]),[6],[8,3,7],[2,4,5,6,15],-0.498000))
Atoms.append(Atom(9,'o',4.624000,-2.535000,4.163000,np.array([4.624000,-2.535000,4.163000]),[1],[0,9,2],[3,1,10,11,12],-0.528000))
Atoms.append(Atom(10,'ho',4.208000,-0.408000,4.263000,np.array([4.208000,-0.408000,4.263000]),[0],[1,10],[0,9,2],0.458000))
Atoms.append(Atom(11,'hc',2.186000,-3.330000,3.083000,np.array([2.186000,-3.330000,3.083000]),[2],[3,1,11,12],[0,2,4,5,6,9],0.108700))
Atoms.append(Atom(12,'hc',3.507000,-3.378000,1.889000,np.array([3.507000,-3.378000,1.889000]),[2],[3,1,11,12],[0,2,4,5,6,9],0.108700))
Atoms.append(Atom(13,'hn',0.670000,-1.895000,0.095000,np.array([0.670000,-1.895000,0.095000]),[5],[3,13,14],[2,4,5,6],0.369800))
Atoms.append(Atom(14,'hn',0.395000,-2.927000,1.341000,np.array([0.395000,-2.927000,1.341000]),[5],[3,13,14],[2,4,5,6],0.369800))
Atoms.append(Atom(15,'ho',2.370000,0.648000,1.537000,np.array([2.370000,0.648000,1.537000]),[7],[6,15],[8,3,7],0.444000))
Bonds.append(Bond(0,'oh-c',0,1,111))
Bonds.append(Bond(1,'oh-ho',0,10,111))
Bonds.append(Bond(2,'c-o',1,9,111))
Bonds.append(Bond(3,'c-c3',1,2,111))
Bonds.append(Bond(4,'c3-hc',2,11,111))
Bonds.append(Bond(5,'c3-hc',2,12,111))
Bonds.append(Bond(6,'c3-n3',3,5,111))
Bonds.append(Bond(7,'c3-h1',3,4,111))
Bonds.append(Bond(8,'c3-c',3,6,111))
Bonds.append(Bond(9,'c3-c3',3,2,111))
Bonds.append(Bond(10,'n3-hn',5,13,111))
Bonds.append(Bond(11,'n3-hn',5,14,111))
Bonds.append(Bond(12,'c-o',6,8,111))
Bonds.append(Bond(13,'c-oh',6,7,111))
Bonds.append(Bond(14,'oh-ho',7,15,111))
Angles.append(Angle(0,'c-oh-ho',1,0,10,222))
Angles.append(Angle(1,'oh-c-o',0,1,9,222))
Angles.append(Angle(2,'oh-c-c3',0,1,2,222))
Angles.append(Angle(3,'o-c-c3',9,1,2,222))
Angles.append(Angle(4,'c-c3-hc',1,2,11,222))
Angles.append(Angle(5,'c-c3-hc',1,2,12,222))
Angles.append(Angle(6,'c-c3-c3',1,2,3,222))
Angles.append(Angle(7,'hc-c3-hc',11,2,12,222))
Angles.append(Angle(8,'hc-c3-c3',11,2,3,222))
Angles.append(Angle(9,'hc-c3-c3',12,2,3,222))
Angles.append(Angle(10,'n3-c3-h1',5,3,4,222))
Angles.append(Angle(11,'n3-c3-c',5,3,6,222))
Angles.append(Angle(12,'n3-c3-c3',5,3,2,222))
Angles.append(Angle(13,'c3-n3-hn',3,5,13,222))
Angles.append(Angle(14,'c3-n3-hn',3,5,14,222))
Angles.append(Angle(15,'h1-c3-c',4,3,6,222))
Angles.append(Angle(16,'h1-c3-c3',4,3,2,222))
Angles.append(Angle(17,'c-c3-c3',6,3,2,222))
Angles.append(Angle(18,'c3-c-o',3,6,8,222))
Angles.append(Angle(19,'c3-c-oh',3,6,7,222))
Angles.append(Angle(20,'hn-n3-hn',13,5,14,222))
Angles.append(Angle(21,'o-c-oh',8,6,7,222))
Angles.append(Angle(22,'c-oh-ho',6,7,15,222))
Torsions.append(Torsion(0,'o-c-oh-ho',9,1,0,10,333))
Torsions.append(Torsion(1,'c3-c-oh-ho',2,1,0,10,333))
Torsions.append(Torsion(2,'oh-c-c3-hc',0,1,2,11,333))
Torsions.append(Torsion(3,'oh-c-c3-hc',0,1,2,12,333))
Torsions.append(Torsion(4,'oh-c-c3-c3',0,1,2,3,333))
Torsions.append(Torsion(5,'o-c-c3-hc',9,1,2,11,333))
Torsions.append(Torsion(6,'o-c-c3-hc',9,1,2,12,333))
Torsions.append(Torsion(7,'o-c-c3-c3',9,1,2,3,333))
Torsions.append(Torsion(8,'oh-c-c3-hc',0,1,2,11,333))
Torsions.append(Torsion(9,'o-c-c3-hc',9,1,2,11,333))
Torsions.append(Torsion(10,'oh-c-c3-hc',0,1,2,12,333))
Torsions.append(Torsion(11,'o-c-c3-hc',9,1,2,12,333))
Torsions.append(Torsion(12,'oh-c-c3-c3',0,1,2,3,333))
Torsions.append(Torsion(13,'o-c-c3-c3',9,1,2,3,333))
Torsions.append(Torsion(14,'c-c3-c3-n3',1,2,3,5,333))
Torsions.append(Torsion(15,'c-c3-c3-h1',1,2,3,4,333))
Torsions.append(Torsion(16,'c-c3-c3-c',1,2,3,6,333))
Torsions.append(Torsion(17,'hc-c3-c3-n3',11,2,3,5,333))
Torsions.append(Torsion(18,'hc-c3-c3-h1',11,2,3,4,333))
Torsions.append(Torsion(19,'hc-c3-c3-c',11,2,3,6,333))
Torsions.append(Torsion(20,'hc-c3-c3-n3',12,2,3,5,333))
Torsions.append(Torsion(21,'hc-c3-c3-h1',12,2,3,4,333))
Torsions.append(Torsion(22,'hc-c3-c3-c',12,2,3,6,333))
Torsions.append(Torsion(23,'hn-n3-c3-h1',13,5,3,4,333))
Torsions.append(Torsion(24,'hn-n3-c3-h1',14,5,3,4,333))
Torsions.append(Torsion(25,'hn-n3-c3-c',13,5,3,6,333))
Torsions.append(Torsion(26,'hn-n3-c3-c',14,5,3,6,333))
Torsions.append(Torsion(27,'n3-c3-c-o',5,3,6,8,333))
Torsions.append(Torsion(28,'n3-c3-c-oh',5,3,6,7,333))
Torsions.append(Torsion(29,'hn-n3-c3-c3',13,5,3,2,333))
Torsions.append(Torsion(30,'hn-n3-c3-c3',14,5,3,2,333))
Torsions.append(Torsion(31,'h1-c3-c-o',4,3,6,8,333))
Torsions.append(Torsion(32,'h1-c3-c-oh',4,3,6,7,333))
Torsions.append(Torsion(33,'o-c-c3-c3',8,6,3,2,333))
Torsions.append(Torsion(34,'oh-c-c3-c3',7,6,3,2,333))
Torsions.append(Torsion(35,'n3-c3-c-o',5,3,6,8,333))
Torsions.append(Torsion(36,'h1-c3-c-o',4,3,6,8,333))
Torsions.append(Torsion(37,'n3-c3-c-oh',5,3,6,7,333))
Torsions.append(Torsion(38,'h1-c3-c-oh',4,3,6,7,333))
Torsions.append(Torsion(39,'c3-c-oh-ho',3,6,7,15,333))
Torsions.append(Torsion(40,'o-c-oh-ho',8,6,7,15,333))
Torsions.append(Torsion(41,'c3-c-oh-ho',3,6,7,15,333))
Torsions.append(Torsion(42,'o-c-oh-ho',8,6,7,15,333))
inputdata = Sysdata(Atoms,Bonds,Angles,Torsions)
