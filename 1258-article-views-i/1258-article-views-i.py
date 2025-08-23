import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    ## identify of self view authors
    views["same_person"] = views["author_id"] == views["viewer_id"]
    df_self_views = views.query("same_person == True")
    author_list = list(df_self_views.author_id.unique())

    return pd.DataFrame({
        "id":sorted(author_list)
    })
        