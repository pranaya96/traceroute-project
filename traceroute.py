import sys
import os

domains = ["stanford.edu","amazon.com", "baidu.com","wikipedia.org","reddit.com","yahoo.co.jp","ebay.com","microsoft.com","bing.com","ok.ru","whatsapp.com","Naver.com","samsung.com","Reuters.com","Dailymail.co.uk","visitdubai.com","ekantipur.com","Typepad.com","About.com","gnu.org","mit.edu","taobao.com", "surveymonkey.com", "olx.in", "51.la","behance.net","namejet.com","github.io","disqus.com","rambler.ru"]


def runTraceroute(arrDomain):
    trace= "sudo tcptraceroute"
    i = 0
    while i < 30:
        for domain in arrDomain:
            myCommand = trace+ " " + domain+ " >" + domain+str(i+1)+".txt"
            os.system(myCommand)
        i+=1

if __name__ == "__main__":
   runTraceroute(domains)


