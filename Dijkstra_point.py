from Create_puzzle import *
from datetime import datetime


#Global Variables
START_POINT = [] # [x, y]
GOAL_POINT = [] # [x, y]
STEPS_LIST = []
STEP_OBJECT_LIST = []

    
#Definition of Class Step:
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
		global obstacleScreen
		if self.position in STEPS_LIST:
			index = STEPS_LIST.index(self.position)
			if self.costToCome < STEP_OBJECT_LIST[index].costToCome:
				STEP_OBJECT_LIST[index] = self
		else:
			updateTheStep(self.position, startColor)
			STEPS_LIST.append(self.position)
			STEP_OBJECT_LIST.append(self)

	def moveUp(self):
		if(self.position[1] > 0):
			newPosition = [self.position[0], self.position[1]-1]
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
			if isValidStep(newPosition) == True:
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
	pathValues = []
	while stepObj.parent != None:
		print(stepObj.position)
		pathValues.append(stepObj.position)
		stepObj = stepObj.parent
	pathValues.append(stepObj.position)
    
	pathValues.reverse()
	showPath(pathValues) 

#MAIN CODE
startPoints = input("Enter the Start Points (x,y) position:")
START_POINT = [int(each) for each in startPoints.split(" ")] 
goalPoints = input("Enter the Goal Points (x,y) position:")
GOAL_POINT = [int(each) for each in goalPoints.split(" ")]

#To switch the orgin to the top
START_POINT[1] = MAX_Y - START_POINT[1]
GOAL_POINT[1] = MAX_Y - GOAL_POINT[1]

updateTheStep(START_POINT, startColor)
updateTheStep(GOAL_POINT, goalColor)

#obstacleScreen = createScreen()

now = datetime.now().time()
print("start time: ",now)

root = step(None, START_POINT, 0)

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

index = STEPS_LIST.index(GOAL_POINT)
#print("index",index)
print("cost to come:",STEP_OBJECT_LIST[index].costToCome)
backtrack(STEP_OBJECT_LIST[index])
now = datetime.now().time()
print("end time: ",now)

while True:
	for inst in pygame.event.get():
		if inst.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()