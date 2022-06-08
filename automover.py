import pyautogui as pag
import time
#always give python file time before cont.

time.sleep(3)

#mouse functions
print(pag.size())       #Prints resolution of screen    
print(pag.position())   #Prints current mouse position


pag.click(500,500,3,3,button="left") #Clicks mouse (x,y,num of clicks,duration, which button)
pag.rightClick, pag.leftClick, pag.doubleClick, pag.tripleClick()

pag.scroll(-10) #scrolls down 10px
pag.scroll(10)  #scrolls up 10px

pag.mouseUp(100,100, button = "left") #mouse button down or up

time.sleep(3)
distance = 300
while distance > 0:
    pag.dragRel(distance, 0, 1, button = "left")
    distance = distance - 20
    pag.dragRel(0, distance, 1, button = "left")
    pag.dragRel(-distance, 0, 1, button = "left")
    distance = distance - 20
    pag.dragRel(0, -distance, 1, button = "left")
time.sleep(2)

#failsafe = manually move mouse to any corner of the screen
