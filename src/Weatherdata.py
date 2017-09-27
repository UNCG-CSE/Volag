from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import re
import os

f = open("ListofStations.txt",'r')
stations = []
for line in f:
    for station in line.split():
        for x in range(2016, 2017):
            for y in range(1, 13):
                urlstring = "http://newa.nrcc.cornell.edu/newaLister/hly/" + station + "/" + str(x) + "/" + str(y)
                print(urlstring)
                html = urlopen(urlstring)
                bsObj = BeautifulSoup(html, "html.parser")
                # print(bsObj)
                temp = bsObj.find("table", {"class": "fixedTable"})
                print(temp)
# print(temp.parent)
# list = []
# count = 0
#
# for link in temp.findAll("a", href=re.compile()[0-9]{4}")):
#     if 'href' in link.attrs:
#         # print(link.attrs['href'])
#         if (link.attrs['href']) not in list:
#             list.append(link.attrs['href'])
#
# size = 0
# folder = input("What is your destination folder?")
# for link in list:
#     print(link)
#     html = urllib.request.build_opener(urllib.request.HTTPCookieProcessor).open(link)
#     bsObj = BeautifulSoup(html, "html.parser")
#     title = str(bsObj.find("title").get_text())
#     fileName = folder + "\\" + title + ".txt"
#     while (fileName.__contains__("?")):
#         fileName = fileName.replace("?", "")
#     f = open(fileName, 'w')
#     string = ""
#     for x in bsObj.findAll("p", {"class": "story-body-text story-content"}):
#         string += x.getText()
#     f.write(string)
#     f.close()
# print("done")