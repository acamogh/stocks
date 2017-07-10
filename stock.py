from bs4 import BeautifulSoup
import re
import csv
import urllib2


import requests

# url = raw_input("Enter a website to extract the URL's from: ")

# r  = requests.get("http://" +url)
r=requests.get('http://www.moneycontrol.com/mutualfundindia/')
data = r.text

soup = BeautifulSoup(data)

mF_link=soup.body.findAll('div',{'class':'equityN'})

count = 0
large_cap=[]
mid_cap=[]




for ul in mF_link:
    for li in ul.find_all("a", class_="b-12"):
            if(count <=2):
                count+=1
                large_cap.append(str(li.get_text()))
            elif(count >=3 and count <=5):
                count+=1
                mid_cap.append(str(li.get_text()))


# with open("stocks.csv", 'w',newline='') as f:
#     writeFile = csv.writer(f)
#     writeFile.writerows('large cap')
#     writeFile.writerows(large_cap)
#     writeFile.writerows('mid cap')
#     writeFile.writerows(mid_cap)

choice  = raw_input(" 1)large cap \n 2)Mid cap : \n Enter your choice: ")

if choice == '1':
    print large_cap
else:
    print mid_cap



