# Setup
import pandas as pd
import numpy as np

#setup to download data directly from the databank
import pandas_datareader
import datetime

#setup to download data directly from world data bank
from pandas_datareader import wb

#define countries we are looking for
countries = ["CN","JP","BR","US","DK","ES","TM","IN","NG"]

#define indicator
indicators = {"NY.GDP.PCAP.KD":"GDP per capita", "NY.GDP.MKTP.CD":"GDP(current US $)", "SP.POP.TOTL":"Population total", 
              "SP.URB.TOTL.IN.ZS":"Urban Population in %", "SP.DYN.TFRT.IN":"Fertility Rate", "SE.ADT.LITR.ZS": "Literacy rate, adult total in %" }


#example download world data bank shown in the lecture
data_wb = wb.download(indicator= indicators, country= countries, start=1990, end=2017)
data_wb = data_wb.rename(columns = {"NY.GDP.PCAP.KD":"gdp pC","NY.GDP.MKTP.CD":"gdp", "SP.POP.TOTL":"pop", "SP.URB.TOTL.IN.ZS":"urban_pop%", 
                                    "SP.DYN.TFRT.IN":"frt", "SE.ADT.LITR.ZS":"litr"})
data_wb = data_wb.reset_index()
data_wb.head(-5)

# save datasheet as excel (just to see it)_index=false to avoid saving the index
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
data_wb.to_excel(r"C:\Users\Lisa1\Desktop\MarieDokumente\Uni\Master\VWL\Phython Introduction\project_1\data_wb.xlsx")

data_wb.shape

#summary statistics
data_wb.describe()

# detect for missing data
## count missing data
data_wb.isnull().sum().sum()

## number of observations
data_wb.count()

## missing value of each variable
data_wb.isnull().sum()

# drop litr
data_wb.drop(['litr'], axis = 1, inplace = True)

#search for the nine missing values in frt
data_wb.groupby('year').mean()

#show frt only for 2017
data_wb.loc[data_wb['year'] == "2017", :].head(-1)

# drop the year for which the data is missing 
I = data_wb['year'] == "2017"
data_wb.drop(data_wb[I].index, inplace = True)
# => data cleaning done


#summary statistics
data_wb.describe()

data_wb.shape

data_wb.count()
#=>data cleaning finished

# make some cool groupby things see lecture basic_data
##empl.groupby('municipality')['e'].mean().head(10)
##empl.groupby('year')['e'].mean().plot
# demean to compare it better
##stocks2.groupby('firm')['close_demeaned'].plot(legend=True); 
##plt.title('Stock price: deviation from time-average'); 
# perform summary statistics
## nameofdataset.describe()
# maybe create an interactive table for each country
##see load_save_and_structure_data
#correlation table?
# maybe perform a simple regression
# world maps as diagramm
