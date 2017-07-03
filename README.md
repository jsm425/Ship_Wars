# Ship_Wars

Functionality right now:

Creates Tkinter window with two frames:
   - frame1 = Board:
      * creates grid of dimensions (dim x dim) where each box in grid is a button 'block' with command 'activate'
   - frame 2 = Harbor:
      * creates menu of buttons for ships of length 2-5, and button 'ready'
    
Commands:
   - Button 'ready' calls function 'stageUp' which increments stage by one (starting stage = 0); button 'ready' destroys self on click
   - Buttons 'block' in grid calls function 'activate', which calls function 'deploy' if stage == 0 and calls function 'fire' if stage == 1
  
   - function 'deploy' uses variables 'activeShip' and 'activeDir' to determine the ship length and direction to place when deploying ships; converts values for appropriate placement in grid 'ownGrid' from 0  to 1
        * ship buttons in harbor set 'activeShip'; click button twice in a row to toggle placement variable 'activeDir' between 'right' and 'down' from 'block' selected
   - function 'fire': if 'block' background == 'lightblue' (ie 'block' is previously unclicked) then gets value of corresponding grid unit from 'ownGrid' - if value == 0 then 'block' background = 'white' (ie miss), and if value == 1 then 'block' background == 'maroon' (ie hit)
       * function 'fire' also calls function 'checkWin': if upon click, number of maroon tiles == number of 1's in ownGrid (ie hits == ships deployed) then prints "GAME OVER"
