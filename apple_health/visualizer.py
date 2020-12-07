from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import seaborn as sns
sns.set()

class visualizer(object):


    def __init__(self, man):
        self.df = man.get_df()
        if self.df is None:
            print('Before visualization, please generate dataframe (apple.health.manager.get_df()')
        self.as_datetime = man.as_datetime
        self.timezone = man.timezone

    def show(self, **kwargs):

        self.type = kwargs['type']
        self.begin_date = dt.datetime.strptime(kwargs['begin_date'], '%Y-%m-%d').replace(tzinfo=dt.timezone(dt.timedelta(hours=self.timezone)))
        self.end_date = dt.datetime.strptime(kwargs['end_date'], '%Y-%m-%d').replace(tzinfo=dt.timezone(dt.timedelta(hours=self.timezone)))

        self.df = self.df[self.df['type'] == self.type]
        if self.as_datetime:
            date = self.df['date']
        else:
            date = pd.to_datetime(self.df['date'])
        self.df = self.df[(self.begin_date < date )&( date < self.end_date)]


        fig, ax = plt.subplots()
        ax.plot(self.df['date'], self.df['value'])
        ax.set_ylabel(self.type)
        ax.set_xticks(ax.get_xticks()[::int(len(ax.get_xticks()) / 10)])
        fig.autofmt_xdate(rotation=90)

        return ax
