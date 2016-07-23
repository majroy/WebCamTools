[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 

# Introduction

This is an application written to read a pair of high definition, fixed focus webcams for the purposes of tracking crack growth in fatigue and fracture specimens.

Running `WebCamXhairDual.py`, two windows showing grayscale output from the webcams will appear. Pressing `q` will exit and destroy both windows and stop all Python processes.

# Features

By default, the apparent framerate will appear in the top left of each window. There are a series of options for decorating the output windows, ranging from crosshairs (diagonals meeting in the centre of the output window), to a centred rectangle to a scale bar. These can be changed by modifying the main constructor function, `imposeXhair`.

# Requirements

1. Python 2.7.x (tested on 2.7.9)
2. Numpy
3. OpenCV for Python

# Future work

* Threading to improve FPS
* Key mapped to freeze and save

