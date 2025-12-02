import numpy as np
from scipy.stats import pearsonr

class WeatherAnalyzer:
    def __init__(self, temps, hums):
        self.temps = np.array(temps, dtype=float)
        self.hums = np.array(hums, dtype=float)

    def avg_temp(self):
        return np.mean(self.temps)

    def max_temp(self):
        return np.max(self.temps)

    def min_temp(self):
        return np.min(self.temps)

    def correlation(self):
        return pearsonr(self.temps, self.hums)[0]
