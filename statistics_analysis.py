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
#Task1 : summary 
##################
dataset_summary=dfnew_two.describe()
dataset_summary.to_csv("data_summary.csv")
##################
###################
# Type-Token-ratio
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
