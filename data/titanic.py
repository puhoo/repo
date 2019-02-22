#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_src='titanic.csv'
df = pd.read_csv(data_src, header=0)
print df.info()
print df.describe()
print df.head()
survived_rate = float(df['Survived'].sum())/df['Survived'].count()
print "survived_rate = ", survived_rate
x=[df[(df.Sex=='male')]['Sex'].size,df[(df.Sex=='female')]['Sex'].size]
y=[df[(df.Sex=='male')&(df.Survived==1)]['Sex'].size, df[(df.Sex=='female')&(df.Survived==1)]['Sex'].size]
print "male number = " + str(x[0]) + "   " + "survived number = " + str(y[0]) + "   " + "survived rate = " + str(float(y[0])/float(x[0]))
print "female number = " + str(x[1]) + "   " + "survived number = " + str(y[1]) + "   " + "survived rate = " + str(float(y[1])/float(x[1]))
sex_survived_rate = (df.groupby(['Sex']).sum() / df.groupby(['Sex']).count())['Survived']
sex_survived_rate.plot(kind='bar')
plt.savefig('titanic.png')
plt.show
