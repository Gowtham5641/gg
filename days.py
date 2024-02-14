def convert_days(days):
    years = days // 365
    days %= 365
    months = days // 30
    days %= 30
    weeks = days // 7
    days %= 7
    return years, months, weeks, days

def main():
    num_days = int(input("Enter the number of days: "))
    years, months, weeks, days = convert_days(num_days)
    print(f"{num_days} days is equal to:")
    print(f"Years: {years}")
    print(f"Months: {months}")
    print(f"Weeks: {weeks}")
    print(f"Days: {days}")

if __name__ == "__main__":
    main()
