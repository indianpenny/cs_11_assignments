"""
Created on Oct 6 14:37:20 2022

@author: Srishti
"""

#A GUI (Graphic User Interface) is an interface between the human user and the computer that uses graphic objects such as buttons, menus, etc. and mouse input to navigate and make changes.

#GUI's require event handlers in code to define what should happen when a mouse click occurs in a specific region (such as the region defined by a rectangular button).

#Make a program that draws a picture of a character, or a scene. 
#You should draw at least 10 shapes, and 3 different colors.

#See the demo code below to understand how coordinates work in programming.
#The purpose of this code to make a picture of Frosty's longlost cousin. 

import simplegui

# Handler to draw on canvas
def draw(canvas):
    background = simplegui.load_image("https://img.itch.zone/aW1nLzUyNTM1MDcucG5n/315x250%23c/FZOJKF.png")

    canvas.draw_image(background, 
                      [315/2,250/2], 
                      [315,250], 
                      [300/2,200/2],
                      [300,200])

    canvas.draw_circle([150,100], 70, 1.5, 'black', 'white')
    canvas.draw_circle([150,107], 14, 2, 'orange', 'orange')
    canvas.draw_circle([120,80], 7, 2, 'black','black')
    canvas.draw_circle([119.5,75], 7, 2, 'black','black')
    canvas.draw_circle([178.1,80], 7, 2, 'black','black')
    canvas.draw_circle([178.5,75], 7, 2, 'black','black')
    canvas.draw_circle([190,125], 3, 2, 'black','black')
    canvas.draw_circle([180,135], 3, 2, 'black','black')
    canvas.draw_circle([170,142], 3, 2, 'black','black')
    canvas.draw_circle([157,147], 3, 2, 'black','black')
    canvas.draw_circle([143,146.5], 3, 2, 'black','black')
    canvas.draw_circle([130,142], 3, 2, 'black','black')
    canvas.draw_circle([120,135], 3, 2, 'black','black')
    canvas.draw_circle([110,125], 3, 2, 'black','black')
    canvas.draw_circle([150,245], 90, 5, 'white', 'white')
    canvas.draw_line([237,192], [240,194], 175, 'brown')
    canvas.draw_line([63,192], [60,194], 175, 'brown')
    canvas.draw_line([105,25], [195,25], 50, 'black')
    canvas.draw_line([85,43], [215,43], 15, 'black')
    canvas.draw_polygon([(149.9,189), (150,188.8), (150.1,189)], 7, 'black', 'black')
    canvas.draw_text("Oh I can't wait", [19,25], 13, 'black')
    canvas.draw_text("for winter break!", [205,25], 13, 'black')

    
                
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Frosty's longlost cousin!!!", 300, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
