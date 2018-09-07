from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import memory
import pose
import commands
import cfgstiff
from task import Task
from state_machine import Node, C, T, S, StateMachine

class Playing(StateMachine):
    class Stand(Node):
        def run(self):
            commands.stand()
            if self.getTime() > 5.0:
                memory.speech.say("playing stand complete")
                self.finish()

    class Turn_Head(Node):
    	def run(self):
    		commands.setHeadPanTilt(2,20)
    		self.postSignal("done")

    class Walk(Node):
        def run(self):
            commands.setWalkVelocity(0.5, 0, 0)
    
    class Walk_Turn(Node):
        def run(self):
            commands.setWalkVelocity(0.5, 0, 0.5)

    class Turn_In_Place(Node):
    	def run(self):
            commands.setWalkVelocity(0, 0, 0.5)
            self.finish()

    class Off(Node):
        def run(self):
            commands.setStiffness(cfgstiff.Zero)
            if self.getTime() > 2.0:
                memory.speech.say("turned off stiffness")
                self.finish()

    def setup(self):
        stand = self.Stand()
        turn_head = self.Turn_Head()
        walk = self.Walk()
        walk_turn = self.Walk_Turn();
        turn_in_place = self.Turn_In_Place();
        sit = pose.Sit()
        off = self.Off()
        self.trans(stand, C, turn_head, S("done"), sit, C, walk, T(5.0), turn_in_place, T(3.0), walk_turn, T(5.0), off)