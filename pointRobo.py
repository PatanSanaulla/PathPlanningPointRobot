import matplotlib.pyplot as mplot
import sys


MAX_X = 5
MAX_Y = 5

START_POINT = [] # [x, y]
GOAL_POINT = [] # [x, y]

STEPS_LIST = []
STEP_OBJECT_LIST = []
class step:
	#Method to initialize the node with the values/attributes and add the Node
	#self: Object of class Node
	#parent: Object of class Node
	#Cube: the cube formation for the Node 
	def __init__(self, parent, position, cost):
		self.position = position # [x, y]
		self.parent = parent
		if parent == None:
			self.costToCome = 0.0
		else:
			self.costToCome = parent.costToCome + cost;
		self.addToGraph()


	def addToGraph(self):
		if self.position in STEPS_LIST:
			index = STEPS_LIST.index(self.position)
			if self.costToCome < STEP_OBJECT_LIST[index].costToCome:
				STEP_OBJECT_LIST[index] = self
		else:
			STEPS_LIST.append(self.position)
			STEP_OBJECT_LIST.append(self)

	def moveUp(self):
		if(self.position[1] > 0):
			newStep = step(self, [self.position[0], self.position[1]-1], 1.0)
			#possible Move
		else:
			return 

	def moveUpRight(self):
		if(self.position[1] > 0 & self.position[0] < MAX_X):
			newStep = step(self, [self.position[0]+1, self.position[1]-1], 1.414)
			#possible Move
		else:
			return 
	
	def moveRight(self):
		if(self.position[0] < MAX_X):
			newStep = step(self, [self.position[0]+1, self.position[1]], 1)
			#possible Move
		else:
			return 

	def moveDownRight(self):
		if(self.position[1] < MAX_Y & self.position[0] < MAX_X):
			newStep = step(self, [self.position[0]+1, self.position[1]+1], 1.414)
			#possible Move
		else:
			return
	
	def moveDown(self):
		if(self.position[1] < MAX_Y):
			newStep = step(self, [self.position[0], self.position[1]+1], 1)
			#possible Move
		else:
			return

	def moveDownLeft(self):
		if(self.position[1] < MAX_Y & self.position[0] > 0):
			newStep = step(self, [self.position[0]-1, self.position[1]+1], 1.414)
			#possible Move
		else:
			return

	def moveLeft(self):
		if(self.position[0] > 0):
			newStep = step(self, [self.position[0]-1, self.position[1]], 1)
			#possible Move
		else:
			return

	def moveUpLeft(self):
		if(self.position[1] > 0 & self.position[0] > 0):
			newStep = step(self, [self.position[0]-1, self.position[1]-1], 1.414)
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
	mplot.xlabel('graphical representation')
	mplot.show()

startPoints = input("Enter the Start Points (x,y) position:")
START_POINT = [int(each) for each in startPoints] 
goalPoints = input("Enter the Goal Points (x,y) position:")
GOAL_POINT = [int(each) for each in goalPoints]

root = step(None, START_POINT, 0)

for eachStep in STEP_OBJECT_LIST:

	if eachStep.position == GOAL_POINT:
		print("reached the required goal")
		#backtrack(eachStep)
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








