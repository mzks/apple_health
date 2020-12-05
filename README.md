# apple_health
Data manager to export iPhone health data as pandas.DataFrame

---------------------------------------------------------------

Nowadays, there are many devices to measure our health.
For example, smart watch, body scale, and app to record our diet.
Flequently, they are able to export their data, however the formats have much varieties.
It requires a lot of work to investigate the formats for every device.
Fortunatelly, these data are integrated to `Health.app` on iPhone.
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
 1. In your iPhone, tap `health` app.
<img src="https://user-images.githubusercontent.com/12980386/101259971-d2a72900-376f-11eb-9d83-03382a9a943d.png" width="180px">

 2. Tap upper right icon
<img src="https://user-images.githubusercontent.com/12980386/101259970-d20e9280-376f-11eb-857d-7bcff046e70c.png" width="180px">

 3. Scroll down to the bottom
<img src="https://user-images.githubusercontent.com/12980386/101259969-d175fc00-376f-11eb-9b57-445529cb2cee.png" width="180px">

 4. Tap `Export All Health Data`
<img src="https://user-images.githubusercontent.com/12980386/101259968-d0dd6580-376f-11eb-975c-bb1277436268.png" width="180px">

 5. Tap `Export` on the dialog
<img src="https://user-images.githubusercontent.com/12980386/101259963-cc18b180-376f-11eb-9b66-a68aa7f0c94b.png" width="180px">

 6. Wait a few minites...
<img src="https://user-images.githubusercontent.com/12980386/101259973-d5098300-376f-11eb-8948-ba8d873a2bde.png" width="180px">

 7. Done! Send the zip file to your system.
<img src="https://user-images.githubusercontent.com/12980386/101259972-d470ec80-376f-11eb-8af2-e531dc3c7c01.png" width="180px">

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
