import matplotlib
matplotlib.use('Agg')
from pandas import *
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_std = data.std()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_std,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	df1 = DataFrame( data = {"Index":list(range(249)),"Current":df['Current fleet'].dropna().tolist()})
	df1.columns = ["Index", "Current fleet"]

	#print df.columns
	
	data = df1.values.T[1]
	boots = []
	boot = boostrap(np.std, 100000, data)
	for i in range(100000):
		boots.append([i,boot[0], "Standard Deviation "])
		boots.append([i,boot[1], "lower"])
		boots.append([i,boot[2], "upper"])



	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Standard Deviation',"Value"])
	sns_plot = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")




	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,100000)

	sns_plot.savefig("bootstrap_confidence_Vehicles_Current.png",bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_Vehicles_Current.pdf",bbox_inches='tight')

	
	
	#New Fleet
	
	df2 = DataFrame( data = {"Index":list(range(79)),"New":df['New Fleet'].dropna().tolist()})
	df2.columns = ["Index", "New Fleet"]

	#print df.columns
	
	data = df2.values.T[1]
	boots = []
	boot = boostrap(np.std, 100000, data)
	for i in range(100000):
		boots.append([i,boot[0], "Standard Deviation "])
		boots.append([i,boot[1], "lower"])
		boots.append([i,boot[2], "upper"])



	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Standard Deviation',"Value"])
	sns_plot = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")




	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,100000)

	sns_plot.savefig("bootstrap_confidence_Vehicles_New.png",bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_Vehicles_New.pdf",bbox_inches='tight')



	