"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class CSVDataSource:
    """Class Data Source
    """
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def load_inflammation_data(self) -> list[str]:
        """Load all csv files from directory

        :param data_path: name of direc containing csv files
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = list(map(models.load_csv, data_file_paths))
        return data


def analyse_data(data_source: CSVDataSource) -> None:
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_daily_standard_deviation_by_day(data)


    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

    return daily_standard_deviation

def compute_daily_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation
