import matplotlib.pyplot as mplot
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
#import numpy as np


MAX_X = 300
MAX_Y = 200

START_POINT = [] # [x, y]
GOAL_POINT = [] # [x, y]

STEPS_LIST = []
STEP_OBJECT_LIST = []


#style.use('fivethirtyeight')

#fig = mplot.figure()
#ax1 = fig.add_subplot(1,1,1)

class step:
	#Method to initialize the node with the values/attributes and add the step
	#self: Object of class step
	#parent: Object of class step
	#position: the x,y values of the current step
	#cost: cost of the step to move from the parent to the current position 
	def __init__(self, parent, position, cost):
		self.position = position # [x, y]
		self.parent = parent
		self.children = []
		if parent == None:
			self.costToCome = 0.0
		else:
			self.costToCome = parent.costToCome + cost;
		self.addToGraph()


	def addToGraph(self):
		if self.position in STEPS_LIST:
			#print("----------")
			index = STEPS_LIST.index(self.position)
			if self.costToCome < STEP_OBJECT_LIST[index].costToCome:
				#print("----------",STEP_OBJECT_LIST[index].children)
				STEP_OBJECT_LIST[index] = self
		else:
			STEPS_LIST.append(self.position)
			STEP_OBJECT_LIST.append(self)

	def moveUp(self):
		if(self.position[1] > 0):
			newPosition = [self.position[0], self.position[1]-1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.0)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.0)
				self.children.append(newStep)
				#possible Move
		else:
			return 

	def moveUpRight(self):
		if(self.position[1] > 0 and self.position[0] < MAX_X):
			newPosition = [self.position[0]+1, self.position[1]-1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.414)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.414)
				self.children.append(newStep)
				#possible Move
		else:
			return 

	def moveRight(self):
		if(self.position[0] < MAX_X):
			newPosition = [self.position[0]+1, self.position[1]]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.0)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.0)
				self.children.append(newStep)
				#possible Move
		else:
			return 

	def moveDownRight(self):
		if(self.position[1] < MAX_Y and self.position[0] < MAX_X):
			newPosition = [self.position[0]+1, self.position[1]+1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.414)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.414)
				self.children.append(newStep)
				#possible Move
		else:
			return
	
	def moveDown(self):
		if(self.position[1] < MAX_Y):
			newPosition = [self.position[0], self.position[1]+1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.0)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.0)
				self.children.append(newStep)
				#possible Move
		else:
			return

	def moveDownLeft(self):
		if(self.position[1] < MAX_Y and self.position[0] > 0):
			newPosition = [self.position[0]-1, self.position[1]+1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.414)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.414)
				self.children.append(newStep)
				#possible Move
		else:
			return

	def moveLeft(self):
		if(self.position[0] > 0):
			newPosition = [self.position[0]-1, self.position[1]]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.0)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.0)
				self.children.append(newStep)
				#possible Move
		else:
			return

	def moveUpLeft(self):
		if(self.position[1] > 0 and self.position[0] > 0):
			newPosition = [self.position[0]-1, self.position[1]-1]
			try:
				if(self.parent.position == newPosition):
					pass #going back to the parent
				else:
					newStep = step(self,newPosition, 1.414)
					self.children.append(newStep)
			except AttributeError:
				newStep = step(self,newPosition, 1.414)
				self.children.append(newStep)
				#possible Move
		else:
			return

def backtrack(stepObj):
	xValues = []
	yValues = []
	while stepObj.parent != None:
		print(stepObj.position)
		xValues.append(stepObj.position[0])
		yValues.append(stepObj.position[1])
		stepObj = stepObj.parent
	xValues.append(stepObj.position[0])
	yValues.append(stepObj.position[1])

	xValues.reverse()
	yValues.reverse()

	mplot.plot(xValues, yValues)
	mplot.axis([0, MAX_X, 0, MAX_Y])
	mplot.xlabel('graphical representation')
	mplot.show()

#def animate(i):
#	xs = []
#	ys = []
#	for step in STEPS_LIST:
#		xs.append(step[0])
#		ys.append(step[1])
#	ax1.clear()
#	ax1.axis([0, MAX_X, 0, MAX_Y])
#	ax1.plot(xs, ys, 'r')


startPoints = input("Enter the Start Points (x,y) position:")
START_POINT = [int(each) for each in startPoints.split(" ")] 
goalPoints = input("Enter the Goal Points (x,y) position:")
GOAL_POINT = [int(each) for each in goalPoints.split(" ")]

now = datetime.now().time()
print("start time: ",now)
root = step(None, START_POINT, 0)
#ani = animation.FuncAnimation(fig, animate, interval=1000)
#mplot.show()

for eachStep in STEP_OBJECT_LIST:

	if eachStep.position == GOAL_POINT:
		print("reached the required goal")
		now = datetime.now().time()
		print("found at time: ",now)
		break
	else:
		eachStep.moveLeft()
		eachStep.moveDown()
		eachStep.moveRight()
		eachStep.moveUp()
		eachStep.moveUpLeft()
		eachStep.moveDownLeft()
		eachStep.moveDownRight()
		eachStep.moveUpRight()

#print(*STEPS_LIST, sep ="\n")
index = STEPS_LIST.index(GOAL_POINT)
print("index",index)
print("cost to come:",STEP_OBJECT_LIST[index].costToCome)
backtrack(STEP_OBJECT_LIST[index])
now = datetime.now().time()
print("end time: ",now)



#print(STEPS_LIST)




