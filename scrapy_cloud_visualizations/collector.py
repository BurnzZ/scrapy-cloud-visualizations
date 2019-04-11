"""Contains anything for retrieving all data from Scrapy Cloud."""

from scrapinghub import ScrapinghubClient


class Collector:

    def __init__(self, auth=None, project_id=None):
        self._client = client = ScrapinghubClient(auth)
        self._project = self._client.get_project(project_id)

    def get_spider_job_keys(self, spider_name):
        spider = self._project.spiders.get(spider_name)
        return [entry['key'] for entry in spider.jobs.iter()]

    def get_data_from_jobs(self, job_keys):
        DATA_TO_COLLECT = ('state', 'close_reason', 'finished_time', 'running_time')
        result = {}

        for jobkey in job_keys:
            job = self._client.get_job(jobkey)
            meta = dict(job.metadata.list())
            result[jobkey] = {key: meta[key] for key in DATA_TO_COLLECT}

        return result
