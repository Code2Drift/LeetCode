import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    final_df = pd.DataFrame()

    ## conditions if df is/are empty
    if employee.empty or department.empty:
        return pd.DataFrame(columns=["Department", "Salary", "Employee"])


    ## merge tables
    df_merge = employee.merge(
        department, left_on="departmentId", right_on="id", how="left"
    )

    df_merge.rename(
        columns={
            "name_y":"Department",
            "salary":"Salary",
            "name_x":"Employee"
        }, inplace=True
    )

    ## check salary based on department groups
    depart_list = df_merge["Department"].unique()

    for depart in depart_list:
        max_salary = df_merge.loc[df_merge["Department"] == depart, "Salary"].max()
        print(max_salary)
        find_maxSalary = df_merge.loc[(df_merge["Salary"] == max_salary) & (df_merge["Department"] == depart)]
        final_df = pd.concat([final_df, find_maxSalary], ignore_index=False)
    
    final_df.drop_duplicates(inplace=True, keep="last")

    return final_df[["Department", "Employee", "Salary"]]


