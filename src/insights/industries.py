from typing import List, Dict

# import src.insights.jobs as jobs
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industry = []

    for row in read(path):
        if row["industry"] not in unique_industry and row["industry"] != "":
            unique_industry.append(row["industry"])

    return list(unique_industry)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    industry_filtered = []

    for job in jobs:
        if job["industry"] == industry:
            industry_filtered.append(job)

    return list(industry_filtered)
