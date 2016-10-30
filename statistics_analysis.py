##########
# library
##########
import pandas as pd
import nltk
import simplejson as json
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
import numpy as np
# for plots 
import matplotlib as mpl 
import matplotlib.pyplot as plt
#statistical module 
from scipy import stats
##################
# Task : Try to find the differences among various decades
# Anova to compare the length of songs, POS counts, Type-Token ratio, the noun that has been using
#################
#################
#Task1 : summary by year : number of songs,length of song and standard deviation
##################

summary_1960s=dfnew_two[dfnew_two["Year"]=="1960s"].describe()
summary_1970s=dfnew_two[dfnew_two["Year"]=="1970s"].describe()
summary_1980s=dfnew_two[dfnew_two["Year"]=="1980s"].describe()
summary_1990s=dfnew_two[dfnew_two["Year"]=="1990s"].describe()
summary_2000s=dfnew_two[dfnew_two["Year"]=="2000s"].describe()
summary_2010s=dfnew_two[dfnew_two["Year"]=="2010s"].describe()
summary_dict=dict()
summary_dict[0]={"Year":"1960s","Song_Numbers":summary_1960s.ix[0,0],"Average_Lyrics_Length":summary_1960s.ix[1,0],"Sd":summary_1960s.ix[2,0]}
summary_dict[1]={"Year":"1970s","Song_Numbers":summary_1970s.ix[0,0],"Average_Lyrics_Length":summary_1970s.ix[1,0],"Sd":summary_1970s.ix[2,0]}
summary_dict[2]={"Year":"1980s","Song_Numbers":summary_1980s.ix[0,0],"Average_Lyrics_Length":summary_1980s.ix[1,0],"Sd":summary_1980s.ix[2,0]}
summary_dict[3]={"Year":"1990s","Song_Numbers":summary_1990s.ix[0,0],"Average_Lyrics_Length":summary_1990s.ix[1,0],"Sd":summary_1990s.ix[2,0]}
summary_dict[4]={"Year":"2000s","Song_Numbers":summary_2000s.ix[0,0],"Average_Lyrics_Length":summary_2000s.ix[1,0],"Sd":summary_2000s.ix[2,0]}
summary_dict[5]={"Year":"2010s","Song_Numbers":summary_2010s.ix[0,0],"Average_Lyrics_Length":summary_2010s.ix[1,0],"Sd":summary_2010s.ix[2,0]}
summary_1970s.ix[[1,2],:]

################################
# super important : summary_dict is the object to store all the statistical result.
###############################
##################
###################
# Task2 : Type-Token-ratio
####################
tt_ratio_dict=dict()
for i in range(len(dfnew_two)):
  frequency=FreqDist(dfnew_two["Unigram"].iloc[i])
  type_number=len(frequency.keys())
  token_number=sum(frequency.values())
  tt_ratio=type_number/token_number
  tt_ratio_dict[i]=tt_ratio

dfnew_two["TTR"]=0  
for i in range(len(tt_ratio_dict)):
  dfnew_two["TTR"].iloc[i]=tt_ratio_dict[i]


####################
#Task3 : visualize every POS tags by year
###################
# all sorts of verb 
fig, axes = plt.subplots(nrows=2, ncols=3)
dfnew_two.boxplot(column="VB",by="Year", ax=axes[0,0])
dfnew_two.boxplot(column="VBD",by="Year", ax=axes[0,1])
dfnew_two.boxplot(column="VBG",by="Year", ax=axes[0,2])
dfnew_two.boxplot(column="VBN",by="Year", ax=axes[1,0])
dfnew_two.boxplot(column="VBP",by="Year", ax=axes[1,1])
dfnew_two.boxplot(column="VBZ",by="Year", ax=axes[1,2])
fig.show()

# all sorts of noun
fig, axes = plt.subplots(nrows=2, ncols=2)
dfnew_two.boxplot(column="NN",by="Year", ax=axes[0,0])
dfnew_two.boxplot(column="NNP",by="Year", ax=axes[0,1])
dfnew_two.boxplot(column="NNS",by="Year", ax=axes[1,0])
fig.show()

gs = gridspec.GridSpec(3, 3)
ax1 = fig.add_subplot(gs[0,:])
ax1=dfnew_two.boxplot(column="NN", by="Year")
gs.update(wspace=0.5, hspace=0.5)
