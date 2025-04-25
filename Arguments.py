salaries_dict = {
    "John Doe": 5200,
    "Jane Smith": 4800,
    "Michael Roberts": 5000,
    "Emily Davis": 5300,
    "Chris Green": 4600,
    "Jessica Wilson": 4950,
    "Daniel Kim": 5100,
    "Sophia Martinez": 4700
}

import pandas as pd

# 1. Convert the salaries_dict dictionary into a pandas Series called
# monthly_salaries_usd_series. Name the Series "Monthly Salaries ($)".
monthly_salaries_usd_series = pd.Series(salaries_dict)
monthly_salaries_usd_series.name = "Monthly Salaries ($)"

# 2. Display the content of monthly_salaries_usd_series.
print(monthly_salaries_usd_series)

# 3. Use a pandas method to obtain the highest salary value stored in the Series.
print(monthly_salaries_usd_series.max())

# 4. Use a pandas method to retrieve the name of the person with the lowest
# monthly salary.
print(monthly_salaries_usd_series.idxmin())

# 5. Use a pandas method to display the top five rows from the Series.
print(monthly_salaries_usd_series.head())

# 6. Use a pandas method to display the last three rows from the Series.
print(monthly_salaries_usd_series.tail(3))
