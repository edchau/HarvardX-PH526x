#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 20:56:40 2018

@author: Edward
"""

text = "This is my test text. We're keeping this text short to keep things manageable."


def count_words(text):
    """
    Counts the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. Skips punctuations
    """
    text = text.lower()
    word_counts = {}
    skips = [".", "," ,";" ,":", "'", '"']
    
    for ch in skips:
        text = text.replace(ch, "")
    for word in text.split(" "):
        if word in word_counts:
            #known word
            word_counts[word] += 1
        else:
            #unknown word
            word_counts[word] = 1
            
    return word_counts


from collections import Counter

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

print(count_words(text)==count_words_fast(text))
print(count_words(text) is count_words_fast(text))


#reading a book

def read_book(title_path):
    """
    Read a book and return it as a string
    """
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
print(len(text))
ind = text.find("What's in a name?")
sample_text = text[ind : ind + 1000]


#Comparing translations of books

def word_stats(word_counts):
    """
    Return number of unique words and word frequencies
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))

text = read_book("./Books/German/shakespeare/Romeo und Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))


#Reading multiple files
import os
book_dir = "./Books"
print(os.listdir(book_dir))
            

#Using Pandas to create a dataframe:
import pandas as pd

#table = pd.DataFrame(columns = ("name", "age"))
#table.loc[1] = "James", 22
#table.loc[2] = "Jess", 32
#print(table)

stats = pd.DataFrame(columns = ("Language" , "Director" , "Title" , "Length" , "Unique"))
#empty data frame with 5 columns
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language , author.capitalize(), title.replace(".txt", "") , sum(counts) , num_unique
            title_num += 1
            
print(stats.head()) #top 5 lines
print(stats.tail()) #bottom 5 lines
print(stats[stats.Language == "English"])


#Plotting Book Statistics
import matplotlib.pyplot as plt
plt.plot(stats.Length, stats.Unique, "bo")

plt.figure(figsize = (10,10))
subset = stats[stats.Language == "English"]
plt.loglog(subset.Length, subset.Unique, "o", label = "English", color = "crimson") 

subset = stats[stats.Language == "French"]
plt.loglog(subset.Length, subset.Unique, "o", label = "French", color = "forestgreen")
 
subset = stats[stats.Language == "German"]
plt.loglog(subset.Length, subset.Unique, "o", label = "German", color = "orange") 

subset = stats[stats.Language == "Portuguese"]
plt.loglog(subset.Length, subset.Unique, "o", label = "Portuguese", color = "blueviolet")

plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of Unique Words")
plt.savefig("lang_plot.pdf")