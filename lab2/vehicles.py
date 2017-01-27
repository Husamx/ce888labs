import matplotlib
matplotlib.use('Agg')
from pandas import *
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
		
	df1 = DataFrame( data = {"Index":list(range(249)),"Current":df['Current fleet'].dropna().tolist()})
	df1.columns = ["Index", "Current fleet"]

	sns_plot = sns.lmplot(df1.columns[1], df1.columns[0], data=df1, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot_Vehicles_current.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot_Vehicles_current.pdf",bbox_inches='tight')

	##Now print new fleet
	df1 = DataFrame( data = {"Index":list(range(79)),"New":df['New Fleet'].dropna().tolist()})
	df1.columns = ["Index", "New Fleet"]

	sns_plot = sns.lmplot(df1.columns[1], df1.columns[0], data=df1, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot_Vehicles_new.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot_Vehicles_new.pdf",bbox_inches='tight')
	

	
