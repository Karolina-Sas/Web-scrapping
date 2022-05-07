import time
import requests 
from bs4 import BeautifulSoup
from contextlib import redirect_stdout

start_time=time.time()

url="https://pl.wikipedia.org/wiki/Kategoria:Polskie_zespo%C5%82y_punkrockowe"
page=requests.get(url)
soup=BeautifulSoup(page.content,"lxml")

counter=0
for a in soup.find_all("a",title=True, accesskey=False):    
    if a["href"][0:5]=="/wiki" and a["href"][0:16]!="/wiki/Wikipedia:" and a["href"][0:16]!="/wiki/Kategoria:":
            
        with open('punk2.txt', 'a+') as file:
                with redirect_stdout(file):                                      
                    print(a.get_text())                    
                    counter+=1
file.close()

with open('punk2.txt', 'r') as file :
  filedata = file.read()
filedata = filedata.replace('(zespół muzyczny)', '')
filedata = filedata.replace('(polski zespół muzyczny)', '')
filedata = filedata.replace('(zespół)', '')

with open('punk2.txt', 'w') as file2:
  file2.write(filedata)

print("records found: " + str(counter) + " processing time: "+ str(round(time.time()-start_time,2))+" s")

file2.close()
