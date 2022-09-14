def leap_year(year):
    """Checks for leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # Only if all the conditions are satisfied the following code will run. 
                return print(f"{year} is a leap year.")
            else:
                # If all the coditions are true except dividing by 400 this code will run.
                return print(f"{year} ain't leap year.")
        # If the year is not divisibe by 100 but divisble by 4 the following code will run..
        return print(f"{year} is a leap year.")
    # If the year is not divisible by 4 the following code will run.
    return print(f"{year} ain't a leap year.")


user = int(input("Enter the year :"))
test = leap_year(user)
