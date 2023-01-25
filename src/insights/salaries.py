from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    max_salary = 0

    for row in read(path):
        if (
            row["max_salary"].isnumeric()
            and int(row["max_salary"]) > max_salary
        ):
            max_salary = int(row["max_salary"])

    return int(max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    min_salary = 0

    for row in read(path):
        if row["min_salary"].isnumeric() and min_salary == 0:
            min_salary = int(row["min_salary"])
        if (
            row["min_salary"].isnumeric()
            and int(row["min_salary"]) < min_salary
        ):
            min_salary = int(row["min_salary"])

    return int(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("`min_salary` or `max_salary` doesn't exists")
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"],
        int,
    ):
        raise ValueError("`min_salary` or `max_salary` aren't valid integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("`min_salary` is greather than `max_salary`")
    if type(salary) not in [int, str]:
        raise ValueError("`salary` isn't a valid integer")
    if int(salary) < job["min_salary"] or int(salary) > job["max_salary"]:
        return False
    return True


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
