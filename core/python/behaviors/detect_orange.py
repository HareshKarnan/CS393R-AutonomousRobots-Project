"""Blank behavior."""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from task import Task
import core
import memory

class Playing(Task):	
    """Main behavior task."""
    def run(self):
    	ball = memory.world_objects.getObjPtr(core.WO_BALL)
	#print (memory.world_objects.getObjPtr(core.WO_BALL))
	print ("image X:", ball.imageCenterX)
	print ("image Y:", ball.imageCenterY)
	if ball.seen:
		print ("ball seen")
    	self.finish()

    pass
