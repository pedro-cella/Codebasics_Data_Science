from fastapi import FastAPI
import services
from datetime import date

app = FastAPI()

# ==========================================
# QUERIES (Busca de Dados Brutos)
# ==========================================

@app.get("/queries/workers", tags=["Queries"])
def get_all_workers():
    """
    Returns a complete list of all workers from the company
    """
    return services.get_all_workers()

@app.get("/queries/workers/by-id", tags=["Queries"])
def get_by_id(id: int):
    """
    Returns a worker by id
    """
    return services.get_by_id(id)

@app.get("/queries/workers/department", tags=["Queries"])
def get_by_department(department: str):
    """
    Returns a list of workers from an specific department
    """
    return services.get_by_department(department)

@app.get("/queries/workers/salary", tags=["Queries"])
def get_by_salary_range(min_salary: float = 0, max_salary: float = None):
    """
    Returns a list of workers that are in the salary range
    """
    return services.get_by_salary_range(min_salary, max_salary)

@app.get("/queries/workers/company-years", tags=["Queries"])
def get_by_company_years(start_date: date = None, end_date: date = None):
    """
    Returns a list of workers that joined the company between two dates
    """
    return services.get_by_company_years(start_date, end_date)

# ==========================================
# STATISTICAL (Números e Médias)
# ==========================================

@app.get("/statistics/salary/all", tags=["Statistics"])
def get_all_salaries():
    """
    Return a list of all salaries in the company
    """
    return services.get_all_salaries()

@app.get("/statistics/salary/average", tags=["Statistics"])
def get_avg_salary():
    """
    Return the average salary of the company
    """
    return services.get_avg_salary()

@app.get("/statistics/salary/max", tags=["Statistics"])
def get_max_salary():
    return services.get_max_salary()

@app.get("/statistics/salary/min", tags=["Statistics"])
def get_min_salary():
    return services.get_min_salary()

@app.get("/statistics/age/average", tags=["Statistics"])
def get_avg_age():
    """
    Return the average age of workers
    """
    return services.get_avg_age()

@app.get("/statistics/satisfaction/average", tags=["Statistics"])
def get_avg_satisfaction():
    """
    Return the average of satisfaction rate
    """
    return services.get_avg_satisfaction_rate()

@app.get("/statistics/workers/count", tags=["Statistics"])
def get_workers_count():
    """
    Return the total number of workers
    """
    return {"total_workers": services.get_number_of_workers()}

@app.get("/statistics/workers/count-by-department", tags=["Statistics"])
def get_count_by_department():
    """
    Return the total number of workers grouped by department
    """
    return services.get_number_of_workers_by_department_numpy()

# ==========================================
# ANALYTICAL (Filtros e Lógica)
# ==========================================

@app.get("/analysis/salary/above-average", tags=["Analysis"])
def get_workers_above_avg():
    """
    Return workers that earn more than the company average
    """
    return services.get_salaries_bigger_than_avg()

@app.get("/analysis/satisfaction/low-rate", tags=["Analysis"])
def get_low_satisfaction(rate: int = 5):
    """
    Return workers with satisfaction rate below an specified value
    """
    return services.get_satisfaction_rate_below_value(rate)

@app.get("/analysis/tenure/filter", tags=["Analysis"])
def get_by_tenure_logic(years: int, operation: str = "eq"):
    """
    Return workers by company years using operations (eq, gt, lt)
    """
    return services.get_workers_with_n_company_years(years, operation)

@app.get("/analysis/workers/by-age", tags=["Analysis"])
def get_by_age(age: int):
    """
    Return workers with an specific age
    """
    return services.get_workers_by_age(age)

# ==========================================
# INSIGHTS (Resultados de Negócio)
# ==========================================

@app.get("/insights/salary/percentage-above-avg", tags=["Insights"])
def get_percentage_above_avg():
    """
    Return the percentage of workers earning above average
    """
    return services.get_percentage_workers_above_avg()

@app.get("/insights/satisfaction/top-department", tags=["Insights"])
def get_happiest_dept():
    """
    Return the department with the highest average satisfaction
    """
    return services.get_department_with_highest_satisfaction_rate_avg()

@app.get("/insights/salary/lowest-dept", tags=["Insights"])
def get_lowest_salary_dept():
    """
    Return the department with the lowest average salary
    """
    return services.get_department_with_lowest_avg_salary()

@app.get("/insights/salary/top-3", tags=["Insights"])
def get_top_3_salaries():
    """
    Return the 3 highest salaries in the company
    """
    return services.get_top_3_highest_salaries()

@app.get("/insights/workers/veteran", tags=["Insights"])
def get_veteran_worker(status: str = "active"):
    """
    Return the longest tenured worker (status: active, inactive, all)
    """
    return services.get_longest_tenured_worker(status)