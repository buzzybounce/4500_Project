#!/usr/bin/env python3

import numpy
import cozmo
import time
import asyncio
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import color_finder
import functools
import sys
import random


'''
color_list order is in order of colorwheel going clockwise
'''
color_list = ["yellow", "green", "blue", "purple", "red", "orange"]
primary_color_list = ['yellow', 'blue', 'red']
secondary_color_list = ['green', 'purple', 'orange']

'''
game_selector = 0 - Cozmo provides two primary colors and user displays 1 secondary color in response
game_selector = 1 - Cozmo provides one primary or secondary color and user days complimentary color according to color
wheel
'''
game_selector = 1

# game_selector = random.randint(0, 1)



async def gameOne_cozmo_program(robot: cozmo.robot.Robot):

# Cozmo speaks a color
    index = random.randint(0, 5)
    correct_color_to_find = (index + 3) % len(color_list)

    print(color_list[correct_color_to_find])

    await robot.say_text("What color is opposite of " + color_list[index] ).wait_for_completed()

    color_finder_game = color_finder.ColorFinder(robot, color_list[correct_color_to_find])

    await color_finder_game.run()






async def gameTwo_cozmo_program(robot: cozmo.robot.Robot):
    colors_not_different = True
    color_to_pass = ""

    primary_color_1_selected_index = random.randint(0, 2)

    while colors_not_different:
        primary_color_2_selected_index = random.randint(0, 2)
        if primary_color_1_selected_index is not primary_color_2_selected_index:
            colors_not_different = False

    # print(primary_color_1_selected_index)
    # print(primary_color_2_selected_index)

    correct_color_to_find = primary_color_1_selected_index + primary_color_2_selected_index
    await robot.say_text("What color is made by " + primary_color_list[primary_color_1_selected_index] +
                         " and" + primary_color_list[primary_color_2_selected_index]).wait_for_completed()

    color_finder_game = color_finder.ColorFinder(robot, color_list[correct_color_to_find])

    await color_finder_game.run()


    if correct_color_to_find == 1:
        color_to_pass = "Green"
    elif correct_color_to_find == 2:
        color_to_pass = "orange"
    else:
        color_to_pass = "purple"


    print(color_to_pass)
    print(correct_color_to_find)












# Cozmo waits and looks for 1 of 2 colors



    # await colorFinder2.run()

   # await robot.say_text("I found yellow").wait_for_completed()


# modify color_finder to search for specific colors

# If Cozmo cannot find a color in a specified period of time, begin speaking clues


# When correct color detected, deliver a cube to the child with correct color
# When both colors are detected, Cozmo congratulates the players, speaks their names and preforms a dance

# cozmo.run_program(gameOne_cozmo_program, use_viewer = True)


if game_selector == 1:
    cozmo.run_program(gameTwo_cozmo_program, use_viewer=True)
