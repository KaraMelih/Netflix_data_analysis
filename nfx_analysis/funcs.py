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

# construct it such that the same function can also be used for searching data from other columns like look_in='director'
def find_actors_movies(df,actor_name, look_in='cast'):
    """
    Finds the 'title's of the movies/series where
    actor_name plays in it
    Arguments
    --------
    df         : pandas.DataFrame
          the data frame to use
    actor_name : str
          Name of the actor
    look_in    : str
          Where to look for the actor
    
    Returns
    -------
    data frame containing only the movies that the actor is in
    """
    # drop NaN values
    series_filt = df.dropna(subset=[look_in])
    actor_movies = series_filt[series_filt[look_in].str.contains(actor_name)]
    return actor_movies


def chart_it(df,feature='listed_in',threshold=100,ax=None):
    '''
    plot pie chart of given features of a given frame
    Arguments
    ---------
    df         : pandas.DataFrame
          the data frame to use
    feature    : str, optional (default:listed_in)
          which features to plot
    ax         : matplotlib.pyplot.axes, optional
          which axis to plot
    
    Returns
    -------
    None. Plots a pie chart
    '''
    d = get_lengths(df['listed_in'], threshold=threshold)
    ax = ax or plt.gca()
    ax.pie(d.values(),labels=d.keys(), autopct="%1.1f%%");
    
    
    
    
    
    
    
    
    
    