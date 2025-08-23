import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    
    ## validate requirements
    employees["even"] = employees["employee_id"].apply(lambda x: x % 2 != 0)
    employees["start"] = employees["name"].apply(lambda x: not x.lower().startswith("m"))

    ## generate bonus calculation, if both condition is true
    employees["bonus"] = employees.apply(
        lambda row: row["salary"] if row["even"] and row["start"] else 0,
        axis=1 # specify axis
    )

    return employees[["employee_id", "bonus"]].sort_values(
        by="employee_id", ascending=True
    )

