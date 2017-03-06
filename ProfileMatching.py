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
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def joinElemenets(items):
    return ' '.join(items)

def getKeywords(text):
    rake_object = rake.Rake("RAKE/SmartStoplist.txt", 3, 3, 1)
    return rake_object.run(text)

def printProfile(profile):
    print profile['Name']
    print profile['Title']
    print profile['Location']
    print profile['Experience']
    print profile['Pay rate']
    print profile['Last Updated']
    print profile['Relocate']
    print profile['Previous Title'], "\n"

text = convertFormat(getText("data/SampleJD.docx"))
text = getKeywords(text)
JD = ' '.join(zip(*text)[0])

PD = pd.read_csv('data/DataMiner-PD-filled.csv')
PD.loc[PD["Pay rate"].isnull(),'Pay rate'] = "negotiable | negotiable"
PD.loc[PD["Previous title"].isnull(),'Previous title'] = "N/A"

PDlist = map(joinElemenets, PD.values.tolist())
sims = map(cosine_sim, PDlist, itertools.repeat(JD, len(PDlist)))

sims = np.array(sims)
topCandidates = sims.argsort()[-10:][::-1]

print tabulate(PD.ix[topCandidates,:], headers='keys', tablefmt='psql')