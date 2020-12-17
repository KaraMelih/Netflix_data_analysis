import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_lengths(df, plot=False, ax=None, threshold=0):
    """
    Get the number of arguments in a given dataframe
    
    Argument
    --------
    df      :  pandas.DataFrame
        input data
        
    plot    : bool
        whether or not to plot the data
    ax      : matplotlib ax object
        axes to draw on
    
    Return
    ------
    
    dict : python dictionary
         the lenght of the data
    """
    unstr_list = [i.split(',') for i in list(df.dropna())]
    cleaned_list = [country.strip() for countrylist in unstr_list for country in countrylist]
    
    mydict = {}
    for e in cleaned_list:
        if e not in mydict:
            mydict[e] = 1
        else: mydict[e] += 1

    mynew_dict = {key:val for (key,val) in mydict.items() if val > threshold}
            
    if plot:
        ax1 = ax or plt.gca()
        ax1.barh(list(mynew_dict.keys()),  list(mynew_dict.values()))
        ax1.set_xlabel('number of content') 

    return mynew_dict