[![Build Status](https://travis-ci.org/marinamarina/bowling.svg?branch=master)](https://travis-ci.org/marinamarina/bowling)

# Ten-pin bowling
This repository contains the codebase for the Technical Assessment as a preparation for the technical assessment session

## Overview

The program allows to keep score of a bowling game for up to 6 people.

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