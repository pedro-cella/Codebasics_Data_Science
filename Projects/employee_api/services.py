import numpy as np
from database import company_db
from datetime import date

def list_all_workers():
    return company_db

def list_by_id(id):
    if id in company_db:
        return company_db[id].model_dump()
    return {}

def list_by_department(department):
    results = []
    for worker in company_db.values():
        if worker.department.upper() == department.upper():
            results.append(worker.model_dump())

    if not results:
        return {}
    return results
    
def list_by_salary_range(min_salary=0, max_salary=None):
    all_salaries = [worker.salary for worker in company_db.values()]

    if max_salary is None:
        max_salary = np.max(all_salaries)

    results = []
    for worker in company_db.values():
        if worker.salary >= min_salary and worker.salary <= max_salary:
            results.append(worker.model_dump())

    if not results:
        return []
    return results

def list_by_company_years(start_date=None, end_date=None):
    if start_date is None:
        start_date = date(2000, 1, 1)

    if end_date is None:
        end_date = date.today()

    results = []

    for worker in company_db.values():
        worker_end_date = worker.end_date if worker.end_date is not None else date.today()
        if worker.start_date >= start_date  and worker_end_date <= end_date:
            results.append(worker.model_dump())
        
    if not results:
        return []
    return results

#testar = list_by_department('HR')
print(list_by_company_years())