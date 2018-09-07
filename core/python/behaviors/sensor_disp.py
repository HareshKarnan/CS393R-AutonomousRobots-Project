
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from task import Task
import core
import memory
import time
import cfgstiff
import commands
from math import pi

	

class Playing(Task):
	def run(self):
		commands.setStiffness(cfgstiff.Zero)
		print ("My battery value is :", core.sensor_values[core.battery])
		print ("My head yaw value is :", core.joint_values[core.HeadYaw])

