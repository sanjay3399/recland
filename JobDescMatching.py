# coding: utf-8
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from docx import Document
from RAKE import rake
import unicodedata
import csv
import pandas as pd
import itertools
import numpy as np
from tabulate import tabulate
import os
import pdb

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def convertFormat(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

def cosine_sim(text1, text2):
    try:
        vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
        tfidf = vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0,1]
    except Exception as e:
        return 0

def getText(filename):
    # pdb.set_trace()
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def joinElemenets(items):
    return ' '.join(items)

def getKeywords(text):
    rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
    return rake_object.run(text)

def Match(filename, k):
    cwd = os.getcwd() + "/data/jobs/"
    jobs = os.listdir("data/jobs")
    JDlist = {}
    for j in jobs:
        text = convertFormat(getText(cwd + j))
        text = getKeywords(text)
        JD = ' '.join(zip(*text)[0])
        JDlist[j.split('.')[0]] = JD

    PD = ""
    if filename.split('.')[1] == 'txt': 
        profile = open(filename)
        PD = profile.read()
    elif filename.split('.')[1] == 'docx':
        PD = convertFormat(getText(filename))

    sims = map(cosine_sim, JDlist.values(), itertools.repeat(PD, len(JDlist)))
    sims = np.array(sims)
    top_jobs = sims.argsort()[-k:][::-1]

    pdb.set_trace()
    recommendations = []
    for index, job in enumerate(top_jobs):
        PD = convertFormat(getText(cwd + str(JDlist.keys()[job]) + '.docx'))
        print "RECOMMENDATION # " + str(index+1)
        print "\n---------------------------------------\n", PD, "\n---------------------------------------\n"

if __name__ == '__main__':
    Match(raw_input("Enter path for profile (Supported formats: .docx, .txt): "), 3)
