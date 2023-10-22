from game import Agent
from game import Directions
from pacman import GameState
import random

class BasicAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    actions = state.getLegalPacmanActions()
    if Directions.NORTH in actions:
      return Directions.NORTH
    else:
      return Directions.STOP

class RandomAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    actions = state.getLegalPacmanActions()
    if len(actions)==1 and actions[0] == Directions.STOP:
      return Directions.STOP
    else:
      actions.remove(Directions.STOP)
      return random.choice(actions)
      

class SmartAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    pos_pacman = state.getPacmanPosition()
    actions = state.getLegalPacmanActions()
    ghostPosition = state.getGhostPositions()
    foods = state.getFood()
    capsuules = state.getCapsules()
    walls = state.getWalls()
    dir={}
    if len(actions)==1 and actions[0] == Directions.STOP:
      return Directions.STOP
    else:
      actions.remove(Directions.STOP)
      for action in actions:
        dir[action] = 0
      for action in actions:
        d=0
        if action == Directions.EAST:
          while walls[pos_pacman[0]+d][pos_pacman[1]] == False:
           d+=1
           if foods[pos_pacman[0]+d][pos_pacman[1]]==True or (pos_pacman[0]+d,pos_pacman[1]) in capsuules:
             dir[action]=d
             break
        elif action == Directions.WEST:
          while walls[pos_pacman[0]-d][pos_pacman[1]] == False:
           d+=1
           if foods[pos_pacman[0]-d][pos_pacman[1]]==True or (pos_pacman[0]-d,pos_pacman[1]) in capsuules:
             dir[action]=d
             break
        elif action == Directions.NORTH:
          while walls[pos_pacman[0]][pos_pacman[1]+d] == False:
           d+=1
           if foods[pos_pacman[0]][pos_pacman[1]+d]==True or (pos_pacman[0],pos_pacman[1]+d) in capsuules:
             dir[action]=d
             break
        elif action == Directions.SOUTH:
          while walls[pos_pacman[0]][pos_pacman[1]-d] == False:
           d+=1
           if foods[pos_pacman[0]][pos_pacman[1]-d]==True or (pos_pacman[0],pos_pacman[1]-d) in capsuules:
             dir[action]=d
             break   

      Min = 0
      result = random.choice(actions)
      random.shuffle(actions)
      for action in actions:
        if (dir[action] <= Min  and dir[action]!=0) or Min == 0:
          Min=dir[action]
          result = action
      return result

class ReflexAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    pos_pacman = state.getPacmanPosition()
    actions = state.getLegalPacmanActions()
    ghostPosition = state.getGhostPositions()
    foods = state.getFood()
    capsuules = state.getCapsules()
    walls = state.getWalls()
    Food_actions=[]
    if len(actions)==1 and actions[0] == Directions.STOP:
      return Directions.STOP
    else:
      actions.remove(Directions.STOP)
      for action in actions:
        if action == Directions.EAST:
           if foods[pos_pacman[0]+1][pos_pacman[1]]==True:
             Food_actions.append(action)
        elif action == Directions.WEST:
          if foods[pos_pacman[0]-1][pos_pacman[1]]==True:
             Food_actions.append(action)
        elif action == Directions.NORTH:
          if foods[pos_pacman[0]][pos_pacman[1]+1]==True:
             Food_actions.append(action)
        elif action == Directions.SOUTH:
          if foods[pos_pacman[0]+1][pos_pacman[1]-1]==True:
             Food_actions.append(action)
      if(len(Food_actions)==0):
        result = random.choice(actions)
      else:
        result = random.choice(Food_actions)          
      return result
        



   