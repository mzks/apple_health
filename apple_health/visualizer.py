import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .core import apple_health

class visualizer(object):

    def __init__(self, man):
        self.df = man.get_df
        

    def show_body_mass(self):
        pass