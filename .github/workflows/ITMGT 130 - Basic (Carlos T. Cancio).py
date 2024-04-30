'''Python: Basic

15 points

This assignment will develop your familiarity with doing simple computations in Python.
'''

def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = int(gross_pay * (1 - tax_rate))
    remaining_pay = after_tax_pay - expenses
    return remaining_pay

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    remaining_material = total_material - total_consumed
    output = str(remaining_material) + material_units
    return output

def interest(principal, rate, periods):
    final_value = principal + int(principal * rate * periods)
    return final_value
