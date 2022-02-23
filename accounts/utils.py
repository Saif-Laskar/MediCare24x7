from datetime import date

def calc_age(DOB):
    today = date.today()
    return today.year-DOB.year -((today.month, today.day) < (DOB.month, DOB.day))