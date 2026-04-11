from datetime import datetime

def calculate_age(birth_year):
    # Get the current year from the system clock
    current_year = datetime.now().year
    
    # Calculate the difference
    age = current_year - birth_year
    
    return age

my_age = calculate_age(2000)
# print(my_age)