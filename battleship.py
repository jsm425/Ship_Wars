import Tkinter as tk

#####
dim = 10


#####
class Application:
  def __init__(self,master):
    VA = Values()
  
    frame1 = tk.Frame()
    frame1.pack(side = 'left')
    
    frame2 = tk.Frame()
    frame2.pack(side = 'right')
    
    OG = OwnGrid()

    BO = Board(OG,frame1,VA)
    HA = Harbor(OG,frame2,VA)
    #BR = Bridge(OG,frame2,VA)
    
    
###
class Board:
  def __init__(self,OG,frame,values):
    self.button_grid = {}
    self.hits = 0
    
    for x in range(dim):
      for y in range(dim):
        block = tk.Button(frame, height = 2, width = 5,
          bg = 'lightblue', activebackground = 'blue')
        block['command'] = lambda id = block : self.activate(id,OG,values)
        self.button_grid[block] = (x,y)
        block.grid(column = x, row = y,sticky = 'nsew') 
        
        
  def activate(self,id,OG,values):
    stage = values.getStage()
    
    if (stage == 0):
      self.deploy(id,OG,values)
      
    elif (stage == 1):
      self.fire(id,OG,values)
    
        
  def deploy(self,id,OG,values):
    AS = values.getActiveShip()
    AD = values.getActiveDir()
    XY = self.button_grid[id]
    
    x = XY[0]
    y = XY[1]
    
    if (AD == 'right'):
      for i in range(0,AS):
        OG.setOwn(1,x + i,y)
      print 'r'
      
    elif (AD == 'down'):
      for i in range(0,AS):
        OG.setOwn(1,x,y + i)
      print 'd'
  
  
  def fire(self,id,OG,values):
    if id['bg'] == 'lightblue':
      x = self.button_grid[id][0]
      y = self.button_grid[id][1]
      
      grid_value = OG.getOwn(x,y)

      if (grid_value == 0):
        id['bg'] = 'white'
        id['activebackground'] = 'grey'
      elif (grid_value == 1):
        id['bg'] = 'maroon'
        id['activebackground'] = 'grey'
        
        self.hits += 1
      else: id['bg'] = 'black'
      
    else: pass
    
    self.checkWin(OG,values)
        
        
  def checkWin(self,OG,values):
    fleet = OG.getFleet()
    if self.hits == fleet:
      print 'GAME OVER'
      print self.hits, fleet
    
    
###
class Harbor:
  def __init__(self,OG,frame,values):  
    self.active_ship = values.getActiveShip()
    self.active_dir = values.getActiveDir()
  
    ship2 = tk.Button(frame, height = 2, width = 16, bg = 'darkgrey',
      command = lambda:self.engage(2,values),activebackground = 'black')
    ship3 = tk.Button(frame, height = 2, width = 24, bg = 'darkgrey',
      command = lambda:self.engage(3,values),activebackground = 'black')
    ship4 = tk.Button(frame, height = 2, width = 32, bg = 'darkgrey',
      command = lambda:self.engage(4,values),activebackground = 'black')
    ship5 = tk.Button(frame, height = 2, width = 40, bg = 'darkgrey',
      command = lambda:self.engage(5,values),activebackground = 'black')
      
    ship2.grid(sticky = 'w')
    ship3.grid(sticky = 'w')
    ship4.grid(sticky = 'w')
    ship5.grid(sticky = 'w')
    
    ready = tk.Button(frame, height = 3, width = 40, bg = 'tan', text = 'READY')
    ready['command'] = lambda: values.upStage() & ready.destroy()
    ready.grid()
        
        
  def engage(self,x,values):
    if (values.getActiveShip() == x):
      if (values.getActiveDir() == 'right'): values.setActiveDir('down')
      elif (values.getActiveDir() == 'down'): values.setActiveDir('right')
    
    values.setActiveShip(x)
    
        
###
class Bridge:
  def __init__(self,OG,frame):
    pass
      
      
#####
class OwnGrid:
  def __init__(self):
    self._ownGrid = [[0] * dim for i in range(dim)]
      
  def getOwn(self,x,y):
    return self._ownGrid[x][y]
    
  def setOwn(self, value, x, y):
    self._ownGrid[x][y] = value
    
  def getFleet(self):
    self._fleet = 0
    for each in self._ownGrid:
      self._fleet += each.count(1)
    return self._fleet

    
###
class Values:
  def __init__(self):
    self._stage = 0
    self._activeShip = -1
    self._activeDir = 'right'
    
  def getStage(self):
    return self._stage
    
  def upStage(self):
    self._stage = self._stage + 1
    print 'up'
  
  def getActiveDir(self):
    return self._activeDir
    
  def setActiveDir(self,dir):
    self._activeDir = dir
    
  def getActiveShip(self):
    return self._activeShip
    
  def setActiveShip(self,x):
    self._activeShip = x

        
#####
root = tk.Tk()

sea_frame = Application(root)

root.mainloop()    
