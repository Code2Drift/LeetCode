import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    ## merge customer and order tables
    merged_tab = customers.merge(
        orders, left_on="id", right_on="customerId", how="left"
    ) 

    ## no order
    final_df = merged_tab[merged_tab["id_y"].isna()][["name"]]
    
    final_df.rename(columns={"name":"Customers"}, inplace=True)

    return final_df

