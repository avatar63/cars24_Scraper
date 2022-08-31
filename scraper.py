from shutil import ExecError
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests



def Extract_Tags(url):
    block = soup.find_all("label",class_="_1Q_nE")
    for i in block:
        tagslist.append(i.text)

def Extract_Data(url):
    block = soup.find_all("strong",class_="_1-PH2")
    for i in block:
        datalist.append(i.text)
    
def CreateDict(tags,data):
    for i in range(len(tags)):
        dict.update({tags[i]:data[i]})


def Excel(dict):
    df = pd.DataFrame(data=dict, index=[0])
    print (df)
    df3=pd.concat([df])
    df3.to_excel('dict1.xlsx', index=False)



url = input("Enter the url of the vehicle: ")
db = requests.get(url).text
soup = bs(db,'lxml')
block = soup.find("label",class_="_1Q_nE")



tagslist=[]
datalist=[]
dict={}

Extract_Tags(url)
Extract_Data(url)
CreateDict(tagslist,datalist)
Excel(dict)
