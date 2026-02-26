from datetime import datetime

def calculate_termination_benefits(parsed_hire_date, parsed_resignation_date, salary):
    
    parsed_hire_date = datetime.strptime(parsed_hire_date, "%d/%m/%Y")
    parsed_resignation_date = datetime.strptime(parsed_resignation_date, "%d/%m/%Y")
    

    if parsed_resignation_date <= parsed_hire_date:
        raise ValueError("A data de demissão deve ser posterior à data de admissão.")
    
    try:
        last_work_anniversary = parsed_hire_date.replace(year=parsed_resignation_date.year)
    except ValueError:
        last_work_anniversary = parsed_hire_date.replace(
            year=parsed_resignation_date.year,
            day=28
        )

    if last_work_anniversary > parsed_resignation_date:
        last_work_anniversary = last_work_anniversary.replace(year=parsed_resignation_date.year - 1)

    vacation_months = (parsed_resignation_date.year - last_work_anniversary.year) * 12 
    vacation_months += (parsed_resignation_date.month - last_work_anniversary.month)    
    
    vacation_amount = (salary / 12) * vacation_months

    
    resignation_year_start = datetime(parsed_resignation_date.year, 1 , 1)

    thirteenth_salary_months = (parsed_resignation_date.year - resignation_year_start.year) * 12 
    thirteenth_salary_months += (parsed_resignation_date.month - resignation_year_start.month)
    
    thirteenth_salary_amount = (salary / 12) * thirteenth_salary_months

    return {
        "Valor Decimo Terceiro": f"R${thirteenth_salary_amount}",
        "Valor Ferias": f"R${vacation_amount}"
    }
