import pandas as pd

# 1. ... by using a dictionary of lists.
dict_lists = {
    "Employee": ["John Doe", "Jane Smith", "Michael Roberts", "Emily Davis", "Chris Green", "Jessica Wilson", "Daniel Kim", "Sophia Martinez"],
    "Monthly Salary ($)": [5200, 4800, 5000, 5300, 4600, 4950, 5100, 4700]
}
df1 = pd.DataFrame(dict_lists)
print(df1)

# 2. ... by using a list of dictionaries.
# dict_lists = [
#    {"Employee": "John Doe", "Monthly Salary ($)": 5200},
#    {"Employee": "Jane Smith", "Monthly Salary ($)": 4800},
#    {"Employee": "Michael Roberts", "Monthly Salary ($)": 5000},
#    {"Employee": "Emily Davis", "Monthly Salary ($)": 5300},
#    {"Employee": "Chris Green", "Monthly Salary ($)": 4600},
#    {"Employee": "Jessica Wilson", "Monthly Salary ($)": 4950},
#    {"Employee": "Daniel Kim", "Monthly Salary ($)": 5100},
#    {"Employee": "Sophia Martinez", "Monthly Salary ($)": 4700}
# ]
# df2 = pd.DataFrame(dict_lists)
# print(df2)

# 3. ... by using  a dictionary of pandas Series (named names and monthly_salary).
# names = pd.Series(["John Doe", "Jane Smith", "Michael Roberts", "Emily Davis", "Chris Green", "Jessica Wilson", "Daniel Kim", "Sophia Martinez"], name="Employee")
# monthly_salary = pd.Series([5200, 4800, 5000, 5300, 4600, 4950, 5100, 4700], name="Monthly Salary ($)")
# dict_lists = {
#    "Employee": names,
#    "Monthly Salary ($)": monthly_salary
# }
# df3 = pd.DataFrame(dict_lists)
# print(df3)

# 4. ... by using a list of lists.
# dict_lists = [
#    ["John Doe", 5200],
#    ["Jane Smith", 4800],
#    ["Michael Roberts", 5000],
#    ["Emily Davis", 5300],
#    ["Chris Green", 4600],
#    ["Jessica Wilson", 4950],
#    ["Daniel Kim", 5100],
#    ["Sophia Martinez", 4700]
# ]
# df4 = pd.DataFrame(dict_lists, columns=["Employee", "Monthly Salary ($)"])
# print(df4)
