#!/usr/bin/python
"""
https://www.codewars.com/kata/plotting-points-on-a-grid
Make a class Grid which accepts two arguments, width and height and makes a multiline string containing something like this:

width=10
height=10
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000

It has a function plot_point which plots an X on the grid. It accepts two arguments, x and y. x and y should be 1-based.

x = 5
y = 3
0000000000
0000000000
0000X00000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
"""
class Grid():

    def __init__(self, width, height):
        self.grid = ""
        self.wid = width
        for i in range(height):
            self.grid += ("0" * width + "\n")
        self.grid = self.grid[:-1]

    def plot_point(self, x, y):
        mylist = list(self.grid)
        x -= 1
        y -= 1
        mylist[y * (int(self.wid) + 1) + x] = "X"
        self.grid = ''.join(mylist)
        print(self.grid)

    def __repr__(self):
        pass


gg = Grid(10, 10)
gg.plot_point(5, 2)