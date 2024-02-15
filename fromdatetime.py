from datetime import datetime

def calculate_days_lived(birthdate, current_date):
    birth_datetime = datetime.strptime(birthdate, "%Y-%m-%d")
    current_datetime = datetime.strptime(current_date, "%Y-%m-%d")
    days_lived = (current_datetime - birth_datetime).days
    return days_lived

birthdate = "2005-07-08"
current_date = "2024-02-09"

days_lived = calculate_days_lived(birthdate, current_date)
print("You have lived for {} days.".format(days_lived))
