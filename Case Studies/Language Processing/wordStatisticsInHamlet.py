#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:38:22 2018

@author: Edward
"""

#Case Study 2 - Word Frequency Distribution in Hamlet
#In this case study, we will find and plot the distribution of word 
#frequencies for each translation of Hamlet. Perhaps the distribution 
#of word frequencies of Hamlet depends on the translation --- let's find out!

from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def count_words_fast(text):
    """
    Counts the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. Skips punctuations
    """
    text = text.lower()
    skips = [".", "," ,";" ,":", "'", '"']
    
    for ch in skips:
        text = text.replace(ch, "")
   
    word_counts = Counter(text.split(" "))
            
    return word_counts

def read_book(title_path):
    """
    Read a book and return it as a string
    """
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    """
    Return number of unique words and word frequencies
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


#Exercise 1
#Find translations of Hamlet and create Pandas dataframe
hamlets = pd.DataFrame(columns = ("language" , "text"))
book_dir = "Books"
title_num = 1

#book_titles is a nested dictionary, containing book titles 
#within authors within languages, all of which are strings.
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1
#There are three translations: English, German, and Portuguese.


#Exercise 2
#Summarize text for single translation of Hamlet
language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)
data = pd.DataFrame({"word": list(counted_text.keys()), 
                     "count": list(counted_text.values())})


#Exercise 3
#Continue to define summary statistics for a single translation of Hamlet.

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

#Exercise 4
#Summarize statistics into smaller pandas dataframe

sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    

    
#Exercise 5
#Join all the data summaries for text Hamlet translation.

def summarize_text(language, text):
    counted_text = count_words_fast(text)
    
    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)

grouped_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])

for index in range(hamlets.shape[0]):
    language, text = hamlets.iloc[index]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
    
    
    
#Exercise 6
#Plot results and look for differences across each translation
colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}

for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )
color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left", prop={'size': 6})

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.title("Hamlet Word Statistics")
plt.show()