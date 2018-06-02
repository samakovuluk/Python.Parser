from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import traceback
import urllib.request
import urllib.parse
import urllib.request  as urllib2 
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options
import time
import os
#________Music Downloader________#
direct=""

url='https://myzuka.club'
import sys  
from urllib.request import Request, urlopen
def get_t_html(url):
         non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
         req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
         web_byte = urlopen(req).read()
         webpage = web_byte.decode("utf-8")
         return webpage
class Mus:  
    site=""
    isp=""
    name=""
    def __init__(self,sites, ispp, names):
        self.site=sites
        self.isp=ispp
        self.name=names
def proba(a,b):
    c=0
    a=a.lower()
    b=b.lower()
    print(a,b)
    for i in a:
        for j in b:
            if(i==j):
                c+=1
    print(c)
    print((c*100/((len(a)+len(b))/2)))
    if((c*100/((len(a)+len(b))/2))>=85):
        return True
    else: 
        return False
def get_html(url) :
    r=requests.get(url)
    return r.text.encode("utf-8")
def find_music(s,q):
    url = 'https://myzuka.club/Search?searchText='+s+"+"+q
    ht=get_html(url)
    soup=BeautifulSoup(ht,'lxml')
    music_content=(soup.find('div',class_="content")).encode('utf-8')
    musics=re.findall(r'<tr>(.*?)</tr>',str(music_content))
    mm=list()

    c=0
    for i in musics:
        t=re.findall(r'<a(.*?)</a>',i)
        ispp=""
        ssyl=""
        name=""
        if(t!=[]):
            ispp=t[0].split('>')[1]
            ssyl=t[1].split('>')[0]
            name=t[1].split('>')[1]
            mm.append(Mus(ssyl,ispp,name))
    for i in mm:
        if(proba(i.isp,q)==True and proba(i.name,s)==True):
            print("Yee, I found",i.site)
            return i.site
    print("I did not found any music")  
def get_music(s,q):
    music=(find_music(s,q).split('"'))
    html=get_html(url+music[1])
    soup=BeautifulSoup(html,'lxml')
    p=(soup.find('a',itemprop="audio"))
    soup=BeautifulSoup(str(p),'lxml')
    link=soup.find('a')
    obj=(link.get('href'))
    obj=url+obj
    print(obj)
    download_mp3(obj)
def download_mp3(link):
    options = Options()
    options.add_experimental_option("prefs", {
      "download.default_directory": r"D://",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(link);
    mp=""
    global direct
    while(True):
        for i in os.listdir("D://"):
            if(".mp3" in i and ".crdownload" not in i):
                mp=i
                break
        if(mp!=""):
            break
    old_file = os.path.join("D://", mp)
    pop=direct+"mp3"
    new_file = os.path.join("D://", direct+".mp3")
    os.rename(old_file, new_file)
    os.rename(new_file,"D://Projects//"+direct+"//"+direct+".mp3")
    
    print("Success")
def ensure_dir(file_path,s):
    directory = os.path.dirname(file_path)
    if  not os.path.exists(file_path+"//"+s):
            os.makedirs(file_path+"//"+s)
        
        
def main_music(s,q):
    global direct

    direct=s.replace(" ","_")+"+"+q.replace(" ","_")
    ensure_dir("D://Projects//",direct)
    print(direct)
    get_music(s,q)
#_______Music Downloader________#

#_______Text Downloader_________#
def get_l_html(link):
    response = requests.get(link,
         headers={
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
         })
    response=(response.text.encode("utf-8"))
    return response
def musixmatch_get_link(s,q):
    link="https://www.musixmatch.com/search/"+s.lower().replace(" ","%20")+"%20"+q.lower().replace(" ","%20")
    print(link)
    response = requests.get(link,
         headers={
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
         })
    response=(response.text.encode("utf-8"))

    soup=BeautifulSoup((response),'lxml')
    mm=list()
    p=re.findall("<li class=(.*?)</li>",str(response))
    for i in p:
        if("showArtist showCoverart" in i):
            so=BeautifulSoup(i,'lxml')
            print(response)
            try:
                name=so.find("a",class_="title").text
            except Exception:
                name=""
            try:
                isp=so.find("a",class_="artist").text
            except Exception:
                isp=""
            site=so.find('a').get("href")
            mm.append(Mus(site,isp,name))
    print(mm)
    for i in mm:
        print(i.isp)
    mom=""
    for i in mm:
        print(i.name,s,"asd")
        if(proba(i.name,q)==True and proba(i.isp,s)==True):
            print("https://www.musixmatch.com"+i.site)
            return "https://www.musixmatch.com"+i.site

    return "//"
def musixmatch(s,q):
    link=(musixmatch_get_link(s,q))
    html=get_l_html(link)
    print(link)
    driver=webdriver.Chrome()
    driver.get(link)
    button=driver.find_elements_by_class_name('cta-button')
    for i in button:
          if i.text=="Choose Translation":
                   i.click()
                   break

    langs=list()
    lg=driver.find_elements_by_class_name('cta-button ')
    for i in lg:
          if "(100%)" in i.text :
                   langs.append(i.text.strip('\n(100%)'))
    driver.close()
    print(langs)
    for i in langs:
        if(len(i)>0):
            print(link+"/translation/"+i.lower())
            get_text((link+"/translation/"+i.lower()),i)

def get_text(link,a):
    
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    req = Request(link,headers={'User-Agent':'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode("utf-8")
    soup=BeautifulSoup(webpage,'lxml')
    text=(soup.find_all('div',class_=" col-xs-6 col-sm-6 col-md-6 col-ml-6 col-lg-6"))
    if(text!=[]):
        c=1
        global direct
        l="D://Projects//"+direct+"//"
        print(l)
        ensure_dir(l,"musixmatch")
        f=open("D://Projects//"+direct+"//"+"musixmatch//"+"orginal.txt",'w',encoding=('utf-8'))
        file=open("D://Projects//"+direct+"//"+"musixmatch//"+a+'.txt','w',encoding=('utf-8'))
        
        for i in text:
            if(c>2):
                if(i.text!='\n'):
                   if c%2!=0:
                      f.write(i.text+"\n")
                   else:
                      file.write(i.text+"\n")
            c+=1
        file.close()


#_______Text Downloader_________#



def main():
    s="Marshmello"
    q="FRIENDS"
    global direct
    direct=s.replace(" ","_")+"+"+q.replace(" ","_")
    ensure_dir("D://Projects//",direct)
    
    musixmatch(s,q)
    #main_music(q,s)

if __name__ == '__main__':
    main()
