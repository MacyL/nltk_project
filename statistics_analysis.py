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
>>> import statsmodels.api as sm
>>> from statsmodels.formula.api import ols
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
###################
# Task2 : calculate Type-Token-ratio
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

temp=dfnew_two[["Year","TTR"]]
summary_dict[0].update({"TTR":temp[temp["Year"]=="1960s"].describe().ix[1,0]})
summary_dict[1].update({"TTR":temp[temp["Year"]=="1970s"].describe().ix[1,0]})
summary_dict[2].update({"TTR":temp[temp["Year"]=="1980s"].describe().ix[1,0]})
summary_dict[3].update({"TTR":temp[temp["Year"]=="1990s"].describe().ix[1,0]})
summary_dict[4].update({"TTR":temp[temp["Year"]=="2000s"].describe().ix[1,0]})
summary_dict[5].update({"TTR":temp[temp["Year"]=="2010s"].describe().ix[1,0]})
####################
# Task3 : Anova to teat length, POS counts among years  
# Annoying thing : can't find a efficient way to do this, so go for stupid way. 
#####################
newtemp=dfnew_two.ix[:,3:]
column_name=newtemp.columns.values.tolist()
column_name=column_name[4:]
anova_dict=dict()
# this code is not working.....
#for i in column_name:
#  phrase=''.join('"'+i+"~"+"Year"+'"')
#  mod=ols(''.join('"'+i+"~"+"Year"+'"'), data=newtemp).fit()
mod=ols("Unigram_length~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["Unigram_length"]=F_test
## and the rest is the same, I don't put it here.
# save for futher investigation 
np.save("anova_object.npy",anova_dict)
# data frame 
anova_p_value=data
for i in anova_dict.keys():
  thetemp=anova_dict[i].ix[1,3]
  anova_p_value[i]=thetemp

anova_table.DataFrame.from_dict(anova_p_value)
####################
#Task4 : visualize some major POS tags by year
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


##### repeated code 
mod=ols("CC~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["CC"]=F_test
mod=ols("CD~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["CD"]=F_test
mod=ols("DT~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["DT"]=F_test
mod=ols("EX~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["EX"]=F_test
mod=ols("FW~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["FW"]=F_test
mod=ols("IN~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["IN"]=F_test
mod=ols("JJ~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["JJ"]=F_test
mod=ols("JJR~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["JJR"]=F_test
mod=ols("JJS~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["JJS"]=F_test
mod=ols("MD~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["MD"]=F_test
mod=ols("NN~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["NN"]=F_test
mod=ols("NNP~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["NNP"]=F_test
mod=ols("NNPS~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["NNPS"]=F_test
mod=ols("NNS~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["NNS"]=F_test
mod=ols("PDT~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["PDT"]=F_test
mod=ols("PRP~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["PRP"]=F_test
mod=ols("PRP$~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["PRP$"]=F_test
mod=ols("RB~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["RB"]=F_test
mod=ols("RBR~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["RBR"]=F_test
mod=ols("RP~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["RP"]=F_test
mod=ols("SYM~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["SYM"]=F_test
mod=ols("TO~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["TO"]=F_test
mod=ols("UH~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["UH"]=F_test
mod=ols("VB~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VB"]=F_test
mod=ols("VBD~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VBD"]=F_test
mod=ols("VBG~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VBG"]=F_test
mod=ols("VBN~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VBN"]=F_test
mod=ols("VBP~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VBP"]=F_test
mod=ols("VBZ~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["VBZ"]=F_test
mod=ols("WDT~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["WDT"]=F_test
mod=ols("WP~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["WP"]=F_test
mod=ols("WRB~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["WRB"]=F_test
mod=ols("TTR~Year",data=newtemp).fit()
F_test=sm.stats.anova_lm(mod, typ=3)
anova_dict["TTR"]=F_test
