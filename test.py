import requests
from Tkinter import *
from bs4 import BeautifulSoup

url = "http://www.cbc.ca/news"

html_content = requests.get(url)

data = html_content.text

soup = BeautifulSoup(data)

topStory = soup.find_all("a", {"class": "pinnableHref pinnableHeadline"})


t = Tk()

# set window measurments + title
t.geometry("450x100")
t.title("CBC HeadLines")

# create scrollbar
scrollbar = Scrollbar(t)
scrollbar.pack( side = RIGHT, fill=Y )

# create list with height = length of list
lb = Listbox(t, height=len(topStory), width= 450)
lb.pack()

# loop and insert line to list
n=0
while n < len(topStory):
    lb.insert(END, topStory[n].text)
    n += 1

# this will let the scroll bar go up/down through out the list
scrollbar.config( command = lb.yview )


t.mainloop()
