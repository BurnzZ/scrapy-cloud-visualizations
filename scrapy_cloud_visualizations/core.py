"""Contains all of the core logic of the package."""

import pandas as pd
import numpy as np


# TODO: The grid is set on 7days by 24hrs at the moment,
#   make this flexible in the future like 24hrs but on 15/30 mins interval
def convert_np_grid(df):
    """Takes a data frame and converts the start and end times into
    a 2D grid that represents a heatmap.
    """

    grid = np.zeros((7, 24))

    # TODO: vectorize later on

    row = np.vstack((
        # These are the x-axis
        df.datetime_start.dt.dayofweek.values, df.datetime_end.dt.dayofweek.values,
        # These are the y-axis
        df.datetime_start.dt.hour.values, df.datetime_end.dt.hour.values
    )).T

    for x1, x2, y1, y2 in row:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 1

    return grid

def transform_data(jobs_data):
    df = pd.DataFrame(jobs_data).T
    df = df.rename(columns={'finished_time': 'epoch_end', 'running_time': 'epoch_start'})
    df['datetime_end'] = pd.to_datetime(df.epoch_end, unit='ms')
    df['datetime_start'] = pd.to_datetime(df.epoch_start, unit='ms')

    grid = convert_np_grid(df)
    return grid
