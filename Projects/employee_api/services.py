import numpy as np
from database import company_db
from datetime import date

# Queries
def get_all_workers():
    return [worker.model_dump() for worker in company_db.values()]

def get_by_id(id):
    if id in company_db:
        return company_db[id].model_dump()
    return {}

def get_by_department(department):
    results = []
    for worker in company_db.values():
        if worker.department.upper() == department.upper():
            results.append(worker.model_dump())

    if not results:
        return {}
    return results
    
def get_by_salary_range(min_salary=0, max_salary=None):
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

def get_by_company_years(start_date=None, end_date=None):
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

# Statistical search
def get_all_salaries():
    return [worker.salary for worker in company_db.values()]

def get_avg_salary():
    salaries = get_all_salaries()
    
    if not salaries:
        return 0.0
    
    return np.mean(salaries)

def get_max_salary():
    salaries = get_all_salaries()

    if not salaries:
        return -1
    return np.max(salaries)

def get_min_salary():
    salaries = get_all_salaries()

    if not salaries:
        return -1
    return np.min(salaries)

def avg_age():
    years = [worker.birth_year for worker in company_db.values()]

    if not years:
        return -1
    
    array_years = np.array(years)

    current_year = date.today().year

    ages = current_year - array_years

    return np.mean(ages)

def get_avg_satisfaction_rate():
    satisfaction_rates = [worker.satisfaction_rate for worker in company_db.values()]

    if not satisfaction_rates:
        return -1
    return round(np.mean(satisfaction_rates))

def get_number_of_workers():
    return len(company_db.keys())

def get_number_of_workers_by_department():
    workers_by_department = {}
    for worker in company_db.values():
        if worker.department in workers_by_department:
            workers_by_department[worker.department] += 1
        else:
            workers_by_department[worker.department] = 1
    
    if not workers_by_department:
        return {}
    return workers_by_department

def get_number_of_workers_by_department_numpy():
    departments = [worker.department for worker in company_db.values()]
    if not departments:
        return {}
    
    dapartment_name, number_of_workers = np.unique(departments, return_counts=True)

    return {dapartment_name.item(): number_of_workers.item() for dapartment_name, number_of_workers in zip(dapartment_name, number_of_workers)}

# Analytical filters
def get_salaries_bigger_than_avg():
    salary_avg = get_avg_salary()

    bigger_than_avg_salaries = []

    for worker in company_db.values():
        if worker.salary > salary_avg:
            bigger_than_avg_salaries.append(worker.model_dump())

    if not bigger_than_avg_salaries:
        return []
    return bigger_than_avg_salaries

print(get_avg_salary())
print(get_salaries_bigger_than_avg())