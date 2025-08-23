import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ## identify valida tweets
    tweets["CharNum"] = tweets["content"].apply(lambda x: len(str(x)))
    tweets["validation"] = tweets["CharNum"].apply(lambda x: x <= 15)

    valid_id = tweets.query("validation == False")

    return pd.DataFrame({
        "tweet_id": valid_id.tweet_id.to_list()
    })
