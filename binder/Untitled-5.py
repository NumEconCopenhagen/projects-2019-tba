u#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dataproject\dataproject\Dataproject_Marie'))
	print(os.getcwd())
except:
	pass

#%%
# Setup
import pandas as pd
import numpy as np


#%%
#setup to download data directly from the databank
import pandas_datareader
import datetime


#%%
#setup to download data directly from world data bank
from pandas_datareader import wb


#%%
#define countries we are looking for
countries = ["CN","JP","BR","US","DK","ES","TM","IN","NG"]


#%%
#define indicator
indicators = {"NY.GDP.PCAP.KD":"GDP per capita", "NY.GDP.MKTP.CD":"GDP(current US $)", "SP.POP.TOTL":"Population total", 
              "SP.URB.TOTL.IN.ZS":"Urban Population in %", "SP.DYN.TFRT.IN":"Fertility Rate", "SE.ADT.LITR.ZS": "Literacy rate, adult total in %"}


#%%
#example download world data bank shown in the lecture
data_wb = wb.download(indicator= indicators, country= countries, start=1990, end=2017)
data_wb = data_wb.rename(columns = {"NY.GDP.PCAP.KD":"gdp_pC","NY.GDP.MKTP.CD":"gdp", "SP.POP.TOTL":"pop", "SP.URB.TOTL.IN.ZS":"urban_pop%", 
                                    "SP.DYN.TFRT.IN":"frt", "SE.ADT.LITR.ZS":"litr"})
data_wb = data_wb.reset_index()
data_wb.head(-5)


#%%
# save datasheet as excel (just to see it)_index=false to avoid saving the index
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
data_wb.to_excel(r"C:\Users\Lisa1\Desktop\MarieDokumente\Uni\Master\VWL\Phython Introduction\project_1\data_wb.xlsx")


#%%
data_wb.shape


#%%
#summary statistics
data_wb.describe()


#%%
# detect for missing data
## count missing data
data_wb.isnull().sum().sum()


#%%
## number of observations
data_wb.count()


#%%
## missing value of each variable
data_wb.isnull().sum()


#%%
# drop litr
data_wb.drop(['litr'], axis = 1, inplace = True)


#%%
#search for the nine missing values in frt
data_wb.groupby('year').mean()


#%%
#show frt only for 2017
data_wb.loc[data_wb['year'] == "2017", :].head(-1)


#%%
# drop the year for which the data is missing 
I = data_wb['year'] == "2017"
data_wb.drop(data_wb[I].index, inplace = True)
# => data cleaning done


#%%
#summary statistics
data_wb.describe()


#%%
data_wb.shape


#%%
data_wb.count()
#=>data cleaning finished


#%%
#Marie: groupby country
data_wb.groupby('country').mean()

##overview shows countries with a high gdp per capita have a low fertility rate. countries with a high gdp per capita have a huge 
##share of urban population


#%%
#Marie: Import 
import matplotlib.pyplot as plt


#%%
I = data_wb['year'] == 2015
data_wb.groupby(['country',I]).unstack("frt").plot(kind = "bar")


#%%
#Achtung später kommt index
I = data_wb['year'] == 2015
data_wb['diff_frt'] = data_wb.groupby('country').frt.diff(1)
data_wb.groupby(['country',I]).diff_frt.median().unstack().plot(kind = "bar")


#%%
data_wb.unstack('country')['frt'].plot(ax = ax)


#%%
#Marie: check whether year is a integer or string
type("year")


#%%
year = float(year)


#%%
# plot

data_wb.groupby('country')['frt'].plot(x='year',y='frt',legend=True)


#%%
data_wb = data_wb.set_index(['year', 'country'])


#%%
fig, ax = plt.subplots()
data_wb.unstack('country')['frt'].plot()


#%%
data_wb.unstack('country')['frt'].plot()
plt.xticks(data_wb["year"].values)
plt.show()


#%%
fig, ax = plt.subplots()
data_wb.unstack('country')['frt'].plot(ax = ax)           


#%%
data_wb = data_wb.reset_index().set_index('year')
data_wb.groupby('country')['frt'].plot(legend=True)


#%%
fig, ax = plt.subplots()
ax.set_xticks(data_wb.year.unique())
data_wb.groupby(["year", "country"]).mean()['frt'].unstack().plot(ax=ax) 


#%%
data_wb.columns.values


#%%
data_wb = data_wb.rename(columns={'Number ': 'Number'})


#%%
type("year")                                         


#%%
data_wb.groupby('country')['frt'].plot(x= "year", y= "frt",legend=True)


#%%
#Marie: plot countries
fig,ax = plt.subplots()
data_wb.groupby('country')['frt'].plot(x='year',y=None,legend=True);


#%%
fig, ax = plt.subplots()
# use unstack()
data_wb.groupby(['year','frt']).plot(legend= True)


#%%
data_wb.groupby('country')['year'].plot(kind='bar')
plt.show()


#%%
#Marie


#%%



#%%
#Marie
import seaborn as sns; sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris)


#%%
#Marie
# effects by countries 
I = data_wb['year'] == 2015
data_wb['diff_frt'] = data_wb.groupby('country').frt.diff(1)
data_wb.groupby(['country',I]).diff_frt.median().unstack().plot(kind='bar');


#%%
I = data_wb['year'] == 2015
data_wb['diff_frt'] = data_wb.groupby('country').frt.diff(1)
data_wb.groupby(['country',I]).diff_frt.median().unstack().plot(kind='bar')


#%%
#Marie
# effects by countries 
I = data_wb['year'] == 2015
data_wb['diff_frt'] = data_wb.groupby('country').frt.diff(1)
data_wb.groupby(['country',I]).diff_frt.median().unstack().plot(kind='bar');


#%%
# nachkomma stellen ändern
# make some cool groupby things see lecture basic_data

##empl.groupby('municipality')['e'].mean().head(10)
##empl.groupby('year')['e'].mean().plot

# maybe create an interactive table for each country
##see load_save_and_structure_data
#correlation table?
# maybe perform a simple regression
# world maps as diagramm

#Task jepe
##data cleaning and structuring
##data anbalysis
##structure a code
##document the code
##results in graphs an figures

##minimum data online source
##virtual and interactive
##methods of descripitve economics->TA


#%%
#correlation table 


#%%
import seaborn as sns


#%%
ax = data_wb.groupby('country').frt.mean().plot(kind='bar')
ax.set_ylabel('Avg. annual fertility rate')


#%%
def annual_growth(x): 
    x_last    = x.values[-1]
    x_first   = x.values[0]
    num_years = len(x)
    
    growth_annualized = (x_last/x_first)**(1/num_years) - 1.0
    return growth_annualized

ax = data_wb.groupby('country')['frt'].agg(annual_growth).plot(kind='bar')
ax.set_ylabel('Annual growth (fertility rate) from first to last year'); 


