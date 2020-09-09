import numpy as np
import csv

import matplotlib.pyplot as plt


def readData(file_name):
    dataObj = open(r'{}'.format(file_name))

    cols = dataObj.readlines()
    dataObj.close()
    columnSubjects = cols[0].rsplit(",")
    del cols[0]

    obj = {columnSubjects[0]: [], columnSubjects[1]:  [], columnSubjects[2]: []}
    print(columnSubjects)
    print("Number of lines in the document:  ", len(cols))
    # For loop to organize data:

    for line in cols:
        newLine = line.split(',')

        for i in range(len(newLine)):
            if i == 0:
                obj[columnSubjects[i]].append(newLine[i])
            elif i == 1:
                obj[columnSubjects[i]].append(float(newLine[i]))
            else:
                obj[columnSubjects[i]].append(float(newLine[i].rstrip('\n')))
    return obj


def createGraph(dataObj):

    # axes = plt.gca()
    # axes.set_ylim(dataObj[" Deaths per 1000 People"][0],
    #               dataObj[" Deaths per 1000 People"][:-1])
    plt.plot_date(dataObj["date"], dataObj[" Deaths per 1000 People"])

    plt.show()
    pass


createGraph(readData("data/world_death_rate.csv"))

# readData("data/world_growth_rate.csv")
