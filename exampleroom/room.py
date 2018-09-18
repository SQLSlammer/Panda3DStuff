#=============================================================#
# Example Room v 1.0                                          #
# Code by Sir McQuack (yoshi295295/outrunning)                #
# Thank you to:                                               #
# QED1224 and Cell1234 for toontown.py and making life easier #
# Laosinaa for giving me a starting point in Panda3D          #
# Disney for creating the Panda3D engine                      #
# This code will be occasionally updated and probably even    #
# used for a animation or something                           #
#=============================================================#

from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *

from panda3d.ai import *
import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import toontown

#--------------------------
# The Room (2003)
terrain = loader.loadModel('room.bam')
terrain.reparentTo(render)
#--------------------------

#--------------------------
# The toons/cogs

# ---toon---
toon = toontown.Toon('Horse', 'm', 'n', 'n', 'm', 'm')
toon.set_color('Red')
toon.set_shirt('phase_3/maps/desat_shirt_9.jpg', 'phase_3/maps/desat_sleeve_9.jpg')
toon.set_bottom('phase_3/maps/desat_shorts_6.jpg')
toon.loop('neutral')
toon.setPos(0, -10, 0)
toon.setH(0)

# ---cog---
cog = toontown.load_cog('Mr. Hollywood')
cog.loop('neutral')
cog.setPos(0, 10, 0)
cog.setH(-180)

# ---sitting cog #1---
sit = toontown.load_cog('Big Wig')
sit.loop('sit')
sit.setPos(-20.5, 4, 0)
sit.setH(270)

# ---sitting cog #2---
sit2 = toontown.load_cog('Corporate Raider')
sit2.loop('sit')
sit2.setPos(-18, 9, -0.85)
sit2.setH(270)

# ---skelecog bodyguard #1---
skele = toontown.load_cog('Robber Baron', skelecog=True)
skele.loop('neutral')
skele.setPos(-70, -10, 0)
skele.setH(270)

# ---skelecog bodyguard #2---
skele2 = toontown.load_cog('Robber Baron', skelecog=True)
skele2.loop('neutral')
skele2.setPos(-70, 10, 0)
skele2.setH(270)

# ---piano player---
ms = toontown.load_cog('Mover & Shaker')
ms.loop('magic1')
ms.setPos(56, -4, 0)
ms.setH(270)

# ---dancing cog---
dc = toontown.load_cog('Robber Baron')
dc.loop('victory')
dc.setPos(50, 2, 0)
dc.setH(180)

# ---balcony cog #1---
bc1 = toontown.load_cog('Name Dropper')
bc1.loop('fingerwag')
bc1.setPos(-8, 29, 8.7)
bc1.setH(-270)

# ---balcony cog #2---
bc2 = toontown.load_cog('The Mingler')
bc2.loop('rubber-stamp')
bc2.setPos(-16, 29, 8.7)
bc2.setH(270)
#--------------------------

#--------------------------
# The objects

# ---fountain---
ftain = loader.loadModel('phase_4/models/props/toontown_central_fountain.bam')
ftain.reparentTo(render)
ftain.setPos(-8, -50, 0)

# ---piano---
piano = loader.loadModel('phase_5.5/models/estate/Piano.bam')
piano.reparentTo(render)
piano.setPos(59, -4, 3.7)
piano.setH(270)
piano.setScale(2)

# ---table---
table = loader.loadModel('phase_12/models/bossbotHQ/BanquetTableChairs.bam')
table.reparentTo(render)
table.setPos(-14, 7, 0)
#--------------------------

base.run()
