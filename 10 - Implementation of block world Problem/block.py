class PREDICATE: 
def str (self): 
 pass 
def repr (self): 
 pass 
def eq (self, other) : 
 pass 
def hash (self): 
 pass 
def get_action(self, world_state): 
 pass 
class Operation: def 
str (self): 
 pass 
def repr (self):
 pass 
def eq (self, other) : 
 pass 
def precondition(self): 
 pass 
def delete(self): 
 pass 
def add(self): 
 pass 
class ON(PREDICATE): 
def init (self, X, Y): 
 self.X = X 
 self.Y = Y 
def str (self): 
 return "ON({X},{Y})".format(X=self.X,Y=self.Y) 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def hash (self): 
return hash(str(self)) 
def get_action(self, world_state): 
 return StackOp(self.X,self.Y)
class ONTABLE(PREDICATE): 
def init (self, X): 
 self.X = X 
def str (self): 
 return "ONTABLE({X})".format(X=self.X) 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def hash (self): 
return hash(str(self)) 
def get_action(self, world_state): 
 return PutdownOp(self.X) 
class CLEAR(PREDICATE): 
def init (self, X): 
 self.X = X 
def str (self): 
 return "CLEAR({X})".format(X=self.X) 
 self.X = X 
def repr (self): 
 return self. str () def eq 
(self, other) :
 return self. dict == other. dict and self. class == other. class def hash (self): 
 return hash(str(self)) 
def get_action(self, world_state): 
 for predicate in world_state: 
if isinstance(predicate,ON) and predicate.Y==self.X: 
return UnstackOp(predicate.X, predicate.Y) 
 return None 
class HOLDING(PREDICATE): 
def init (self, X): 
 self.X = X 
def str (self): 
 return "HOLDING({X})".format(X=self.X) 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def hash (self): 
 return hash(str(self)) 
def get_action(self, world_state): 
 X = self.X 
 if ONTABLE(X) in world_state: 
return PickupOp(X)
 else: 
for predicate in world_state: 
if isinstance(predicate,ON) and predicate.X==X: 
return UnstackOp(X,predicate.Y) 
class ARMEMPTY(PREDICATE): 
def init (self): 
 pass 
def str (self): 
 return "ARMEMPTY" 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def hash (self): 
 return hash(str(self)) 
def get_action(self, world_state=[]): 
 for predicate in world_state: 
if isinstance(predicate,HOLDING): 
return PutdownOp(predicate.X) 
 return None 
class StackOp(Operation):def 
init (self, X, Y):
 self.X = X 
 self.Y = Y 
def str (self): 
 return "STACK({X},{Y})".format(X=self.X,Y=self.Y) 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def precondition(self): 
 return [ CLEAR(self.Y) , HOLDING(self.X) ] 
def delete(self): 
 return [ CLEAR(self.Y) , HOLDING(self.X) ] 
def add(self): 
 return [ ARMEMPTY() , ON(self.X,self.Y) ] 
class UnstackOp(Operation): 
def init (self, X, Y): 
 self.X = X 
 self.Y = Y 
def str (self): 
 return "UNSTACK({X},{Y})".format(X=self.X,Y=self.Y) 
def repr (self): 
 return self. str () def eq 
(self, other) :
 return self. dict == other. dict and self. class == other. class def precondition(self): 
 return [ ARMEMPTY() , ON(self.X,self.Y) , CLEAR(self.X) ]def  delete(self): 
 return [ ARMEMPTY() , ON(self.X,self.Y) ]def  
add(self): 
 return [ CLEAR(self.Y) , HOLDING(self.X) ] 
class PickupOp(Operation): 
def init (self, X): 
 self.X = X 
def str (self): 
 return "PICKUP({X})".format(X=self.X) 
def repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def precondition(self): 
 return [ CLEAR(self.X) , ONTABLE(self.X) , ARMEMPTY() ]def  delete(self): 
 return [ ARMEMPTY() , ONTABLE(self.X) ] 
def add(self): 
 return [ HOLDING(self.X) ]
class PutdownOp(Operation): 
def init (self, X): 
 self.X = X 
def str (self): 
 return "PUTDOWN({X})".format(X=self.X)def 
repr (self): 
 return self. str () def eq 
(self, other) : 
 return self. dict == other. dict and self. class == other. class def precondition(self): 
 return [ HOLDING(self.X) ] 
def delete(self): 
 return [ HOLDING(self.X) ] 
def add(self): 
 return [ ARMEMPTY() , ONTABLE(self.X) ] 
def isPredicate(obj): 
predicates = [ON, ONTABLE, CLEAR, HOLDING, ARMEMPTY] for predicate in predicates: 
 if isinstance(obj,predicate): 
return True 
return False
def isOperation(obj): 
operations = [StackOp, UnstackOp, PickupOp, PutdownOp]for operation in operations: 
 if isinstance(obj,operation): 
return True 
return False 
def arm_status(world_state):for 
predicate in world_state: 
 if isinstance(predicate, HOLDING): 
return predicate 
return ARMEMPTY() 
class GoalStackPlanner: 
def init (self, initial_state, goal_state): 
 self.initial_state = initial_state 
 self.goal_state = goal_state 
def get_steps(self): 
 steps = [] 
 stack = []
 #World State/Knowledge Base 
 world_state = self.initial_state.copy() 
 #Initially push the goal_state as compound goal onto the stack  stack.append(self.goal_state.copy()) 
 #Repeat until the stack is empty 
 while len(stack)!=0: 
#Get the top of the stack 
stack_top = stack[-1] 
#If Stack Top is Compound Goal, push its unsatisfied goals onto stack if type(stack_top) is list: 
compound_goal = stack.pop() 
for goal in compound_goal: 
if goal not in world_state: 
stack.append(goal) 
elif isOperation(stack_top): 
operation = stack[-1] 
all_preconditions_satisfied = True 
for predicate in operation.delete(): 
if predicate not in world_state:
all_preconditions_satisfied = False 
stack.append(predicate) 
if all_preconditions_satisfied: 
stack.pop() 
steps.append(operation) 
for predicate in operation.delete(): 
world_state.remove(predicate) 
for predicate in operation.add(): 
world_state.append(predicate) 
elif stack_top in world_state: 
stack.pop() 
else: 
unsatisfied_goal = stack.pop() 
action = unsatisfied_goal.get_action(world_state) 
stack.append(action) 
for predicate in action.precondition(): 
if predicate not in world_state: 
stack.append(predicate)
 return steps 
if name == ' main ': 
initial_state = [ 
 ON('B','A'),ON('E', 'B'), 
 ONTABLE('A'),ONTABLE('C'),ONTABLE('D'), 
 CLEAR('B'),CLEAR('C'),CLEAR('D'),CLEAR('E'), 
 ARMEMPTY() 
] 
goal_state = [ 
 ON('B','D'),ON('D','C'), ON('C', 'A'),ON('A', 'E'), 
 ONTABLE('A'), 
 CLEAR('B'),CLEAR('C'), CLEAR('D'),CLEAR('E'), 
 ARMEMPTY() 
] 
goal_stack = GoalStackPlanner(initial_state=initial_state, goal_state=goal_state)steps = goal_stack.get_steps() 
print("UNSTACK(E,B)") 
print("PUTDOWN(E)") 
for i in steps: 
 print(i) 
