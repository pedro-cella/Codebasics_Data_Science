import numpy as np
from database import company_db
from datetime import date
from heapq import nlargest

# Queries
def get_all_workers():
    return [worker.model_dump() for worker in company_db.values()]

def get_by_id(id):
    if id in company_db:
        return company_db[id].model_dump()
    return None

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
        return None
    
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

def get_avg_age():
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
        return None
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

def get_satisfaction_rate_below_value(rate):
    satisfaction_rates = []
    for worker in company_db.values():
        if worker.satisfaction_rate < rate:
            satisfaction_rates.append(worker.model_dump())
    
    if not satisfaction_rates:
        return []
    return satisfaction_rates

def get_workers_with_n_company_years(company_years, operation):
    workers = []
    year_today = date.today().year
    
    for worker in company_db.values():
        tenure = worker.start_date.year
        if operation == "eq" and tenure == company_years:
            workers.append(worker.model_dump())
        elif operation == "gt" and tenure > company_years:
            workers.append(worker.model_dump())
        elif operation == "lt" and tenure < company_years:
            workers.append(worker.model_dump())

    if not workers:
        return []
    return workers

def get_workers_from_a_department(department):
    departments = np.unique([worker.department for worker in company_db.values()])
    workers = []

    for worker in company_db.values():
        if worker.department.upper() == department.upper():
            workers.append(worker.model_dump())

    if not workers:
        return []
    return workers 

def get_workers_by_age(age):
    workers = []
    year_today = date.today().year

    for worker in company_db.values():
        if (year_today - worker.birth_year) == age:
            workers.append(worker.model_dump())

    if not workers:
        return []
    return workers

# Insights
def get_percentage_workers_above_avg():
    avg_salary = get_avg_salary()
    total_workers = len(get_all_workers())
    above_avg_workers = []

    for worker in company_db.values():
        if worker.salary > avg_salary:
            above_avg_workers.append(worker.model_dump())

    above_avg_ratio = (len(above_avg_workers)/total_workers)

    if not above_avg_workers:
        return -1
    return f"{above_avg_ratio*100}%"

def get_avg_satisfaction_by_department():
    departments_satisfaction_rate = {}

    for worker in company_db.values():
        if worker.department in departments_satisfaction_rate:
            departments_satisfaction_rate[worker.department].append(worker.satisfaction_rate)
        else:
            departments_satisfaction_rate[worker.department] = [worker.satisfaction_rate]
    
    averages = {department: np.mean(rates) for department, rates in departments_satisfaction_rate.items()}

    if not departments_satisfaction_rate:
        return {}
    return averages

def get_department_with_highest_satisfaction_rate_avg():
    averages = get_avg_satisfaction_by_department()

    if not averages:
        return None
    return max(averages, key=averages.get)

def get_avg_salary_by_department():
    departments_salary = {}

    for worker in company_db.values():
        if worker.department in departments_salary:
            departments_salary[worker.department].append(worker.salary)
        else:
            departments_salary[worker.department] = [worker.salary]

    averages = {department: np.mean(rates) for department, rates in departments_salary.items()}

    if not averages:
        return {}
    return averages

def get_department_with_lowest_avg_salary():
    averages = get_avg_salary_by_department()

    if not averages:
        return None
    return min(averages, key=averages.get)

def get_longest_tenured_worker(status):
    workers = [
        worker for worker in company_db.values()
        if (status.lower() == "all") or
           (status.lower() == "active" and worker.end_date is None) or
           (status.lower() == "inactive" and worker.end_date is not None)
    ]

    if not workers:
        return None
    
    longest_tenured = min(workers, key=lambda worker: (worker.start_date, worker.registration_code))
    return longest_tenured.model_dump()

def get_top_3_highest_salaries():
    workers = list(company_db.values())

    if not workers:
        return []
    
    top_3_salaries = nlargest(3, workers, lambda worker: worker.salary)

    return [worker.model_dump() for worker in top_3_salaries]