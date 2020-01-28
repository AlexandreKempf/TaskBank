<h1 align="center">TaskBank</h1>

**A library of machine learning tasks for [HackDuck](https://github.com/AlexandreKempf/HackDuck)**

[![PyPI version](https://badge.fury.io/py/TaskBank.svg)](https://badge.fury.io/py/TaskBank)


## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [FAQ](#faq)
- [See Also](#see-also)

## Installation:
You can install it as:
- __a pip package:__ `pip install TaskBank`
- __a github folder:__ `git clone https://github.com/AlexandreKempf/TaskBank.git` and then `pip install .` in the folder

## Features:
- __easy to use:__ Each task is written as a simple Python function
- __complete:__ Implement the functions from the best machine learning packages (scikit-learn, pandas, imgaug ...)
- __MLFlow integration:__ Save logs and metrics automatically when using [HackDuck](https://github.com/AlexandreKempf/HackDuck)
- __use it for your own scripts:__ `import TaskBank` as a classic python package

## FAQ:
- __How can I install it ?__
Just type `pip install TaskBank` in the terminal.
- __How can I use it ?__
Once it is install, build your flow with [HackDuck](https://github.com/AlexandreKempf/HackDuck) using the best tasks from TaskBank.
- __Is it free to use ?__
It is! And even better, the code is open source.
- __How can I contribute ?__
I'm looking for contributors to write new tasks or to play with them

## See Also:
[HackDuck](https://github.com/AlexandreKempf/HackDuck)


## TODO:
 - [ ] Implement a pytorch model with lightning or ignite
 - [ ] Implement optimization with optuna
 - [ ] Implement time series augmentation https://github.com/terryum/Data-Augmentation-For-Wearable-Sensor-Data/blob/master/Example_DataAugmentation_TimeseriesData.ipynb
 - [ ] Implement the loading of famous datasets
 - [ ] Implement the bases for a good ETL (load several file types, panda support, filters ...)
