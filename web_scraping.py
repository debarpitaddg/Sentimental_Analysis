import nltk
import requests
from bs4 import BeautifulSoup
import numpy as np
from clartext import positive,negative,stopwords
from taking_inputs import inputs
import re

def sentimental_analysis(url,url_id):
    r=requests.get(url)

    # print(htmlcontent)--> prints all the content including tags
    soup=BeautifulSoup(r.content,'html.parser')

    #a1=soup.get_text().split(" ")
    a1=""
    for i in soup.findAll(attrs={"class" : "td-post-content"}):
        a1+=i.text
    a2=a1.split("\n")

    #a3=words with empty strings before cleaning
    a3=[]
    for i in a2:
        s=""
        if(i==""):
            continue
        for j in i:
            if((j.lower()>="a" and j.lower()<="z") or j=="-"):
                s+=j.lower()
            else:
                a3.append(s)
                s=""
        if s not in a3:
            a3.append(s)

    #a4=without empty strings and without stopwords=number of words after cleaning
    a4=[]
    for i in a3:
        if i not in stopwords:
            if i!='':
                a4.append(i)

    #positive negative counting
    positive_check=0
    negative_check=0
    for i in a4:
        if i in positive:
            positive_check+=1
        elif i in negative:
            negative_check-=1

    # a5=without empty strings= number of words
    a5 = [j for j in a3 if j != '']


    #a6=number of sentences
    fullstop=a1.split(".")
    exclamation=a1.split("!")
    question=a1.split("?")
    a6=(len(fullstop)+(len(question)-1)+(len(exclamation)-1))

    def syllable_count(word):
        word = word.lower()
        count = 0
        vowels = "aeiou"
        for i in word:
            if i in vowels:
                count+=1
            if word.endswith("ed") or word.endswith("es"):
                count-=1
        return count

    # complex word count
    complex_word=0
    for i in a5:
        if(syllable_count(i)>2):
            complex_word+=1



    #syllable iterate
    syllable_word_count=0
    for j in a5:
        syllable_word_count+=syllable_count(j)

    #personal pronouns
    pronoun=re.compile(r'\b(I|we|my|ours|our|(?-i:us))\b',re.I)
    count_pro=pronoun.findall(" ".join(a5))



    #avg word length
    charac_count=0
    for i in a5:
        charac_count+=len(i)

    #list of attributes to be put in excel

    datas= {}
    if(len(a5)==0):
        datas["PERCENTAGE OF COMPLEX WORDS"] = 0

        datas["FOG INDEX"]=(0.4*((round(len(a5)/a6))+0))

        datas["SYLLABLE PER WORD"] = 0

        # avg word length
        datas["AVG WORD LENGTH"] = 0

    else:
        # %age of complex words
        datas["PERCENTAGE OF COMPLEX WORDS"] = ((complex_word / len(a5)))
        # fog index
        datas["FOG INDEX"] = (0.4 * ((round(len(a5) / a6)) + (complex_word / len(a5))))
        # syllable count per word
        datas["SYLLABLE PER WORD"] = (round(syllable_word_count / len(a5)))
        # avg word length
        datas["AVG WORD LENGTH"] = (round(charac_count / len(a5)))


    datas["URL_ID"]=(int(url_id))
    datas["URL"]=url
    datas["POSITIVE SCORE"]=(positive_check)
    datas["NEGATIVE SCORE"]=(-1*negative_check)

    #polarity score
    datas["POLARITY SCORE"]=((positive_check - (-1*negative_check))/((positive_check +(-1*negative_check))+0.000001))

    #subj score
    datas["SUBJECTIVITY SCORE"]=((positive_check+(-1*negative_check))/(len(a4) + 0.000001))

    #avg sentence length
    datas["AVG SENTENCE LENGTH"]=(round(len(a5)/a6))



    #avg number of words per sentence
    datas["AVG NUMBER OF WORDS PER SENTENCE"]=(round(len(a5)/a6))


    #complex word count
    datas["COMPLEX WORD COUNT"]=(complex_word)

    #word count
    datas["WORD COUNT"]=(len(a4))


    #personal pronouns
    datas["PERSONAL PRONOUNS"]=(len(count_pro))


    return datas

d={"URL_ID":[],
   "URL":[],
   "POSITIVE SCORE":[],
   "NEGATIVE SCORE":[],
   "POLARITY SCORE":[],
   "SUBJECTIVITY SCORE":[],
   "AVG SENTENCE LENGTH":[],
   "PERCENTAGE OF COMPLEX WORDS":[],
   "FOG INDEX":[],
   "AVG NUMBER OF WORDS PER SENTENCE":[],
   "COMPLEX WORD COUNT":[],
   "WORD COUNT":[],
   "SYLLABLE PER WORD":[],
   "PERSONAL PRONOUNS":[],
   "AVG WORD LENGTH":[]
   }


for i in inputs:
    datas=sentimental_analysis(i[1],i[0])
    for key in d.keys():
        d[key].append(datas[key])
print(d)

