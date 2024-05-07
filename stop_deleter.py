import pandas as pd


def del_stopwords_df(df, stop_list,col_i):
    text = df.iloc[:,col_i].str.lower()
    slovak_alphabet = "a,á,ä,b,c,č,d,ď,dz,dž,e,é,f,g,h,ch,i,í,j,k,l,ĺ,ľ,m,n,ň,o,ó,ô,p,q,r,ŕ,s,š,t,ť,u,ú,v,w,x,y,ý,z,ž"
    alphabet_list = slovak_alphabet.split(",")
    text = text.apply(del_non_alphabet,alphabet_list=alphabet_list)
    text = text.apply(del_stop_words,stop=stop_list)
    return text

def del_stop_words(x,stop):
    word_list = x.split(" ")
    ret_list = [word for word in word_list if word not in stop]
    return " ".join(ret_list)

def del_non_alphabet(x,alphabet_list):
    ret_str = ""
    for ch in x:
        if ch == " " or ch in alphabet_list:
            ret_str+=ch
    return ret_str