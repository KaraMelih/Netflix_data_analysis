import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

x = 5

myname = 'Melih'

movies = df[df['type']=='Movie']  
tvseries = df[df['type']=='TV Show']
