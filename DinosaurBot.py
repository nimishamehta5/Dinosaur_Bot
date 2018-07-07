from PIL import ImageGrab,ImageOps
import pyautogui
import time
import numpy as np

class Coordinates():
    #Pixel coordinates of the replay button as per screenshot
    replay=(347,417)
    #Pixel coordinates of top right corner of dino as per screenshot, we aren't 
    #using it in our program, but can if we want to specify relative position of box
    dino=(179,422)
    
def restartGame():
    pyautogui.click(Coordinates.replay)
    
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    
restartGame()
time.sleep(1)

def imageGrab():
    #'box' defines the area in front of the dino where an obstacle is likely
    #as per the screenshot, which may vary with every screen/layout
    box=(146,399,223,431)
    image=ImageGrab.grab(box)
    #convert to grayscale to avoid getting R,G,B values
    gray_image=ImageOps.grayscale(image)
    a=np.array(gray_image) #converts picture to intensity array
    return a.sum()
    
def main():
    restartGame()
    for i in range(1000):
        #608608 is the a.sum() value when there is no obstacle (empty space)
        if(imageGrab()!=608608):
            pressSpace()
            time.sleep(0.1)
             
main()
