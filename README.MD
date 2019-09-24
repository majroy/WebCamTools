[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0) 

# Introduction

This is an application written to read a pair of high definition, fixed focus webcams for the purposes of tracking crack growth in fatigue and fracture specimens.

Running `WebCamXhairSingle.py` will read the first webcam available. Pressing `q` will exit and destroy both windows and stop all Python processes. Pressing `p` will save .png files when the key was pressed.

Running `WebCamXhairDual.py`, two windows showing grayscale output from the webcams will appear, as in `WebCamXhairSingle.py`. Pressing `p` will save the output of each webcam to the directory that the script is running from as 00.png for camera 1, and 01.png for camera 2. *Note that two webcams connected to separate USB ports are required*.

# Features

By default, the apparent framerate will appear in the top left of each window. There are a series of options for decorating the output windows, ranging from crosshairs (diagonals meeting in the centre of the output window), to a centred rectangle to a scale bar. These can be changed by modifying the main constructor function, `imposeXhair`.

# Requirements

1. Python 3.6.x (tested on 3.6.0)
2. Numpy 1.16
3. OpenCV for Python 4.1.1
4. Generic webcams - Microsoft Lifecams and integrated laptop webcams were employed


