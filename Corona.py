from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="cv.ico",
        timeout=5
    )


def getDataUrl(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        myhtmldata=getDataUrl('https://www.worldometers.info/coronavirus/country/india/')
        soup=BeautifulSoup(myhtmldata,"html.parser")
        #print(soup.prettify())


        data=""
        for i in soup.find_all("div",{"id":"maincounter-wrap"}):
            data+=i.get_text()
            #data=data[1:]
            itemlist=data.split("\n\n")
            #print(itemlist)
        a=""
        for j in itemlist:
            a+=j
        
        print(a)
        

       
        
        
        notification.notify(
            title="Cases of corona virus in india",
            message=a,
            app_icon="cv.ico",
            timeout=5
        )
    time.sleep(30)

    """myhtmldata=getDataUrl('https://www.mohfw.gov.in/')
    
    soup=BeautifulSoup(myhtmldata,"html.parser")
    #print(soup.prettify())
    myData=""
    for tr in soup.find_all("div",{"id":"cases"}):
        myData+=tr.get_text()
        myData=myData[1:]
        Itemlist=myData.split("\n\n")
        #print(Itemlist)
    
    #print(Itemlist)
    states=['Maharashtra','Kerala','Delhi']
    for item in Itemlist[5:-7]:
        
        item=item.split("\n")
        datalist=item[1:]

        print(datalist)
        if datalist[1] in states:
            #print(datalist)
            nTitle="Cases of Corona Virus in Major Indian state"
            nText=f"State:{datalist[1]}\n Cases:{datalist[2]}\n,Deaths:{datalist[-1]}"
            notifyme(nTitle,nText)
            time.sleep(2)"""

    


    
