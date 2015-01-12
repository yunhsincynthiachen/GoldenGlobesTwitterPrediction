# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:17:03 2015

@author: ychen1
"""

from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt

def ggmoviestwittersearch(textfile,dict_stuff):
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    L = []
    L2 = []
    t = Twitter()
    for key in dict_stuff:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + dict_stuff[key]):
            L.append(tweet.text)
            L2.append(sentiment(tweet.text))

    file = open(textfile,'w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L:
        file.write(str(i)+'\n')
    file.close()
    
def openbestggmpfiletweets(textfile):
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open(textfile,'r') as myfile:
        data = myfile.readlines()
    return data
    
def makingtweetslowercase(data):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets = []
    for i in range(len(data)):
        tweets.append(data[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets

def finding_sentiment_analysis(index, lower_case_list):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index = []
    for j in index: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index.append((sentiment(lower_case_list[j])))
    return sent_index

def finding_tot_sentiment_for_movie(sent_index):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index:
        tot_sent += i[0]
    return tot_sent
    
##############################################################################################################

if __name__ == "__main__":
    goldenglobesmpvalue = '\"best drama\"will win';
    goldenglobescomvalue = '\"will win';
    
    ggbestmotionpicture = {'\"boyhood\"':goldenglobesmpvalue,
               '\"foxcatcher\"':goldenglobesmpvalue, 
               '\"imitation game\"':goldenglobesmpvalue, 
               '\"selma\"':goldenglobesmpvalue, 
               '\"theory of everything\"':goldenglobesmpvalue}
               
    ggbestcomedy = {'\"into the woods\"':goldenglobescomvalue,
               '\"birdman\"':goldenglobescomvalue, 
               '\"grand budapest hotel\"':goldenglobescomvalue, 
               '\"st. vincent\"':goldenglobescomvalue, 
               '\"pride\"':goldenglobescomvalue}
               
    ggbestdirector = {'\"ava duvernay\"':goldenglobescomvalue,
               '\"wes anderson\"':goldenglobescomvalue, 
               '\"alejandro\"':goldenglobescomvalue, 
               '\"david fincher\"':goldenglobescomvalue, 
               '\"richard linklater\"':goldenglobescomvalue}
               
    ggbestactresscom = {'\"julianne moore\"':goldenglobescomvalue,
               '\"amy adams\"':goldenglobescomvalue, 
               '\"emily blunt\"':goldenglobescomvalue, 
               '\"helen mirren\"':goldenglobescomvalue, 
               '\"quvenzhane wallis\"':goldenglobescomvalue}
              
    ggbestactressmp = {'\"julianne moore\"':goldenglobescomvalue,
               '\"rosamund pike\"':goldenglobescomvalue, 
               '\"reese witherspoon\"':goldenglobescomvalue, 
               '\"felicity jones\"':goldenglobescomvalue, 
               '\"jennifer aniston\"':goldenglobescomvalue}
    
    ggbestactorcom = {'\"michael keaton\"':goldenglobescomvalue,
               '\"bill murray\"':goldenglobescomvalue, 
               '\"ralph fiennes\"':goldenglobescomvalue, 
               '\"christoph waltz\"':goldenglobescomvalue, 
               '\"joaquin phoenix\"':goldenglobescomvalue}
    
    ggbestactormp = {'\"eddie redmayne\"':goldenglobescomvalue,
               '\"steve carell\"':goldenglobescomvalue, 
               '\"benedict cumberbatch\"':goldenglobescomvalue, 
               '\"david oyelowo\"':goldenglobescomvalue, 
               '\"jake gyllenhaal\"':goldenglobescomvalue}
               
    ggmp = [ggbestmotionpicture,ggbestcomedy,ggbestdirector,ggbestactresscom,ggbestactressmp,ggbestactorcom,ggbestactormp]    #initializes a dictionary that we can use to search through Twitter for

    textfiles = ['bestggmptweets.txt','bestggcomtweets.txt','bestggdirtweets.txt','bestggactcomtweets.txt','bestggactrmptweets.txt','bestggactorcomtweets.txt','bestggactormptweets.txt']
    
    lists = []
    for i in textfiles:
        #ggmoviestwittersearch(i,ggmp[textfiles.index(i)])
        lists.append(makingtweetslowercase(openbestggmpfiletweets(i))) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    sizes = []
    sumofsentiments = 0
    
    all_index = [[],[],[],[],[]]
    all_sent_ggmp = []
    ggmp_names = ['boyhood','foxcatcher','imitation game','selma','theory of everything']
    ggmpcom_names = ['into the woods','birdman','grand budapest hotel','st. vincent','pride']
    ggdirector_names = ['ava duvernay','wes anderson','alejandro','david fincher','richard linklater']
    ggactresscom_names = ['julianne moore','amy adams','emily blunt','helen mirren','quvenzhane wallis']
    ggactressmp_names = ['julianne moore','rosamund pike','reese witherspoon','felicity jones','jennifer aniston']
    ggactorcom_names = ['michael keaton','bill murray','ralph fiennes','christoph waltz','joaquin phoenix']
    ggactormp_names = ['eddie redmayne','steve carell','benedict cumberbatch','david oyelowo','jake gyllenhaal']
    
    for name in ggmpcom_names: 
        for i in range(len(lists[1])):
            if name in lists[1][i]:
                all_index[ggmpcom_names.index(name)].append(i)

    for i in range(len(all_index)):
        all_sent_ggmp.append(finding_tot_sentiment_for_movie(finding_sentiment_analysis(all_index[i], lists[1])))

    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sum_name_list = []    
    for sum_name in all_sent_ggmp:
        if sum_name < 0:
            sum_name_list.append(-sum_name)
        else:
            sum_name_list.append(sum_name)
            
    print sum_name_list
    
    for name in sum_name_list:
        sumofsentiments += (name)/100
    
    for size_name in sum_name_list:
        sizes.append(size_name/sumofsentiments)
    
    
    
    labels = ['Boyhood','Foxcatcher','The Imitation Game','Selma','The Theory of Everything']
    labels2 = ['Into the Woods','Birdman','Grand Budapest Hotel','St. Vincent','Pride']
    labels3 = ['Ava Duvernay','Wes Anderson','Alejandro Gonzalez Inarritu','David Fincher','Richard Linklater']
    labels4 = ['Julianne Moore','Amy Adams','Emily Blunt','Helen Mirren','Quvenzhane Wallis']
    labels5 = ['Julianne Moore','Rosamund Pike','Reese Witherspoon','Felicity Jones','Jennifer Aniston']
    labels6 = ['Michael Keaton','Bill Murray','Ralph Fiennes','Christoph Waltz','Joaquin Phoenix']
    labels7 = ['Eddie Redmayne','Steve Carell','Benedict Cumberbatch','David Oyelowo','Jake Gyllenhaal']
    
    colors = ['yellowgreen','orange','gold','red','lightskyblue']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes,labels=labels2,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    
