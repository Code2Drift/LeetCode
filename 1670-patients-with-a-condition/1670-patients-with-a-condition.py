import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    ## split conditions params
    patients["cond_splits"] = patients["conditions"].apply(lambda x: x.split())
    
    ## validate diabetes conditions
    patients["diabets"] = patients["cond_splits"].apply(
        lambda x: any(cond.lower().startswith("diab1") for cond in x)
    )
    diabetes_df = patients.query("diabets == True")
    print(patients)
        
    return diabetes_df[["patient_id", "patient_name", "conditions"]]