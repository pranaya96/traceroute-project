import sys
import os.path
import numpy as np
import operator

domainsArr = ["stanford.edu","amazon.com", "baidu.com","wikipedia.org","reddit.com","yahoo.co.jp","ebay.com","microsoft.com","bing.com","ok.ru","whatsapp.com","Naver.com","samsung.com","Reuters.com","Dailymail.co.uk","visitdubai.com","ekantipur.com","Typepad.com","About.com","gnu.org","mit.edu","taobao.com", "surveymonkey.com", "olx.in", "51.la","behance.net","namejet.com","github.io","disqus.com","rambler.ru"]

resultsArr =[]

def processFiles(domainsArr):
    
    for domain in domainsArr:
        results = []
        for i in range(30):
            varPath = domain + str(i+1) +'.txt'
            filePath =  domain+"/"+varPath
            z = readFile(filePath)
            for k in z:
                results.append(k)
        
        resultsArr.append(results)
    

def readFile(fileName):
    fileHandle = open (fileName,"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    lastLine = lineList[len(lineList)-1].split(" ")
    output = []
    for i in range(len(lastLine)):
        if "ms" in lastLine[i]:
            val_of_interest = lastLine[i-1]
            if "-" not in val_of_interest:
                output.append(val_of_interest)
    return output
    


def calculate(resultsArr):
    averageAndStd = []
    for x in range(len(resultsArr)):
        try:
           values_list = list(map(float, resultsArr[x]))
        except ValueError,e:
             #print "error",e,"on line",x
             pass
        average = np.mean(values_list)
        standardDeviation = np.std(values_list)
        averageAndStd.append((domainsArr[x],average, standardDeviation))
    return averageAndStd

def printReport(calculationsArr):
    for x in range(len(calculationsArr)):
        print "For host " + calculationsArr[x][0] + ":\n****************************\nAverage: " + str(calculationsArr[x][1])+'ms'+"\n"+"Average + 4 * Standard Deviation: "+ str(calculationsArr[x][2])+ "ms\n"
    topFiveAverage = sorted(calculationsArr, key = operator.itemgetter(1), reverse = True)[:5]
    topFiveAveragePlusSd = sorted(calculationsArr, key = operator.itemgetter(2), reverse = True)[:5]

    #print  topFiveAverage, topFiveAveragePlusSd
    print "######################################################"
    print "Top 5 host interms of average delay(Descending order):\n"
    for x in range(len(topFiveAverage)):
        print topFiveAverage[x][0]

    print "\nTop 5 host interms of average plus 4 times of S.D delay(Descending order):\n"   
    for x in range(len(topFiveAveragePlusSd)):
        print topFiveAveragePlusSd[x][0]
    


if __name__ == "__main__":
    processFiles(domainsArr)
    finalCalculations= calculate(resultsArr)
    printReport(finalCalculations)

 
