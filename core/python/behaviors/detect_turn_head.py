from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import memory
import core
import pose
import commands
import cfgstiff
from task import Task
from state_machine import Node, C, T, S, StateMachine ,LoopingStateMachine

class Playing(LoopingStateMachine):    

    class Turn_Head(Node):
        def run(self):
            ball = memory.world_objects.getObjPtr(core.WO_BALL)
            commands.setHeadPanTilt(ball.visionBearing,ball.visionElevation)
            # self.postSignal("done") 
    class Stand(Node):
        def run(self):
            commands.stand()
            if self.getTime() > 5.0:
                memory.speech.say("playing stand complete")
                self.finish()

    class Off(Node):
        def run(self):
            commands.setStiffness(cfgstiff.Zero)
            if self.getTime() > 2.0:
                memory.speech.say("turned off stiffness")
                self.finish()
    def run(self):
        turn_head = self.Turn_Head()        
        ball = memory.world_objects.getObjPtr(core.WO_BALL)
        off = self.Off()
        stand = self.Stand()
        print("Ball seen: ",ball.seen)

        if ball.seen:
            print("Inside first loop\n")
            print(ball.visionBearing,ball.visionElevation,ball.imageCenterX,ball.imageCenterY)
            if ball.imageCenterX!=0:
                print("ball seen in PYTHON")
                turn_head = self.Turn_Head()
                commands.setHeadPanTilt(ball.visionBearing,ball.visionElevation*10)
                # commands.setHeadPanTilt(-1,20)
                print("Set")
                # self.trans(stand,C,turn_head, S("done"))
                #robot = memory.world_objects.getObjPtr(cache_.robot_state.WO_SELF);
                #print ("robot location: ",robot.loc)
                #print ("robot orientation: ",robot.orientation)
                #print("elevation:",ball.visionElevation, " bearing:",ball.visionBearing)
        
        
    