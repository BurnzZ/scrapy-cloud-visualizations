"""Contains anything that involves in visualizing the data."""

import seaborn as sns
import matplotlib.pyplot as plt

from core import transform_data
from collector import Collector


class Visualizer:

    def __init__(self, auth=None, project_id=None):
        self._project_id = project_id
        self._collector = Collector(auth=auth, project_id=project_id)

    def show_heatmap_jobs(self, spidername=None):
        jobkeys = self._collector.get_spider_job_keys(spidername)
        print(f"KEYS: {jobkeys}")
        jobs_data = self._collector.get_data_from_jobs(jobkeys)
        print(f"RAW DATA: {jobs_data}")

        df_grid = transform_data(jobs_data)
        print(f"TRANSFORMED DATA: {df_grid}")

        sns.set()
        ax = sns.heatmap(df_grid, cmap='BuGn', cbar=False, annot=True,
                         yticklabels=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
                         xticklabels=range(0, 24))
        ax.set_title(spidername + " runs")
        plt.show()
