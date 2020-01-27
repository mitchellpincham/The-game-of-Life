# The-game-of-Life
A game made in Python 3.8 and Pygame

Go to rand.py for a random board

editor.py is where you can make your own board -
  just click the boxes you want and press enter
  
the rules of the game of life:
  each square has 2 possible states alive or dead
  
  neibours are the 8 surrounding squares
  
  if an alive square has less than 2 neibours then it dies from underpopulation
  if an alive square has more than 3 neibours then it dies from overpopulation
  otherwise it survives
  
  if a dead quare has exactly 3 alive squares around it then it turns into an alive square.
  

you can read up on the rules or history on the wiki: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

the wiki page also has examples of 'Still lifes' 'Oscillators' and 'spaceships' which you can try out in the editor.

more spaceships, guns and other things can be found here: https://www.conwaylife.com/wiki/Main_Page
