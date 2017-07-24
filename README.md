# Minesweeper

This is a project that I started in June 2017 as a part of the UMD FIRE AUSS Summer Fellowship.

The original objective was to model robotic path planning in Minesweeper, but ultimately the project evolved to deal with
sensor fusion and uncertainty in measurements. 

I have implemented python code to model a robot transversing a Minesweeper board attempting to solve it using Bayesian-inspired
methods. The python code does all of the calculations and robot motions, and then the python code will write data to files which
are then read by MATLAB. MATLAB then animates the actions that the robot took.

I have since implemented 1-9 robots autonomously attempting to solve a board. They are about 60% successful, however this depends on
the mine density. 
