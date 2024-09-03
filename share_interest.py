import calendar
month = int(input("enter the month number : "))
year= int(input("enter the year number : "))

_,num_days=calendar.monthrange(year,month)
print(f"number of days {calendar.month_name[month]} {year}: {num_days}")

c={'kbs':15,'bkc':10,'tcl':15,'abc':5}
u=input("enter the company name \n 1.kbs \n 2.bkc \n 3.tcl \n 4.abc:")
if u in c:
    interest = c[u] * num_days
    print(f"number of days {calendar.month_name[month]} {year}: {num_days}")
    print(f"The interest for {u.upper()} is: {interest}")
else:
    print("Invalid company name. Please enter either 'kbs' or 'bkc'.")

