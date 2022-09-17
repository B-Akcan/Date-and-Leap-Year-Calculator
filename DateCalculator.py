import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

days = list(range(1,32))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_of_months = {"January": 31, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
years = list(range(1,2101))

def calculate(day1, month1, year1, day2, month2, year2):
    try:
        day_from = day1.get()
        month_from = month1.get()
        year_from = year1.get()
        day_to = day2.get()
        month_to = month2.get()
        year_to = year2.get()
    except:
        showerror(title="Error", message="Please select value(s) from the list(s).")
        return

    if day_from not in days or day_to not in days or month_from not in months or month_to not in months:
        showerror(title="Error", message="Please select proper value(s).")
        return
    elif year_from not in years or year_to not in years:
        showerror(title="Error", message="Please select year(s) between 1 and 2100.")
        return
    elif month_from != "February" and days_of_months[month_from] < day_from:
        showerror(title="Error", message=f"{month_from} consists of {days_of_months[month_from]} days but you chose {day_from} days.")
        return
    elif month_to != "February" and days_of_months[month_to] < day_to:
        showerror(title="Error", message=f"{month_to} consists of {days_of_months[month_to]} days but you chose {day_to} days.")
        return
    elif month_from == "February":
        if is_leap_year(year_from) and day_from > 29:
            showerror(title="Error", message=f"{year_from} is a leap year therefore february is 29 days but you chose {day_from} days.")
            return
        elif (not is_leap_year(year_from)) and day_from > 28:
            showerror(title="Error", message=f"February is 28 days but you chose {day_from} days.")
            return
    elif month_to == "February":
        if is_leap_year(year_to) and day_to > 29:
            showerror(title="Error", message=f"{year_to} is a leap year therefore february is 29 days but you chose {day_to} days.")
            return
        elif (not is_leap_year(year_to)) and day_to > 28:
            showerror(title="Error", message=f"February is 28 days but you chose {day_to} days.")
            return

    month_from_index = months.index(month_from)
    month_to_index = months.index(month_to)
    if year_from > year_to:
        showerror(title="Error", message="The first year chosen must be less than or equal to the second year chosen.")
        return
    elif year_from == year_to:
        if month_from_index > month_to_index:
            showerror(title="Error", message="The first month chosen must be former than or the same with the second month chosen.")
            return
        elif month_from_index == month_to_index:
            if day_from > day_to:
                showerror(title="Error", message="The first day chosen must be less than or equal to the second day chosen.")
                return
            else:
                day_diff = day_to - day_from
                res.set(f"{day_diff} day(s).")
                return
        else:
            day_diff = (month_to_index - month_from_index)*30 + day_to - day_from
            res_months = day_diff // 30
            res_days = (day_diff - res_months*30)
            res.set(f"{res_months} month(s), {res_days} day(s).")
            return
    else:
        day_diff = (year_to - year_from)*365 + (month_to_index - month_from_index)*30 + day_to - day_from
        res_years = day_diff // 365
        res_months = (day_diff - res_years*365) // 30
        res_days = (day_diff - res_years*365 - res_months*30)
        res.set(f"{res_years} year(s), {res_months} month(s), {res_days} day(s).")
        return

def reset():
    day1_var.set("")
    month1_var.set("")
    year1_var.set("")
    day2_var.set("")
    month2_var.set("")
    year2_var.set("")
    res.set("")

def is_leap_year(*args):
    year = args[0]
    if len(args) == 2: res_2 = args[1]

    if year % 100 == 0 and year % 400 == 0:
        if len(args) == 2: res_2.set("Yes!")
        return 1
    elif year % 100 == 0 and year % 400 != 0:
        if len(args) == 2: res_2.set("No!")
        return 0
    elif year % 100 != 0:
        if year % 4 == 0:
            if len(args) == 2: res_2.set("Yes!")
            return 1
        else:
            if len(args) == 2: res_2.set("No!")
            return 0


root = tk.Tk()
root.title("Date Clcltr")
root.geometry("235x300+50+50")
root.resizable(0, 0)

title_style = ttk.Style()
title_style.configure("Title.TLabel", font=("TkDefaultFont", 14))

title1 = ttk.Label(root, text="Date Calculator", style="Title.TLabel", foreground="darkred")
title1.place(x=5, y=5)

lbl1 = ttk.Label(root, text="From:")
lbl1.place(x=5, y=40)

day1_var = tk.IntVar()
day1_var.set("")
day1 = ttk.Combobox(root, textvariable=day1_var, values=days)
day1.place(x=45, y=40, width=40)

month1_var = tk.StringVar()
month1_var.set("")
month1 = ttk.Combobox(root, textvariable=month1_var, values=months)
month1.place(x=90, y=40, width=80)

year1_var = tk.IntVar()
year1_var.set("")
year1 = ttk.Combobox(root, textvariable=year1_var, values=years)
year1.place(x=175, y=40, width=54)

lbl2 = ttk.Label(root, text="To:")
lbl2.place(x=5, y=65)

day2_var = tk.IntVar()
day2_var.set("")
day2 = ttk.Combobox(root, textvariable=day2_var, values=days)
day2.place(x=45, y=65, width=40)

month2_var = tk.StringVar()
month2 = ttk.Combobox(root, textvariable=month2_var, values=months)
month2.place(x=90, y=65, width=80)

year2_var = tk.IntVar()
year2_var.set("")
year2 = ttk.Combobox(root, textvariable=year2_var, values=years)
year2.place(x=175, y=65, width=54)

bttn_reset = ttk.Button(root, text="Reset", command=reset)
bttn_reset.place(x=120, y=90, width=110)

result_lbl = ttk.Label(root, text="Result:")
result_lbl.place(x=5, y=125)

res = tk.StringVar()
res.set("")
result = ttk.Label(root, textvariable=res)
result.place(x=45, y=125)

bttn_calculate = ttk.Button(root, text="Calculate", command=lambda: calculate(day1_var, month1_var, year1_var, day2_var, month2_var, year2_var))
bttn_calculate.place(x=5, y=90, width=110)

title2 = ttk.Label(root, text="Is It A Leap Year?", style="Title.TLabel", foreground="darkred")
title2.place(x=5, y=165)

lbl3 = ttk.Label(root, text="Select:")
lbl3.place(x=5, y=200)

year3_var = tk.IntVar()
year3_var.set("")
year3 = ttk.Combobox(root, textvariable=year3_var, values=years)
year3.place(x=45, y=200, width=55)

result2_lbl = ttk.Label(root, text="Result:")
result2_lbl.place(x=5, y=235)

res2 = tk.StringVar()
res2.set("")
result2 = ttk.Label(root, textvariable=res2)
result2.place(x=45, y=235)

bttn_leapyear = ttk.Button(root, text="Calculate", command=lambda: is_leap_year(year3_var.get(), res2))
bttn_leapyear.place(x=105, y=198, width=125)

lbl3_style = ttk.Style()
lbl3_style.configure("LBL3.TLabel", font=("Snap ITC", 9))
lbl3 = ttk.Label(root, text="by Batuhan Akçan", style="LBL3.TLabel")
lbl3.place(x=105, y=275)



root.mainloop()