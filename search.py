# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    
    start = problem.getStartState()
    c = problem.getStartState()
    exploredState = []
    exploredState.append(start)
    states = util.Stack()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty() and not problem.isGoalState(c):
        state, actions = states.pop()
        exploredState.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                c = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    c = problem.getStartState()
    exploredState = []
    exploredState.append(start)
    states = util.Queue()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty() and not problem.isGoalState(c):
        state, actions = states.pop()
        exploredState.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                c = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]
    util.raiseNotDefined()
    util.raiseNotDefined()
    
def breadthFirstSearch1(problem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    exploredState = set()  # Use a set to keep track of visited states
    exploredState.add(start)
    states = util.Stack()  # Use a stack for depth-first search
    stateTuple = (start, [])
    states.push(stateTuple)
    
    while not states.isEmpty():
        state, actions = states.pop()
        
        if problem.isGoalState(state):
            return actions  # If all dots are eaten, return the actions
            
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if coordinates not in exploredState:
                direction = i[1]
                exploredState.add(coordinates)
                states.push((coordinates, actions + [direction]))
    
    return []  
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    start = problem.getStartState()
    exploredState = []
    states = util.PriorityQueue()
    states.push((start, []), nullHeuristic(start, problem))
    nCost = 0
    while not states.isEmpty():
        state, actions = states.pop()
        if problem.isGoalState(state):
            return actions
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0]
                if coordinates not in exploredState:
                    directions = succ[1]
                    nActions = actions + [directions]
                    nCost = problem.getCostOfActions(nActions) + heuristic(coordinates, problem)
                    states.push((coordinates, actions + [directions]), nCost)
        exploredState.append(state)
    return actions
    util.raiseNotDefined()
    
def customHeuristic(coordinates, target, problem):
    count = 0
    count1 = 0
    x,y = coordinates
    while x < target[0]:
        x += 1
        if problem.getWalls()[x][y]:
            count += 1
    
    while x >= target[0]:
        x -= 1
        if problem.getWalls()[x][y]:
            count += 1
    
    while y < target[1]:
        y += 1
        if problem.getWalls()[x][y]:
            count += 1
    while y > target[1]:
        y -= 1
        if problem.getWalls()[x][y]:
            count += 1
    x,y = coordinates
    while y < target[1]:
        y += 1
        if problem.getWalls()[x][y]:
            count1 += 1
    while y > target[1]:
        y -= 1
        if problem.getWalls()[x][y]:
            count1 += 1
      
    while x < target[0]:
        x += 1
        if problem.getWalls()[x][y]:
            count1 += 1
    
    while x >= target[0]:
        x -= 1
        if problem.getWalls()[x][y]:
            count1 += 1
    
    return min(count, count1)

def visitedAlready(coordinates, grid, visited):
    	for v in visited:
    	    if coordinates == v[0] and grid == v[1]:
    	        return 0
        return 1

def getNewGoal(position, foods, problem):
    goals = util.PriorityQueue()
    for f in foods:
        goals.push(f, customHeuristic(position, f, problem))
    toReturn = goals.pop()
    foods.remove(toReturn)
    problem.removeFood(foods)
    return toReturn
    
def partitionFood(start, foods, problem):
    list1 = []
    list2 = []
    aux1 = getNewGoal(start, foods, problem)
    aux2 = getNewGoal(start, foods, problem)
    list1.append(aux1)
    list2.append(aux2)
    print aux1, aux2
    
    while not problem.noMoreFood():
        aux1 = getNewGoal(aux1, foods, problem)
        aux2 = getNewGoal(aux2, foods, problem)
        list1.append(aux1)
        list2.append(aux2)
        print aux1, aux2
   
    return (list1, list2)
        

def firstPacman(problem, heuristic=customHeuristic):
    start = problem.getStartState()
    visited = []
    states = util.PriorityQueue()
    states.push((start, []), nullHeuristic(start))
    goal = problem.getGoal()
    #print problem.getTargets()
    list1, list2 = partitionFood(goal, problem.getTargets(), problem)
    problem.setTargets(list1)
    #print problem.getTargets()
    
    while not states.isEmpty():
        state, actions = states.pop()
        if state not in visited:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0][0]
            	if visitedAlready(coordinates, succ[0][1], visited):
            	    direction = succ[1]
            	    acc = actions + [direction]
            	    cost = problem.getCostOfActions(acc) + customHeuristic(coordinates, goal, problem)
            	    states.push((succ[0], acc), cost)
        visited.append(state)
        if problem.isIntermediateGoalState(state):
            if problem.noMoreFood():
                return actions
            else:
                if problem.broFound():
                    problem.setBrother(len(actions))
                newGoal = getNewGoal(state[0], problem.getTargets(), problem)
                problem.changeGoal(newGoal)
                while not states.isEmpty():
                    states.pop()
                visited = []
                states.push((state, actions), 0)
    return []


def secondPacman(problem, heuristic=customHeuristic):
    start = problem.getStartState()
    visited = []
    states = util.PriorityQueue()
    lista = []
    for x in range(24):
        lista.append('Stop')
    print lista
    states.push((start, lista), nullHeuristic(start))
    goal = problem.getGoal()
    #print problem.getTargets()
    list1, list2 = partitionFood(start[0], problem.getTargets(), problem)
    problem.setTargets(list2)
    #print problem.getTargets()
    
    while not states.isEmpty():
        state, actions = states.pop()
        if state not in visited:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0][0]
            	if visitedAlready(coordinates, succ[0][1], visited):
            	    direction = succ[1]
            	    acc = actions + [direction]
            	    cost = problem.getCostOfActions(acc) + customHeuristic(coordinates, goal, problem)
            	    states.push((succ[0], acc), cost)
        visited.append(state)
        if problem.isIntermediateGoalState(state):
            if problem.noMoreFood():
                return actions
            else:
                newGoal = getNewGoal(state[0], problem.getTargets(), problem)
                problem.changeGoal(newGoal)
                while not states.isEmpty():
                    states.pop()
                visited = []
                states.push((state, actions), 0)
    return []
    

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bfs1 = breadthFirstSearch1
pac = firstPacman
man = secondPacman

