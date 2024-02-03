#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df2012=pd.read_excel("2012.xlsx")


# In[3]:


df2012=df2012[['Sector', 'Sub Sector ', 'Organization', 'Operation', 'Operation Type',
       'Address', 'City', 'Postal Code', 'Total Floor Area ', 'Average Hours per week', 'Annual Flow ', 'Electricity',
         'Natural Gas', 'Fuel Oil 1 & 2', 'Fuel Oil 4 &6',  'Propane',  'Coal Quantity', 'Wood','Renewable', 
        'Renewable Emission Factor','DistrictCooling_Quantity','DistrictHeating_Quantity',
              'GHG Emissions KG','Energy Intensity ekWh_sqft']]


# In[4]:


len(df2012.columns)


# In[5]:


df2012["Year"]=2012


# In[105]:


df2013=pd.read_excel("2013.xlsx",header=2)


# In[106]:


columns=['Sector', 'Sub Sector ', 'Organization', 'Operation', 'Operation Type',
       'Address', 'City', 'Postal Code', 'Total Floor Area ', 'Average Hours per week', 'Annual Flow ', 'Electricity',
         'Natural Gas', 'Fuel Oil 1 & 2', 'Fuel Oil 4 &6',  'Propane',  'Coal Quantity', 'Wood','Renewable', 
        'Renewable Emission Factor','DistrictCooling_Quantity','DistrictHeating_Quantity',
              'GHG Emissions KG','Energy Intensity ekWh_sqft']
df2013 = df2013.reindex(columns=columns)


# In[107]:


len(df2013.columns)


# In[108]:


df2013['Year']=2013


# In[10]:


df2014=pd.read_excel("2014.xlsx",header=2)


# In[11]:


df2014 = df2014.reindex(columns=columns)


# In[12]:


df2014['Year']=2014


# In[13]:


len(df2014.columns)


# In[14]:


df2015=pd.read_excel("2015.xlsx",header=2)


# In[15]:


df2015 = df2015.reindex(columns=columns)


# In[16]:


df2015['Year']=2015


# In[17]:


len(df2015.columns)


# In[18]:


df2016=pd.read_excel("2016.xlsx")


# In[19]:


df2016 = df2016.reindex(columns=columns)


# In[20]:


df2016['Year']=2016


# In[21]:


len(df2016.columns)


# In[22]:


df2017=pd.read_excel("2017.xlsx")


# In[23]:


df2017 = df2017.reindex(columns=columns)


# In[24]:


df2017['Year']=2017


# In[25]:


len(df2017.columns)


# In[97]:


df2018=pd.read_excel("2018.xlsx")


# In[98]:


df2018 = df2018.reindex(columns=columns)


# In[99]:


df2018['Year']=2018


# In[100]:


len(df2018.columns)


# In[30]:


df2019=pd.read_excel("2019.xlsx")


# In[31]:


df2019 = df2019.reindex(columns=columns)


# In[32]:


df2019['Year']=2019


# In[33]:


len(df2019.columns)


# In[101]:


df2020=pd.read_excel("2020.xlsx")


# In[102]:


df2020 = df2020.reindex(columns=columns)


# In[103]:


df2020['Year']=2020


# In[104]:


len(df2020.columns)


# In[38]:


df2021=pd.read_excel("2021.xlsx")


# In[39]:


import numpy as np
df2021["Fuel Oil1"].replace('Not Available', 0, inplace=True)


# In[40]:


df2021["Fuel Oil2"].replace('Not Available', 0, inplace=True)


# In[41]:


a=[]
for i,j in zip (df2021["Fuel Oil1"],df2021["Fuel Oil2"]):
    c=int(i)+int(j)
    a.append(c)


# In[42]:


df2021["Fuel Oil 1 & 2"]=a


# In[43]:


df2021["Fuel Oil6"].replace('Not Available', 0, inplace=True)


# In[44]:


df2021["Fuel Oil4"].replace('Not Available', 0, inplace=True)


# In[45]:


b=[]
for i,j in zip (df2021["Fuel Oil4"],df2021["Fuel Oil6"]):
    c=int(i)+int(j)
    b.append(c)


# In[46]:


