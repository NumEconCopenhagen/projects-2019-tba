####DATA PROJECT####

###Data Cleaning and Structuring###
## Set up
import pandas as pd
import numpy as np
import pandas_datareader
import datetime
from pandas_datareader import wb

##Downloand Data from the Wold Data Bank 
countries = ["CN","JP","BR","US","DK","ES","TM","IN","NG"]
indicators = {"NY.GDP.PCAP.KD":"GDP per capita", "NY.GDP.MKTP.CD":"GDP(current US $)", "SP.POP.TOTL":"Population total", 
              "SP.URB.TOTL.IN.ZS":"Urban Population in %", "SP.DYN.TFRT.IN":"Fertility Rate", "SE.ADT.LITR.ZS": "Literacy rate, adult total in %" }
data_wb = wb.download(indicator= indicators, country= countries, start=1990, end=2017)
data_wb = data_wb.rename(columns = {"NY.GDP.PCAP.KD":"gdp_pC","NY.GDP.MKTP.CD":"gdp", "SP.POP.TOTL":"pop", "SP.URB.TOTL.IN.ZS":"urban_pop%", 
                                    "SP.DYN.TFRT.IN":"frt", "SE.ADT.LITR.ZS":"litr"})
data_wb = data_wb.reset_index()
data_wb.head(-5)             

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
data_wb.to_excel(r"./data_wb1.xlsx")

##Overview of the data 
data_wb.dtypes

pd.options.display.float_format = '{:,}'.format

round(data_wb.head(),2)

data_wb['gdp_in_bil'] = data_wb['gdp']/1000000000

round(data_wb.head(),2) 

del data_wb['gdp'] #drop old variable for gdp
round(data_wb.head(),2)

data_wb.shape

round(data_wb.describe(),2)

##Detect missing data 
data_wb.isnull().sum().sum()
data_wb.count()
data_wb.isnull().sum()
data_wb.drop(['litr'], axis = 1, inplace = True)
round(data_wb.groupby('year').mean(),2)
round(data_wb.loc[data_wb['year'] == "2017", :].head(-1),2)
I = data_wb['year'] == "2017"
data_wb.drop(data_wb[I].index, inplace = True)

##Cleaned data set 
round(data_wb.describe(),2)
data_wb.shape
data_wb.count()

###Data Analysis and Visualisations###
round(data_wb.groupby('country').mean(),2)

##Interative plot 
import matplotlib.pyplot as plt
%matplotlib inline 
from ipywidgets import interact, interactive, fixed, interact_manual 
import ipywidgets as widgets 

country=data_wb["country"]
year=data_wb["year"]
gdp_pC=data_wb["gdp_pC"]

def interactive_figure(country, data_wb):
    data_country = data_wb[data_wb.country == country]
    year = data_country.year
    gdp_pC = data_country.gdp_pC
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(1,1,1)
    ax.plot(year, gdp_pC)
    ax.set_xlabel("Years")
    ax.set_ylabel("GDP per Capita")
    plt.xticks(rotation=90)
    plt.gca().invert_xaxis()

widgets.interact(interactive_figure,
    year = widgets.fixed(year),
    data_wb = widgets.fixed(data_wb),
    country=widgets.Dropdown(description="Country", options=data_wb.country.unique()),
    gdp_pC=widgets.fixed(gdp_pC)
);

##World map 
import folium
data_wb.groupby('country').mean()

row_indexes=data_wb[data_wb['country']== 'Brazil'].index
data_wb.loc[row_indexes,'Lat']= -14.2350
data_wb.loc[row_indexes,'Lon']= -51.9253

row_indexes=data_wb[data_wb['country']== 'China'].index
data_wb.loc[row_indexes,'Lat']= 33.5449
data_wb.loc[row_indexes,'Lon']= 103.149

row_indexes=data_wb[data_wb['country']== 'Denmark'].index
data_wb.loc[row_indexes,'Lat']= 56.2639
data_wb.loc[row_indexes,'Lon']= 9.5018

row_indexes=data_wb[data_wb['country']== 'Spain'].index
data_wb.loc[row_indexes,'Lat']= 40.4637
data_wb.loc[row_indexes,'Lon']= -3.7492

row_indexes=data_wb[data_wb['country']== 'India'].index
data_wb.loc[row_indexes,'Lat']= 20.5937
data_wb.loc[row_indexes,'Lon']= 78.9629

row_indexes=data_wb[data_wb['country']== 'Japan'].index
data_wb.loc[row_indexes,'Lat']= 36.2048
data_wb.loc[row_indexes,'Lon']= 138.2529

row_indexes=data_wb[data_wb['country']== 'Nigeria'].index
data_wb.loc[row_indexes,'Lat']= 9.0820
data_wb.loc[row_indexes,'Lon']= 8.6753

row_indexes=data_wb[data_wb['country']== 'Turkmenistan'].index
data_wb.loc[row_indexes,'Lat']= 38.9697
data_wb.loc[row_indexes,'Lon']= 59.5563

row_indexes=data_wb[data_wb['country']== 'United States'].index
data_wb.loc[row_indexes,'Lat']= 37.0902
data_wb.loc[row_indexes,'Lon']= -95.7129

round(data_wb,2)

# Make an empty map
map = folium.Map(location=[0,0], tiles="Mapbox Bright", zoom_start=2)
#converted_value = getattr(value, "tolist", lambda x=value: x)()

selectedyear = 2010 #Select your preferred year
selectedvariable = 'gdp_pC' #select yout preferred variable

year_overview = data_wb.loc[data_wb['year']== str(selectedyear)] #selectedyear for a dropdown with used year
year_overview

# Make an empty map
map = folium.Map(location=[0,0], tiles="Mapbox Bright", zoom_start=2)
#converted_value = getattr(value, "tolist", lambda x=value: x)()


# I can add marker one by one on the map
for i in range(0,len(year_overview)):
    folium.Circle(
        location=[year_overview.iloc[i]['Lat'], year_overview.iloc[i]['Lon']],
        #popup=locations2016_gdp_pC.iloc[i]['country'],
        radius=year_overview.iloc[i][selectedvariable]*10, #the smaller the original number, the higher the radius should be chosen
        color='green',
        fill=True
    ).add_to(map)


map

#saving in a file
map.save('./map.py')
data_wb.drop(['Lat','Lon'], axis = 1, inplace = True)

#Fertility rate per country 
ax = data_wb.groupby('country').frt.mean().plot(kind='bar')
ax.set_ylabel('Avg. annual fertility rate')

def annual_growth(x): 
    x_last    = x.values[-1]
    x_first   = x.values[0]
    num_years = len(x)
    
    growth_annualized = (x_last/x_first)**(1/num_years) - 1.0
    return growth_annualized

ax = data_wb.groupby('country')['frt'].agg(annual_growth).plot(kind='bar')
ax.set_ylabel('Annual growth (fertility rate) from first to last year'); 

data_wb.dtypes
data_wb['year'] = data_wb.year.astype(float)
data_wb.dtypes

##Fertility rate per country from 1990 until 2016
data_wb = data_wb.set_index(["year", "country"])

#plot fertility rate over the years
data_wb.unstack('country')['frt'].plot()

##Correlation Table 
import seaborn as sns
fig = plt.subplots(figsize = (10,10))
sns.set(font_scale=1.5)
sns.heatmap(data_wb.corr(),square = True,cbar=True,annot=True,annot_kws={'size': 10})
plt.show()


##Regression: 
