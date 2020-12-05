import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
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
        self.path = '/Users/mzks/Downloads/'
        self.as_datetime = False

    def get_df(self, zip_name=None, path=None):

        if zip_name == None:
            zip_name = self.zip_name
        if path == None:
            path = self.path
        if path[-1] != '/':
            path = path + '/'
        filename = path + zip_name
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

        df = pd.DataFrame({'date': dates,
                   'start_date': start_dates,
                    'value': values,
                    'type': data_types,
                    })

        return df


    def help(self):

        print('Usage: ')
        print("man.path = '/path/to/your/zipfile/'")
        print("man.zip_name = 'export.zip', for example")
        print('')
        print("If you want dates as datetime types")
        print("man.as_datetime = True")
        print("Then,")
        print("df = man.get_df()")

