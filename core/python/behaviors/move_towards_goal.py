from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import memory
import core
import pose
import commands
import cfgstiff
from task import Task
from state_machine import Node, C, T, S, StateMachine, LoopingStateMachine

class Playing(LoopingStateMachine):    
    
    class Walk(Node):
        def run(self):
            goal = memory.world_objects.getObjPtr(core.WO_OWN_GOAL)
            commands.setWalkVelocity(0.5, 0, goal.visionBearing)

   class Off(Node):
        def run(self):
            commands.setStiffness(cfgstiff.Zero)
            if self.getTime() > 2.0:
                memory.speech.say("turned off stiffness")
                self.finish()
    def setup(self):
        walk = self.Walk()        
        goal = memory.world_objects.getObjPtr(core.WO_OWN_GOAL)
        if goal.seen:
            print("goal seen")
            dist = goal.visionDistance
            while(dist > 5):
                print("visionDistance: ",dist)
                self.trans(walk,C)
                dist-=10;
        
        
    