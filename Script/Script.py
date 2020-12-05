import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


if __name__=="__main__":
	os.makedirs('image',exist_ok=True)
	farmer = pd.read_csv('data/Kishan_call.csv')
	df =farmer.groupby(['QueryType']).count()
	
	plt.figure(figsize=(12,10))
	plt.bar(df.index,df['DistrictName'])
	plt.xlabel('Query Type',size=16)
	plt.title('Query asked by farmers of Goa on National helpline Number',size=16)
	plt.ylabel('Number of Queries',size=16)
	plt.savefig('image/Bar_plt.png')
	
	
	Energy = pd.read_csv('data/Energy_consumption.csv')
	endf = Energy.groupby(['Region']).mean()
	cont = ['Africa', 'Asia Pacific', 'CIS', 'Europe', 'Middle East',
	       'North America', 'S. & Cent. America']
	endif = pd.DataFrame(endf,index =cont ).mean(axis=1)
	
	plt.figure(figsize=(12,12))
	plt.pie(endif,labels=cont,autopct='%1.1f%%')
	plt.title('Energy consumption share in 2018',size=16)
	plt.savefig('image/pie_plot.png')
	
	
	tendif = endf.T
	
	plt.figure(figsize=(8,8))
	plt.boxplot((tendif['CIS'],tendif['Middle East']),labels = ['CIS','Middle East'])
	plt.title('Energy Consumption of CIS and Middle East during 2012-2018',size=14)
	plt.xlabel('Continents',size=14)
	plt.ylabel('energy consumed (Milloin tons oil equivalent)',size=14)
	plt.savefig('image/Box-plot1.png')
	
	plt.figure(figsize=(8,8))
	plt.boxplot((tendif['Africa'],tendif['Europe']),labels = ['Africa','Europe'])
	plt.title('energy consumption of Africa and Europe during 2012-2018',size=14)
	plt.xlabel('Continents',size=14)
	plt.ylabel('energy consumed (Milloin tons oil equivalent)',size=14)
	plt.savefig('image/Box-plot2.png')
	
	
	road = pd.read_csv('data/Road_Accidents_2017-Annexure_ Tables_1.csv')
	plt.figure(figsize=(10,10))
	plt.scatter(road['Years'][3:-1],road['Total Number of Road Accidents (in numbers)'][3:-1],marker = '^',label='Accidents',s=128)
	plt.scatter(road['Years'][3:-1],road['Total Number of Persons Killed (in numbers)'][3:-1],marker = 'o',label='persons Died',s=128)
	plt.scatter(road['Years'][3:-1],road['Total Number of Persons Injured (in numbers)'][3:-1],marker='*',label='persons Injured',s=128)
	plt.xlabel('Year',size=16)
	plt.ylabel('Number of person',size=16)
	plt.title('Road Accidents in India ',size=14)
	plt.grid()
	plt.xticks(road['Years'][3:-1],rotation=30)
	plt.legend()
	plt.savefig('image/scatter_plot.png')


