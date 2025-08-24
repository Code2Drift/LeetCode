import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    list_salary = sorted(employee["salary"].unique(), reverse=False)

    ## if N larger than salary list
    if len(list_salary) <= 1:
        return pd.DataFrame({
            "SecondHighestSalary": [None]
        })
    
    elif len(list_salary) == 2:
        return pd.DataFrame({
            "SecondHighestSalary": [list_salary[0]]
        })

    elif len(list_salary) > 2:
        return pd.DataFrame({
            "SecondHighestSalary": [list_salary[-2]]
        })