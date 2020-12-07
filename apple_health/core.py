import os
from glob import glob
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime as dt
from matplotlib.dates import DateFormatter, date2num
import matplotlib.ticker as plticker
from scipy import optimize
from matplotlib.offsetbox import OffsetImage, AnnotationBbox 
from tqdm import tqdm


class manager(object):

    def __init__(self):

        self.typedict = {
            'HKQuantityTypeIdentifierHeartRateVariabilitySDNN': 'heart_rate_sdnn',
            #'HKCategoryTypeIdentifierAppleStandHour': 'stand_hour',
            #'HKCategoryTypeIdentifierMindfulSession': 'mind_session',
            #'HKCategoryTypeIdentifierHighHeartRateEvent': 'high_heart_rate_event',
            #'HKCategoryTypeIdentifierAudioExposureEvent': 'audio_exposure_event',
            'HKQuantityTypeIdentifierAppleStandTime': 'stand_time',
            #'HKCategoryTypeIdentifierSleepAnalysis': 'sleep_analysis',
            'HKQuantityTypeIdentifierActiveEnergyBurned': 'active_energy',
            'HKQuantityTypeIdentifierFlightsClimbed': 'flights_climbed',
            'HKQuantityTypeIdentifierAppleExerciseTime' :'exercise_time',
            'HKQuantityTypeIdentifierBasalBodyTemperature': 'besa_body_temp',
            'HKQuantityTypeIdentifierRestingHeartRate': 'resting_heart_rate',
            'HKQuantityTypeIdentifierVO2Max': 'vo2_max',
            'HKQuantityTypeIdentifierWalkingHeartRateAverage': 'walking_heart_rate_average',
            'HKQuantityTypeIdentifierEnvironmentalAudioExposure': 'env_audio_exposure',
            'HKQuantityTypeIdentifierBasalEnergyBurned': 'basal_energy',
            'HKQuantityTypeIdentifierStepCount': 'step_count',
            'HKQuantityTypeIdentifierHeartRate': 'heart_rate',
            'HKQuantityTypeIdentifierDistanceWalkingRunning': 'dist_walk_run',
            'HKQuantityTypeIdentifierBodyTemperature': 'body_temp',
            'HKQuantityTypeIdentifierBodyFatPercentage': 'body_fat',
            'HKQuantityTypeIdentifierLeanBodyMass': 'lean_body_mass',
            'HKQuantityTypeIdentifierBodyMassIndex': 'bmi',
            'HKQuantityTypeIdentifierBodyMass': 'body_mass',
            'HKQuantityTypeIdentifierHeight': 'height',
            'HKQuantityTypeIdentifierDietaryEnergyConsumed': 'dietary_energy',
            'HKQuantityTypeIdentifierDietaryCalcium': 'calcium',
            'HKQuantityTypeIdentifierDietaryCarbohydrates': 'carbohydrates',
            'HKQuantityTypeIdentifierDietaryFatSaturated': 'fat_saturated',
            'HKQuantityTypeIdentifierDietaryFatTotal': 'fat_total',
            'HKQuantityTypeIdentifierDietaryFiber': 'fiber',
            'HKQuantityTypeIdentifierDietaryIron': 'iron',
            'HKQuantityTypeIdentifierDietaryProtein': 'protein',
            'HKQuantityTypeIdentifierDietaryRiboflavin': 'reboflavin',
            'HKQuantityTypeIdentifierDietarySodium': 'sodium',
            'HKQuantityTypeIdentifierDietarySugar': 'suger',
            'HKQuantityTypeIdentifierDietaryThiamin': 'thiamin',
            'HKQuantityTypeIdentifierDietaryVitaminA': 'vitamin_A',
            'HKQuantityTypeIdentifierDietaryVitaminC': 'vitamin_C',
            'HKQuantityTypeIdentifierDietaryVitaminE': 'vitamin_E',
        }

        self.zip_name = 'export.zip'
        self.path = None
        self.path_list = [os.getcwd(),
            os.environ['HOME'], os.environ['HOME']+'/Downloads',
                          ]
        self.zip_names = ['export*.zip']

        self.as_datetime = False
        self.df = None
        self.ready_to_generate = False


    def add_path(self, path):
        self.path_list.insert(0, path)
        return self.path_list


    def add_zip_name(self, zip_name):
        self.zip_names.insert(0, zip_name)
        return self.zip_names



    def set_latest_zip(self, zip_names=None):
        if zip_names is None:
            zip_names = self.zip_names
        files = []
        for path in self.path_list:
            if path[-1] != '/':
                path = path + '/'
            for zip_name in zip_names:
                files.extend(glob(path + zip_name))

        dates = [os.path.getctime(file) for file in files]
        if not dates:
            print('Invalid path or zip file name')
            print('Path list: ')
            print(self.path_list)
            print('Zip name:' + self.zip_name)
            return

        zip_name_with_path = files[np.argmax(dates)]
        self.zip_name = os.path.basename(zip_name_with_path)
        self.path = os.path.dirname(zip_name_with_path)
        self.ready_to_generate = True
        print('File: ' + self.path + '/' + self.zip_name)
        return


    def prepare(self):
        for path in self.path_list:
            if path[-1] != '/':
                path = path + '/'
            for zip_name in self.zip_names:
                if os.path.exists(path + zip_name):
                    self.path = path[:-1]
                    self.zip_name = zip_name
                    self.ready_to_generate = True
                    return

        if not self.ready_to_generate:
            print('Invalid path or zip file name')
            print('Path list: ')
            print(self.path_list)
            print('Zip name list:')
            print(self.zip_names)
            return

        return
        


    def generate(self):

        if not self.ready_to_generate:
            self.prepare()
        if not self.ready_to_generate:
            print('No such file.')
            return
        if self.path[-1] != '/':
            path = self.path + '/'

        filename = path + self.zip_name
        print('target file: ' + filename)
        zipfile.ZipFile(filename).extractall(path)
        tree = ET.parse(path+'apple_health_export/export.xml')
        root = tree.getroot()

        records = [record for record in root if record.get('type') in self.typedict]

        data_types = [self.typedict[record.get('type')] for record in records]
        dates = [record.get('creationDate') for record in records]
        start_dates = [record.get('startDate') for record in records]
        values = [float(record.get('value')) for record in records]
        values = pd.Series(values)

        if self.as_datetime:
            dates = pd.to_datetime(dates)
            start_dates = pd.to_datetime(start_dates)

        self.df = pd.DataFrame({'date': dates,
                           'start_date': start_dates,
                           'value': values,
                           'type': data_types,
                           })



    def get_df(self):

        if self.df is None:
            self.generate()
        return self.df


    def help(self):

        print('Usage: ')
        print("man.add_path('/path/to/your/zipfile')")
        print("man.add_zip_name('export.zip'), for example")
        print("Instead of `them`, `man.set_latest_zip()` will find the latest zip file in the path list")
        print('')
        print("If you want dates as datetime types")
        print("man.as_datetime = True")
        print("Then,")
        print("df = man.get_df()")

