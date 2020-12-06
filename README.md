# apple_health
Data manager to export iPhone health data as pandas.DataFrame

---------------------------------------------------------------

Nowadays, there are many devices to measure our health.
For example, smart watch, body scale, and app to record our diet.
Frequently, they are able to export their data, however, the formats have much varieties.
It requires a lot of work to investigate the formats for every device.
Fortunately, these data are integrated to `Health.app` on iPhone.
Of course, we can see the data and nice graphs on our iPhone, but we want to analyze and visualize the data by *ourselves*!
This repository provides a conversion tool of the data to panda's DataFrame on python environment.

## Example of data visualization
<img src="https://ppwww.phys.sci.kobe-u.ac.jp/~mzks/health.png" width="720px">

## Table of Contents

 - [Installation](#installation)
 - [How to export your data](#export_data)
 - [Simple usage](#simple_usage)
 - [Development](#development)

## Installation
On your system,
```
$ python -m pip install git+https://github.com/mzks/apple_health
```

## Export data

<img src="https://user-images.githubusercontent.com/12980386/101274292-25202e00-37e0-11eb-8d1b-ef4378f14faf.gif" width="180px">

Step by step explaination is [here](./Export.md)

## Simple Usage
Online usage on notebook is [here](./notebook/usage.ipynb).

```
from apple_health import manager
man = manager()
man.path = '/path/to/your/zipfile/directory/'
man.zip_name = 'export.zip' # default name
man.as_datetime = True # If you want to obtain the data as datetime type.
```
Then, `df = man.get_df()` (takes a few minutes) will generate data as pandas.DataFrame.


## Development
Please make issues and pull-requests freely.
