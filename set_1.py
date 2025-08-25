'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''

import math

def savings(gross_pay, tax_rate, expenses):
    '''Savings.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    '''
    after_tax = math.floor(gross_pay * (1 - tax_rate))
    remaining = after_tax - expenses
    return remaining


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    '''
    total_consumed = num_jobs * job_consumption
    waste = total_material - total_consumed
    return f"{waste}{material_units}"


def interest(principal, rate, periods):
    '''Interest.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    '''
    interest_amount = principal * rate * periods
    final_value = math.floor(principal + interest_amount)
    return final_value


# ---------- Test Block ----------
if __name__ == "__main__":
    print(savings(10000, 0.12, 2000))        # expect 6800
    print(material_waste(100, "kg", 5, 10))  # expect "50kg"
    print(interest(10000, 0.05, 2))          # expect 11000

