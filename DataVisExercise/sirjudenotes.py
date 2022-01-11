# 1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
# 2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).

import csv
import matplotlib.pyplot as plt
import datetime as dt
import pygal
import statistics as st

filename = 'activity.csv'

dictDate = {}
dictInterval = {}

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow)

    for row in reader:
        steps = row[0]
        #disregard NA values
        if steps!= 'NA':
            date = row[1]
            date2 = int(dt.datetime.strptime(date,'%Y-%m-%d').day)
            
            interval = int(row[2])
            
            #populate the dictionary
            #if the date exists, nothing happense
            #otherwise, add new key in the dictionary
            dictDate.setdefault(str(date),[])
            #populate the list with the number of steps
            #taken in the specific date
            dictDate[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            
    listDate = []   #store the dates
    listTotal = []  #stores the total number of steps taken per day
    listAve = []     #stores the average number of steps taken per day
    
    for i in dictDate.keys():
        listDate.append(i)
        listTotal.append(sum(dictDate.get(i)))
        listAve.append(st.mean(dictDate.get(i)))
        
    #plot the points using a histogram
    hist = pygal.Bar()
    hist.title = "Total steps per day"
    hist.x_title = "Steps per day"
    hist.y_title = "Frequency"
    hist.x_labels = listDate
    hist.add("Total number of steps",listTotal)
    hist.render_to_file('stepsversion2.svg')
    
    print("Mean : " +str(st.mean(listTotal)))
    q = sorted(listTotal)
    print("Median : "+str(st.median(q)))
    

    #second case
    #what is the average daily activity pattern
    
    listAveragePerInterval = []
    for i in dictInterval.keys():
        listAveragePerInterval.append(st.mean(dictInterval.get(i)))
        
    print(listAveragePerInterval)
    
    #1. Make a time series plot of the 5-minute interval (x-axis) 
    #and the average number of steps taken, averaged across all days (y-axis)
    
    hist = pygal.Bar()
    hist.title = "Average per interval"
    hist.x_title = "The interval"
    hist.y_title = "Average per interval"
    hist.x_labels = dictInterval.keys()
    hist.add("Average steps",listAveragePerInterval)
    hist.render_to_file('stepsversion3.svg')
    
    #2. Which 5-minute interval, on average across all the days in the 
    #dataset, contains the maximum number of steps?
    answer = max(listAveragePerInterval)
    print(answer)
            
            
