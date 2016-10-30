##########
# library
##########
import pandas as pd
import nltk
import simplejson as json
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
import numpy as np
from nltk.util import ngrams

###################################################################################################
# The data is downloaded by datacollect tool, website : https://github.com/rasbt/datacollect
#####################################################################################################

#################################################################
# Put this script along with song lyrics files in the same folder and run
# Task : tokenize, unigram, bigram, POS tag, frequency calculate, type token ratio 
##################################################################

## import csv file
input60s=pd.read_csv("1960s_song_lyrics.csv", index_col=0, sep=",")
input70s=pd.read_csv("1970s_song_lyrics.csv", index_col=0, sep=",")
input80s=pd.read_csv("1980s_song_lyrics.csv", index_col=0, sep=",")
input90s=pd.read_csv("1990s_song_lyrics.csv", index_col=0, sep=",")
input00s=pd.read_csv("2000s_song_lyrics.csv", index_col=0, sep=",")
input10s=pd.read_csv("2010s_song_lyrics.csv", index_col=0, sep=",")
input60s['Year']="1960s"
input70s['Year']="1970s"
input80s['Year']="1980s"
input90s['Year']="1990s"
input00s['Year']="2000s"
input10s['Year']="2010s"
df=[input60s,input70s,input80s,input90s,input00s,input10s]
dfnew=pd.concat(df, ignore_index=True)
# Replace lyrics annotation and delete redundant white space, a basic dataset is built 
dfnew["Lyrics"]=dfnew["Lyrics"].replace(to_replace="[\[A-Z][0-9]\]", value="",regex=True)
dfnew["Lyrics"]=dfnew["Lyrics"].replace(to_replace="]", value="",regex=True)
dfnew["Lyrics"]=dfnew["Lyrics"].replace(to_replace=".",value="")
dfnew["Lyrics"]=dfnew["Lyrics"].replace(to_replace=" ",value="")
# NLTK tokenization by white space, create some columns for putting data, question mark and exclamation are treated as tokens 
# "." and ";" or ":" is deleted  
##############
# Unigram section
#############
dfnew["Unigram"]="NaN"
Unigram_dict=dict()
dfnew["Unigram_length"]=0
#############
# POS section
############
dfnew["POS"]="NaN"
POS_dict=dict()
POS_Frequency=dict()
#################
# Bigram section
#################
dfnew["Bigram"]="NaN"
Bigram_dict=dict()
########################
tokenizer = RegexpTokenizer("\S+")

for i in range(len(dfnew)):
  dfnew["Lyrics"].iloc[i]=dfnew["Lyrics"].iloc[i].replace("?"," ?").replace("!"," !").replace(","," ,").replace(")"," )").replace("("," (")
  dfnew["Lyrics"].iloc[i]=dfnew["Lyrics"].iloc[i].lower()
  tokens= tokenizer.tokenize(dfnew["Lyrics"].iloc[i])
  mybigrams=list(ngrams(tokens,2))
  dfnew["Unigram_length"].iloc[i]=len(tokens)
  Unigram_dict[i]=tokens
  Bigram_dict[i]=mybigrams
  POS_dict[i]=nltk.pos_tag(tokens)
  
    
## put this dictionary back to data frame 
for i in range(len(Unigram_dict)):
  dfnew["Unigram"].iloc[i]=Unigram_dict[i]
  dfnew["Bigram"].iloc[i]=Bigram_dict[i]
  dfnew["POS"].iloc[i]=POS_dict[i]

for i in range(len(POS_dict)):
  tag= nltk.FreqDist(tag for (word, tag) in POS_dict[i])
  POS_Frequency[i]=tag
  
pos_frequency=pd.DataFrame.from_dict(POS_Frequency)
pos_frequency_transpose=pd.DataFrame.transpose(pos_frequency)
pos_frequency_transpose=pos_frequency_transpose.fillna(0)
## combine frequency table to dfnew
df_with_POS=[dfnew,pos_frequency_transpose]
dfnew_two=pd.concat(df_with_POS, axis=1)

######## if want to calculate the propotion of each tag in each data 
dfnew_propo=dfnew_two.ix[:,8:].div(dfnew_two["Unigram_length"],axis=0)
## I save this to another file, in case I need it in the future 

## save data 
dfnew_two.to_csv("combined_song_with_POS.csv")
dfnew_two_propo.to_csv("POS_propotion_to_song_length.csv")



  
