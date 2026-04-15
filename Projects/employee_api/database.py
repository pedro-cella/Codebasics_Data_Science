from models import Employee, Outsourced, Intern
from datetime import date

company_db = {
    1: Employee(registration_code=1111, name="Pedro", lastname="Cella", birth_date=1999, salary=8000.00, 
                start_date=date(2026, 2, 12), end_date=None, satisfaction_rate=10, department="HR"),
    2: Employee(registration_code=2222, name="Caio", lastname="Noronha", birth_date=2000, salary=6000.00, 
                start_date=date(2020, 3, 2), end_date=None, satisfaction_rate=6, department="IT"),
    3: Outsourced(registration_code=3333, name="Maria", lastname="Victória", birth_date=1998, salary=10000.00, 
                start_date=date(2023, 5, 24), end_date=None, satisfaction_rate=3, department="Finances"),
    4: Outsourced(registration_code=4444, name="Carlos", lastname="Peçanha", birth_date=1983, salary=12400.56, 
                start_date=date(2018, 6, 15), end_date=None, satisfaction_rate=10, department="TI"),
    5: Intern(registration_code=5555, name="Pedro", lastname="Cella", birth_date=2000, salary=1600.00, 
                start_date=date(2012, 2, 4), end_date=None, satisfaction_rate=6, department="HR"),
    6: Intern(registration_code=6666, name="Felicia", lastname="James", birth_date=2004, salary=1600.00, 
                start_date=date(2026, 1, 10), end_date=date(2026, 3, 12), satisfaction_rate=8, department="Marketing"),
}