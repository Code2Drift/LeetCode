import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    final_df = pd.DataFrame()

    ## conditions if df is/are empty
    if employee.empty or department.empty:
        return pd.DataFrame(columns=["Department", "Salary", "Employee"])


    ## merge tables
    df_merge = employee.merge(
        department, left_on="departmentId", right_on="id", how="left"
    ).rename(
        columns={"name_y": "Department", "salary": "Salary", "name_x": "Employee"}
    )

    ## check salary based on department groups
    max_per_dept = df_merge.groupby("Department")["Salary"].transform("max")
    final_df = df_merge.loc[df_merge["Salary"] == max_per_dept]
    
    final_df.drop_duplicates(inplace=True, keep="last")

    return final_df[["Department", "Employee", "Salary"]].reset_index(drop=True)


