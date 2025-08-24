import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    list_salary = sorted(employee["salary"].unique(), reverse=True)

    ## if N longer than salary list
    if N > len(list_salary):
        return pd.DataFrame({
            f"getNthHighestSalary({N})": [None]
        })

    ## negative N - invalid input
    elif N < 0:
        return pd.DataFrame({
            f"getNthHighestSalary({N})": [None]
        })
    
    ## N is zero
    elif N == 0:
        return pd.DataFrame({
            f"getNthHighestSalary({N})": [None]
        }) 

    else:
        return pd.DataFrame({
            f"getNthHighestSalary({N})": [list_salary[N-1]]
        }) 

