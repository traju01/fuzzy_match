import pandas as pd
import os
import streamlit as st

st.title("Fuzzy Match Program")
uploaded_file = st.file_uploader("Upload the file you want Fuzzy Matched: ", type=['xlsx', 'xls'])
#df = pd.read_excel(uploaded_file)
uploaded_file_2 = st.file_uploader("Upload the dictionary file: ", type=['xlsx', 'xls'])
#df2 = pd.read_excel(uploaded_file_2)

fuzzy_column = st.text_input("Enter the column name you want matched from the fuzzy matched file: ")
#fuzzy_column=fuzzy_column.strip()
matched_column = st.text_input("Enter the column name you want to match with from the dictionary file: ")
#matched_column=matched_column.strip()
lookup_column = st.text_input("Enter the column name you want to append from the dictionary file: ")
#lookup_column=lookup_column.strip()


def find_match (word, word_from_dict):
    
    initial_score=0
    word=''.join(filter(str.isalnum,word))
    word_from_dict=''.join(filter(str.isalnum,word_from_dict))

    word=word.lower()
    word_from_dict=word_from_dict.lower()
    
    word=word.strip()
    word_from_dict=word_from_dict.strip()
    
    word_length = len(word)
    dict_word_length = len(word_from_dict)
    
    length=word_length
    a=0
    x=0
    count=0
    new_score=0
    initial_score=0
    while length>0:
        #print(word)
        #print(word, word_from_dict,x,a, word_length)
        if a>=word_length:
            length=0
        elif word[a]==word_from_dict[x] and a<word_length:
            count=count+1
            length=length-1
            #print(a, word[a], length, x, word_from_dict[x])
            x=x+1
            a=a+1
            #print(count)
        elif word[a]!=word_from_dict[x] and count>0 and x<dict_word_length:
            length=0
        elif word[a]!=word_from_dict[x] and count==0 and x<dict_word_length:
            #print(a, word[a], length, x, word_from_dict[x])
            x=x+1
        if x==dict_word_length:
            x=0
            a=a+1
    
    initial_score = count/word_length
        
    initial_count = count
    #print(initial_score)
    if initial_score < 0.9:
        #print("round two")
        length = dict_word_length
        a=0
        x=0
        count=0
        while length>0:
            #print(a)
            if word[a]==word_from_dict[x] and x<dict_word_length :
                count=count+1
                length=length-1
                #print(a, word[a], length, x, word_from_dict[x])
                x=x+1
                a=a+1
            elif word[a]!=word_from_dict[x] and count>0 and x<dict_word_length:
                length=0
            elif word[a]!=word_from_dict[x] and count==0 and x<dict_word_length:
                #print(a, word[a], length, x, word_from_dict[x])
                a=a+1
            if a==word_length:
                a=0
                x=x+1
            if x>=dict_word_length:
                length=0
        new_score=count/word_length
        new_count=count
    if new_score>initial_score:
        #return word, new_score, new_count, word_from_dict
        return new_score
    elif new_score<=initial_score:
        #return word, initial_score, initial_count, word_from_dict
        return initial_score

#word = input("Enter a word: ")
#word_compare = input("Enter the word you want to compare to: ")
#find_match(word, word_compare)

def find_match_round_two (word, word_from_dict):
    
    initial_score=0
    word=''.join(filter(str.isalnum,word))
    word_from_dict=''.join(filter(str.isalnum,word_from_dict))

    word=word.lower()
    word_from_dict=word_from_dict.lower()
    
    word=word.strip()
    word_from_dict=word_from_dict.strip()
    
    word_length = len(word)
    dict_word_length = len(word_from_dict)
    
    length=word_length
    a=0
    x=0
    count=0
    new_score=0
    initial_score=0
    initial_score_2=0
    new_score_2=0
    while length>0:
        #print(word)
        #print(word, word_from_dict,x,a, word_length)
        if a>=word_length:
            length=0
        elif word[a]==word_from_dict[x] and a<word_length:
            count=count+1
            length=length-1
            #print(a, word[a], length, x, word_from_dict[x])
            x=x+1
            a=a+1
            #print(count)
        elif word[a]!=word_from_dict[x] and count>0 and x<dict_word_length:
            length=0
        elif word[a]!=word_from_dict[x] and count==0 and x<dict_word_length:
            #print(a, word[a], length, x, word_from_dict[x])
            x=x+1
        if x==dict_word_length:
            x=0
            a=a+1
    
    initial_score = count/dict_word_length
    initial_score_2 = count/word_length    
    
    initial_count = count
    #print(initial_score)
    if initial_score < 0.95 and initial_score!=initial_score_2:
        #print("round two")
        length = dict_word_length
        a=0
        x=0
        count=0
        while length>0:
            #print(a)
            if word[a]==word_from_dict[x] and x<dict_word_length :
                count=count+1
                length=length-1
                #print(a, word[a], length, x, word_from_dict[x])
                x=x+1
                a=a+1
            elif word[a]!=word_from_dict[x] and count>0 and x<dict_word_length:
                length=0
            elif word[a]!=word_from_dict[x] and count==0 and x<dict_word_length:
                #print(a, word[a], length, x, word_from_dict[x])
                a=a+1
            if a==word_length:
                a=0
                x=x+1
            if x>=dict_word_length:
                length=0
        new_score=count/word_length
        new_score_2=count/dict_word_length
        new_count=count
    if new_score>initial_score and new_score==new_score_2:
        #return word, new_score, new_count, word_from_dict
        return new_score
    elif new_score<=initial_score and initial_score==initial_score_2:
        #return word, initial_score, initial_count, word_from_dict
        return initial_score
    else:
        score_backend=0.5
        return score_backend

