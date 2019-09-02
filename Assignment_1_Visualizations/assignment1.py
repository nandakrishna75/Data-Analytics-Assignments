# SCATTER PLOT
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.mlab as mlab
import statistics as st
import re
import time
df = pd.read_csv("./CANDIDATE_ANALYSED_LIST.csv")

def partyVsEarnings():
    list1 = []
    list2 = []

    # print(df.groupby(['PARTY', 'EARNINGS']).count())
    list1.append(df['PARTY'][0])
    list2.append(df['EARNINGS'][0])
    for index, row in df['PARTY'][1:].items():
        if df["PARTY"][index] in list1:
            index2 = list1.index(df['PARTY'][index])
            list2[index2] += df['EARNINGS'][index]
        else:
            list1.append(df['PARTY'][index])
            list2.append(df['EARNINGS'][index])
    # print(list1)
    # print(list2)
    x = list1[1:10]
    y = list2[1:10]
    plt.plot(x,y,'o',color='black')
    plt.xlabel('PARTY')
    plt.ylabel('EARNINGS')
    plt.title('party vs earnings')
    plt.show()

def educationVsVotes():
    list1 = []
    list2 = []

    # print(df.groupby(['EDUCATION', 'TOTAL_VOTES']).count())
    list1.append(df['EDUCATION'][0])
    list2.append(df['TOTAL_VOTES'][0])
    for index, row in df['EDUCATION'][1:].items():
        if df["EDUCATION"][index] in list1:
            index2 = list1.index(df['EDUCATION'][index])
            list2[index2] += df['TOTAL_VOTES'][index]
        else:
            list1.append(df['EDUCATION'][index])
            list2.append(df['TOTAL_VOTES'][index])
    # print(list1)
    # print(list2)
    x = list1[1:10]
    y = list2[1:10]
    plt.plot(x,y,'o',color='black')
    plt.xlabel('EDUCATION')
    plt.ylabel('TOTAL_VOTES')
    plt.title("education vs votes")
    plt.show()

def partyVsVotes():
    list1 = []
    list2 = []

    # print(df.groupby(['PARTY', 'TOTAL_VOTES']).count())
    list1.append(df['PARTY'][0])
    list2.append(df['TOTAL_VOTES'][0])
    for index, row in df['PARTY'][1:].items():
        if df["PARTY"][index] in list1:
            index2 = list1.index(df['PARTY'][index])
            list2[index2] += df['TOTAL_VOTES'][index]
        else:
            list1.append(df['PARTY'][index])
            list2.append(df['TOTAL_VOTES'][index])
    # print(list1)
    # print(list2)
    x = list1[1:10]
    y = list2[1:10]
    # index = np.arrange(len(y))
    plt.bar(x,y)
    plt.xlabel('Party')
    plt.ylabel('Total votes')
    plt.xticks(x,x,rotation=30)
    plt.title('Votes for each Party')
    plt.show()

def casesVsVotes():
    list1 = []
    list2 = []

    # print(df.groupby(['NO_PENDING_CRIMINAL_CASES', 'TOTAL_VOTES']).count())
    list1.append(df['NO_PENDING_CRIMINAL_CASES'][0])
    list2.append(df['TOTAL_VOTES'][0])
    for index, row in df['NO_PENDING_CRIMINAL_CASES'][1:].items():
        if df["NO_PENDING_CRIMINAL_CASES"][index] in list1:
            index2 = list1.index(df['NO_PENDING_CRIMINAL_CASES'][index])
            list2[index2] += df['TOTAL_VOTES'][index]
        else:
            list1.append(df['NO_PENDING_CRIMINAL_CASES'][index])
            list2.append(df['TOTAL_VOTES'][index])
    # print(list1)
    # print(list2)
    x = list1[1:10]
    y = list2[1:10]
    # index = np.arrange(len(y))
    plt.bar(x,y)
    plt.xlabel('NO_PENDING_CRIMINAL_CASES')
    plt.ylabel('Total votes')
    plt.xticks(x,x,rotation=30)
    plt.title('Votes vs No of pending criminal cases')
    plt.show()

def educationVsEarning():
    list1 = []
    list2 = []

    # print(df.groupby(['EDUCATION', 'EARNINGS']).count())
    list1.append(df['EDUCATION'][0])
    list2.append(df['EARNINGS'][0])
    for index, row in df['EDUCATION'][1:].items():
        if df["EDUCATION"][index] in list1:
            index2 = list1.index(df['EDUCATION'][index])
            list2[index2] += df['EARNINGS'][index]
        else:
            list1.append(df['EDUCATION'][index])
            list2.append(df['EARNINGS'][index])
    # print(list1)
    # print(list2)
    x = list1[1:10]
    y = list2[1:10]
    # index = np.arrange(len(y))
    plt.bar(x,y)
    plt.xlabel('EDUCATION')
    plt.ylabel('earnings')
    plt.xticks(x,x,rotation=30)
    plt.title('earnings vs education')
    plt.show()


partyVsEarnings()
educationVsVotes()
partyVsVotes()
# casesVsVotes()
educationVsEarning()