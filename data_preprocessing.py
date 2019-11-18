
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
#/*#matplotlib inline means that any graph we create, will appear in the same notebook file*/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import statistics
import seaborn as sns #styling plots
import difflib
from scipy import stats
from scipy.stats import mode

#/*Create dataframe, dataframe is tabular structure in python*/
df=pd.read_csv ("C:\\Users\\Saurabh Minotra\\OneDrive - Dalhousie University\\MEC\\Fall_2019\\Visual Analytics\\Assignment1\\CSCI6612 - Visual Analytics (Sec 1) - 2019 Fall - 9132019 - 1234 PM\\dataset1_dirty.csv")
#https://www.udemy.com/data-science-and-machine-learning-with-python-hands-on


# In[2]:

#Create the histogram for the columns with data type integer
#Create the barchart for the columns with data type object
#
sns.set()
def create_graphs():
    plot.figure(figsize=(20,10))
    for i, columns in enumerate(df.columns):
        plot.figure(figsize=(20,10))
        a = df[df.columns[i]].dtypes.name
        if a=='int64':
            print('Histogram:',i+1,'for', columns,'with data type',a)
            sns.distplot(df[columns])
            plot.show()
        else:
            plot.figure(figsize=(20,10))
            sns.countplot(x = (df[columns]), data = df) 
            print('Bar:',i+1,'for', columns,'with data type',a)
#https://seaborn.pydata.org/tutorial/distributions.html


# In[3]:

create_graphs()


# In[4]:

#Check outliers for the column
def detect_outliers():
    for i, columns in enumerate(df.columns):
        a = df[df.columns[i]].dtypes.name
        if a=='int64':
            u = np.median(df[columns])
            s = np.std(df[columns])
            filtered = [e for e in (df[columns]) if (u - 2 * s < e < u + 2 * s)]
            print([df.columns[i]], "-",u - 2 * s,u + 2 * s)
            sns.boxplot(df[columns])
            plot.show()
        else:
            print('.') 


# In[5]:

detect_outliers()


# In[6]:

df=df[df['age']>0]


# In[7]:

df.describe()


# In[8]:

#Initializing local variables
#Making a list of expected values and storing it in a list
workclass_def_val=['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
workclass_def_val
list3 = workclass_def_val
#https://www.programiz.com/python-programming/list


# In[9]:

##list 2 contains the unique value of the categories and list 3 contains the expected values. 

df_wk_all_values = []
a = df.workclass.unique()
list2 = []
for i in range(0,len(a)):
    list2.append(a[i])
print(list2)


# In[10]:

#iteration is done to find the close match 

df.workclass.unique()
key=dict()
for i in range(len(list2)):
    for j in range(len(list3)):
        sequence =difflib.SequenceMatcher(isjunk=None,a=list2[i] ,b=list3[j])
        difference=sequence.ratio()
        if (difference >0.89):
            key[list2[i]]=list3[j]
            print(list2[i], ' | ', list3[j])

#https://www.programiz.com/python-programming/list
#https://docs.python.org/3/tutorial/datastructures.html
#https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict
#https://docs.python.org/3/library/difflib.html


# In[11]:

key


# In[12]:

df['workclass'] = df['workclass'].map(key)


# In[13]:

df['workclass'].unique()


# In[14]:

df['workclass'].isnull().sum()
#check null values for the column


# In[15]:

#replace the null values with others
df.workclass.replace({np.nan:'Others'},inplace=True)


# In[16]:

df['workclass'].isnull().sum()


# In[17]:

#List to get the occupation unique values
df.occupation.unique()
df_wk_all_values = []
a = df.occupation.unique()
list4 = []
for i in range(0,len(a)):
    list4.append(a[i])
print(list4)


# In[18]:

##list 4 contains the unique value of the categories and list 5 contains the expected values. 

workclass_def_val=['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
'Handlers-cleaners', 'Machine-op-inspct',
'Adm-clerical', 'Farming-fishing',
'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
workclass_def_val
list5 = workclass_def_val
print(list5)


# In[19]:

key=dict()
for i in range(len(list4)):
    for j in range(len(list5)):
        sequence =difflib.SequenceMatcher(isjunk=None,a=list4[i] ,b=list5[j])
        difference=sequence.ratio()
        if (difference > 0.89):    
            key[list4[i]]=list5[j]
            print(list4[i], ' | ', list5[j])


# In[20]:

key
df['occupation'] = df['occupation'].map(key)


# In[21]:

df.occupation.replace({np.nan:'Others'},inplace=True)


# In[22]:

df['workclass'].unique()


# In[23]:

for i in df['education'].unique(): 
    print(i,df[df['education']==i]['education-num'].value_counts().index[0])
    df.loc[df['education'] == i,'education-num'] = df[df['education']==i]['education-num'].value_counts().index[0]
    print("done",df[df['education']==i]['education-num'].value_counts().index[0])
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
#https://www.geeksforgeeks.org/python-pandas-series-value_counts/
#https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas


# In[24]:

df=df.drop(['capital-gain', 'capital-loss'], axis=1)


# In[25]:

create_graphs()


# In[27]:

df.to_csv('./dataset1_processed.csv',index=False)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