#word = input("Enter a word: ")
#word_compare = input("Enter the word you want to compare to: ")
#find_match(word, word_compare)


def find_in_column(df, df_dict, df_column_name, df_dict_column_key_name, df_dict_column_value_name, score_threshold, score_threshold_2):
    search_size = len(df)
    dict_size = len(df_dict)
    x=0
    y=0
    df["Matched Key"]= "No Match"
    #df["Health Plan ID"]= "No Match"
    df["Lookup Value"]= "No Match"
    #print(search_size)
    while x < search_size:
        if df[df_column_name][x] is not None:
            while y < dict_size and x<search_size:
                #print(df[df_column_name][x], df_dict[df_dict_column_key_name][y])
                score=find_match(df[df_column_name][x], df_dict[df_dict_column_key_name][y])
                if score>=score_threshold:
                    df["Matched Key"][x]= df_dict[df_dict_column_key_name][y]
                    #df["Health Plan ID"][x]= df_dict[df_dict_column_value_name][y]
                    df["Lookup Value"][x]= df_dict[df_dict_column_value_name][y]
                    print(x, df_dict[df_dict_column_value_name][y])
                    x=x+1
                    y=0
                elif score < score_threshold:
                    y=y+1
            x=x+1
            y=0
            print(x)
        else:
            x=x+1
            y=0
    
    x=0
    y=0
    #df.to_csv("output_initial_match.csv")
    while x < search_size:
        if df[df_column_name][x] is not None and df["Matched Key"][x]=="No Match":
            while y < dict_size and x<search_size:
                #print(df[df_column_name][x], df_dict[df_dict_column_key_name][y])
                word_total=df[df_column_name][x]
                first_word=word_total.partition(' ')[0]
                dict_total=df_dict[df_dict_column_key_name][y]
                second_word = dict_total.partition(' ')[0]
                #print(first_word)
                if len(first_word) !=0:
                    #score=find_match_round_two(first_word, df_dict[df_dict_column_key_name][y])
                    score=find_match_round_two(first_word, second_word)
                    if score>=score_threshold_2:
                        df["Matched Key"][x]= df_dict[df_dict_column_key_name][y]
                        df["Lookup Value"][x]= df_dict[df_dict_column_value_name][y]
                        #df["Health Plan ID"][x]= df_dict[df_dict_column_value_name][y]
                        print(x, df_dict[df_dict_column_value_name][y])
                        x=x+1
                        y=0
                    elif score < score_threshold:
                        y=y+1
                else:
                    x=x+1
                    y=0
            x=x+1
            y=0
            #print(x)
        else:
            x=x+1
            y=0
    
    return df.to_csv("output_matched.csv")

#df=pd.read_excel("Health_Plan.xlsx")
#df2=pd.read_excel("mapping_formulary.xlsx")
#find_in_column(df, df2, "PAYER_NAME", "HealthPlanName", "HealthPlanID", 0.9, 0.95)
#find_in_column(df, df2, fuzzy_column, matched_column, lookup_column, 0.9, 0.95)
#new_df=df

if st.button("Submit"):
    df = pd.read_excel(uploaded_file)
    df2 = pd.read_excel(uploaded_file_2)
    df[fuzzy_column]=df[fuzzy_column].astype(str)
    df2[matched_column]=df2[matched_column].astype(str)
    df2[lookup_column]=df2[lookup_column].astype(str)
    df = df[df[fuzzy_column].notna()]
    df2 = df2[df2[matched_column].notna()]
    find_in_column(df, df2, fuzzy_column, matched_column, lookup_column, 0.9, 0.95)
    st.write("Output has been fuzzy matched: ")
    st.dataframe(df)