df2021["Fuel Oil 4 &6"]=b


# In[47]:


df2021 = df2021.reindex(columns=columns)


# In[48]:


df2021['Year']=2021


# In[49]:


len(df2021.columns)


# In[109]:


df=pd.concat([df2012,df2013,df2014,df2015,df2016,df2017,df2018,df2019,df2020,df2021])


# In[110]:


csv_file_path = r"C:\Users\babyk\OneDrive\Documents\projects\career fair 1\pro.csv"
df.to_csv(csv_file_path, index=False)


# In[168]:


import pandas as pd
df=pd.read_csv("pro.csv")


# In[169]:


len(df)


# In[170]:


df.head(2)


# In[171]:


import numpy as np
df.replace('Not Available', np.nan, inplace=True)


# In[172]:


(df.isnull().sum()/len(df))*100


# In[173]:


df = df.drop(["Sub Sector ","Renewable","Renewable Emission Factor"], axis=1)


# In[184]:


(df.isnull().sum()/len(df))*100


# In[176]:


tfa=df.groupby(['Sector']).agg({'Total Floor Area ':"mean"},index=0)


# In[178]:


tfa['Total Floor Area '].median()


# In[179]:


print(df['Total Floor Area '].dtype)
print(tfa['Total Floor Area '].dtype)


# In[180]:


df['Total Floor Area '] = pd.to_numeric(df['Total Floor Area '], errors='coerce')


# In[181]:


df['Total Floor Area '] = df['Total Floor Area '].fillna(tfa['Total Floor Area '].median())


# In[182]:


print(df['Total Floor Area '].isnull().any())


# In[198]:


df['Total Floor Area '] = df['Total Floor Area '].fillna(tfa['Total Floor Area '].reindex(df.index))


# In[199]:


af=df.groupby("Sector").agg({"Annual Flow ":"mean"})


# In[200]:


af["Annual Flow "].median()


# In[201]:


df["Annual Flow "]=df["Annual Flow "].fillna(af["Annual Flow "].median())


# In[202]:


df["Operation"]=df["Operation"].fillna(df["Operation"].mode().iloc[0])


# In[203]:


df['Address']=df['Address'].fillna(df['Address'].mode().iloc[0])


# In[204]:


df['City']=df['City'].fillna(df['City'].mode().iloc[0])


# In[187]:


df['Postal Code']=df['Postal Code'].fillna(df['Postal Code'].mode().iloc[0])


# In[188]:


import seaborn as sns
sns.distplot(df['Electricity'])


# In[189]:


# Assuming 'Column_Name' is the name of the column you want to change the data type
df['Electricity']= df['Electricity'].astype('float')


# In[190]:


ele=df.groupby('Sector').agg({'Electricity': 'median'})


# In[217]:


sns.distplot(ele['Electricity'])
mean_val = ele["Electricity"].mean()
median_val = ele["Electricity"].median()
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_val:.2f}')


# In[192]:


df['Electricity']=df['Electricity'].fillna(ele['Electricity'].median())


# In[193]:


sns.distplot(df['Average Hours per week'])


# In[194]:


ah=df.groupby("Sector").agg({"Average Hours per week":"mean"})


# In[216]:


sns.distplot(ah["Average Hours per week"])
mean_val = ah["Average Hours per week"].mean()
median_val = ah["Average Hours per week"].median()
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_val:.2f}')


# In[196]:


df['Average Hours per week']=df['Average Hours per week'].fillna(ah['Average Hours per week'].mean())


# In[207]:


sns.distplot(df['Natural Gas'])


# In[209]:


df['Natural Gas']=df['Natural Gas'].astype('float')


# In[211]:


ng=df.groupby("Sector").agg({"Natural Gas":"median"})


# In[215]:


import matplotlib.pyplot as plt
sns.distplot(ng["Natural Gas"], kde=True)
mean_val = ng["Natural Gas"].mean()
median_val = ng["Natural Gas"].median()
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_val:.2f}')
plt.legend()
plt.show()


# In[218]:


df["Natural Gas"]=df['Natural Gas'].fillna(ng["Natural Gas"].mean())


# In[224]:


fo1=df.groupby("Sector").agg({"Fuel Oil 1 & 2":"mean"})


# In[227]:


sns.distplot(fo1["Fuel Oil 1 & 2"])
mean_val = fo1["Fuel Oil 1 & 2"].mean()
median_val = fo1["Fuel Oil 1 & 2"].median()
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_val:.2f}')


# In[228]:


df['Fuel Oil 1 & 2']=df['Fuel Oil 1 & 2'].fillna(fo1["Fuel Oil 1 & 2"].median())


# In[229]:


fo4=df.groupby("Sector").agg({"Fuel Oil 4 &6":"mean"})


# In[232]:


df['Fuel Oil 4 &6']=df['Fuel Oil 4 &6'].fillna(fo4["Fuel Oil 4 &6"].median())


# In[289]:


(df.isnull().sum()/len(df))*100


# In[237]:


df['Propane']=df["Propane"].astype("float")


# In[239]:


p=df.groupby("Sector").agg({"Propane":"mean"})


# In[240]:


df['Propane']=df["Propane"].fillna(p['Propane'].mean())


# In[245]:


df['Coal Quantity'] = pd.to_numeric(df['Coal Quantity'], errors='coerce')
df['Coal Quantity']=df["Coal Quantity"].astype("float")


# In[246]:


cq=df.groupby("Sector").agg({"Coal Quantity":"mean"})


# In[247]:


sns.distplot(cq["Coal Quantity"])


# In[248]:


df['Coal Quantity']=df["Coal Quantity"].fillna(cq['Coal Quantity'].mean())


# In[253]:


df['Wood'] = pd.to_numeric(df['Wood'], errors='coerce')
df['Wood']=df['Wood'].astype("float")


# In[255]:


w=df.groupby('Sector').agg({'Wood':"mean"})


# In[256]:


sns.distplot(w['Wood'])


# In[257]:


df['Wood']=df['Wood'].fillna(w['Wood'].median())


# In[262]:


ei=df.groupby("Sector").agg({'Energy Intensity ekWh_sqft':"median"})


# In[263]:


df["Energy Intensity ekWh_sqft"]=df["Energy Intensity ekWh_sqft"].fillna(ei['Energy Intensity ekWh_sqft'].mean())


# In[277]:


dh=df.groupby("Sector").agg({'DistrictHeating_Quantity':"mean"})


# In[278]:


df['DistrictHeating_Quantity']=df['DistrictHeating_Quantity'].fillna(dh['DistrictHeating_Quantity'].mean())


# In[279]:


dc=df.groupby("Sector").agg({'DistrictCooling_Quantity':"mean"})


# In[282]:


df['DistrictCooling_Quantity']=df['DistrictCooling_Quantity'].fillna(dc['DistrictCooling_Quantity'].mean())


# In[288]:


df['GHG Emissions KG']=df['GHG Emissions KG'].fillna(df['GHG Emissions KG'].median())


# In[290]:


csv_file_path = r"C:\Users\babyk\OneDrive\Documents\projects\career fair 1\pro_clean.csv"
df.to_csv(csv_file_path, index=False)


# In[2]:


import pandas as pd
df1=pd.read_csv("pro_clean.csv")


# In[3]:


df1.head(2)


# In[5]:


import matplotlib.pyplot as plt
plt.scatter(df1['Average Hours per week'], df1['GHG Emissions KG'])
plt.xlabel('Average Hours per week')
plt.ylabel('GHG Emissions KG')
plt.title('Relationship')
plt.show()
#there's  no relationship between Average Hours per week and GHG Emissions KG


# In[6]:


mean= df1.groupby("Year")["GHG Emissions KG"].mean().reset_index()
plt.plot(mean["Year"],mean["GHG Emissions KG"])
plt.xlabel("YEAR")
plt.ylabel("Greenhouse gas emmision")
# GHG is very high in 2013


# In[ ]:


top_sectors = df1.groupby("Sector")["GHG Emissions KG"].sum().nlargest(10).index
filtered_df = df1[df1["Sector"].isin(top_sectors)]

plt.bar(filtered_df["Sector"], filtered_df["GHG Emissions KG"], color='skyblue')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




