import logging
import asyncio
from typing import List

from tqdm import tqdm

logger = logging.getLogger('aiodownloader.utils')


def pretty_tqdm(size: int, name: str):
    """Returns a tqdm pbar with some predefined options"""
    return tqdm(total=size, desc=name, unit_scale=True, unit='B')


async def multi_progress_bar(jobs: List[any]):
    """
    Creates one tqdm progress bar for every download job and updates all of them asynchronously 
    every sec according to how much the job has avanced since the last update.

    :param jobs: list of download jobs that will have a progress bar 
    :return: 
    """
    # Getting the job sizes to create the tqdm pbars
    jobs_done, _ = await asyncio.wait([job.get_size() for job in jobs])
    job_sizes = [done.result() for done in jobs_done]

    pbars = [pretty_tqdm(job_size, job.file_name) for job_size, job in zip(job_sizes, jobs)]

    # List to store the last seen progress from the jobs.
    last_progresses = [0] * len(jobs)

    uncompleted_jobs = True
    while uncompleted_jobs:
        uncompleted_jobs = False

        new_progresses = []
        for pbar, job, last_progress in zip(pbars, jobs, last_progresses):
            if not job.completed:
                # Updating the pbar with how much the job has advanced since the last update
                pbar.update(job.progress - last_progress)
                new_progresses.append(job.progress)
                uncompleted_jobs = True

        last_progresses = new_progresses
        await asyncio.sleep(0.5)






