from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    dict_jobs = [
        {
            "name": "job1",
            "min_salary": 3,
            "max_salary": 4,
            "date_posted": "01-01-2023",
        },
        {
            "name": "job2",
            "min_salary": 1,
            "max_salary": 2,
            "date_posted": "01-02-2023",
        },
    ]

    sort_by(dict_jobs, "min_salary")

    assert dict_jobs == [
        {
            "name": "job2",
            "min_salary": 1,
            "max_salary": 2,
            "date_posted": "01-02-2023",
        },
        {
            "name": "job1",
            "min_salary": 3,
            "max_salary": 4,
            "date_posted": "01-01-2023",
        },
    ]

    sort_by(dict_jobs, "max_salary")

    assert dict_jobs == [
        {
            "name": "job1",
            "min_salary": 3,
            "max_salary": 4,
            "date_posted": "01-01-2023",
        },
        {
            "name": "job2",
            "min_salary": 1,
            "max_salary": 2,
            "date_posted": "01-02-2023",
        },
    ]
