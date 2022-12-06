import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def datetime_type(df,date):
    ''' datetime_type takes in a dataframe and a ready date columne and reassigns the date to the datetime type
    returns df'''
    # save into dataframe
    df[date] = pd.to_datetime(df[date])
    return df

def distribution( df, var):
    ''' distribution takes in a dataframe and variable and returns a histoplot 
    that  display the distirbution of the variable'''
    # use histplot
    sns.histplot(df[var])
    #show plot
    plt.show();


def set_date_to_index(df, date):
    ''' set_date_to_index takes in a dataframe and string date and set the index of data frame to the index
    returns altered data frame'''
    # Sort rows by the date and then set the index as that date
    df = df.set_index(date).sort_index()
    return df

def add_date_column_string(df,column_name, string='%B'):
    ''' add_date_column takes in a df:data frame and a time frame method run_method: defaulted to %B  month_name()
    and returns a dataframe wiht a new column,'''
    # save into data frame
    df[column_name]=df.index.strftime(string)
    
    return df

def multiply_columns_addto_df(df, column_name, var1, var2):
    ''' multiply_columns_addto_df takes in a dataframe and multiplies two of its variables and sa
    returs'''
    # save into data frame
    df[column_name]= df[var1]* df[var2]
    return df

def fillna(df):
    '''fill na takes in a dataframe and fill in the nans/nulls'''
    # fill in nulls
    df.fillna(0, inplace=True)
    return df