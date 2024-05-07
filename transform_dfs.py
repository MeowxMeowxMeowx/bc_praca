import pandas as pd 
import numpy as np
from stop_deleter import del_stopwords_df
import nltk
from nltk.corpus import stopwords


if __name__ == "__main__":
    df_train = pd.read_json("dataset/train.jsonl",lines=True)[["comment","rating_int"]]
    df_validate = pd.read_json("dataset/validation.jsonl",lines=True)[["comment","rating_int"]]
    df_test = pd.read_json("dataset/test.jsonl",lines=True)[["comment","rating_int"]]
    
    nltk.download('stopwords')
    stop=set(stopwords.words('slovak'))

    tmp = del_stopwords_df(df_test,stop,0)
    df_test["comment"] = tmp
    df_test.to_csv("test_nostop_lower.csv")

    tmp = del_stopwords_df(df_train,stop,0)
    df_train["comment"] = tmp
    df_train.to_csv("train_nostop_lower.csv")


    tmp = del_stopwords_df(df_validate,stop,0)
    df_validate["comment"] = tmp
    df_train.to_csv("validate_nostop_lower.csv")

