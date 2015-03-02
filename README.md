[![Build Status](https://travis-ci.org/marinamarina/bowling.svg?branch=master)](https://travis-ci.org/marinamarina/bowling)

Temporarily for a private repo:
[![Build Status](https://magnum.travis-ci.com/marinamarina/bowling.svg?token=mjEQw6pBznfzG3bFcBry?branch=master)](https://magnum.travis-ci.com/marinamarina/bowling)

# Ten-pin bowling
This repository contains the codebase for the Technical Assessment as a preparation for the technical assessment session

## Overview

The program is a scoreboard that allows to keep score of a bowling game for up to 6 people.

### There are several symbols used when keeping score:
* an "X" signifies a "strike" in which 10 pins have been knocked down by the first roll of the ball in a frame
* a "/" signifies a "spare" in which all 10 pins have been knocked down on the second roll in a frame
* a "-" indicates that no pins were knocked down on that roll, called a "miss"



## Pre-requisites

* Python (version >= 2.7)

## Installation

Note: all of the commands in the rest of this README are relative to the root of the repository. Therefore, when you've downloaded the repo, make sure you `cd bowling` to go into the top level of the repository.

* clone the repository from your terminal using `git clone https://github.com/marinamarina/bowling.git`

## Running the program

* run `python play.py`

## Running tests

Run the unit tests:

Python version 2.7 or earlier `python -m unittest discover`
Python version 3.1 or earlier `python3 -m discover`
Python version 3.2 or earlier `python3 -m unittest discover`

Or just leave it to Travis (Every push will also trigger a new build on Travis CI).