import os

domains = ["stanford.edu","amazon.com", "baidu.com","wikipedia.org","reddit.com","yahoo.co.jp","ebay.com","microsoft.com","bing.com","ok.ru","whatsapp.com","Naver.com","samsung.com","Reuters.com","Dailymail.co.uk","Bloomberg.com","ekantipur.com","Typepad.com","About.com","gnu.org","mit.edu","taobao.com", "surveymonkey.com", "olx.in", "51.la","behance.net","namejet.com","github.io","disqus.com","rambler.ru"]

def groupby(arrDomain):
    for domain in arrDomain:
        myCommand = "mkdir "  + domain+ " | mv *" +domain+ "* " + domain+"/" 
        os.system(myCommand)
        

if __name__ == "__main__":
   groupby(domains)

