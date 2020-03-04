import requests
from bs4 import BeautifulSoup
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


### User input selection, user inputs the name of an artist
### and the program formats the input to the requirements of the
### url

user_1 = input('Please enter the name of an artist or group    ')
user_1 = user_1.replace(' ','+')
url_1 = 'https://www.lyrics.com/artist/'
url_2 = url_1+user_1

print('Run times are roughly 1 minute per 100 songs ')
print('''Common bugs include..........
max tries exceeded with url, if an artist has
thousands of songs, the host sever may prevent 
you from making too many requests in a short period of time
Run times too long? Try searching for an Artist with
a smaller discography, or go have a cup of coffee while you wait''')



### The program then uses the request module to open the url
### where we use beautfiul soup find the text content of the page
### as we don't want to waste time bringing in images etc

all_song_urls = requests.get(url_2)
data = all_song_urls.text
soup = BeautifulSoup(data)

### the following loop finds all instances of <a> with the
### href attribute and stores them in the list 'links'

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    
### Filter out all Nonetype objects from the links list
    
links = filter(None, links)   

### Create a new list and store only urls that contain
### the artists name so as to filter out all uneccessary urls
    
new = []
for new_list in links:
    if (user_1) in new_list:
       new.append(new_list) 

### append the string to all elemnts in the list new
### this satisfies the url formatting requirements
       
app_url = ['https://www.lyrics.com' + link for link in new]

### this loop opens each url in 'appurl' list which contains all the 
### song urls, each url is a page containing lyrics
### we iterate through the list opening the page extracting the
### html content, parse the content, filter by the classes that contain
### the information we are interested in, in our case 'pre' and 'dd' class
### which contain the lyric body and the date of release respectively
### the length of the lyric body is counted and stored in the list 'words'
### the date is stored in the list 'dates'

words = []
dates = []

for txt in app_url:
    page = requests.get(txt)
    pages = page.text
    seep = BeautifulSoup(pages,'html.parser')
    s = seep.pre
    d = seep.dd
    
    word = s.get_text()
    date = d.get_text()
    
    w =  (len(word.split(' ')))
    
    words.append(w)
    dates.append(date)

### Some lyric pages don't contain release dates they contain view information
### in place of the date, we citerate through the list looking for the str 'View'
### if the str is found it is replaced 'No Date'
    
for i, item in enumerate(dates):
    if "View" in item:
        dates[i] = "No Date"
        
### Now we find the average number of words per song by diviind the sum of
### integers in the list 'words' by the number of song urls in the list 'new'
        
div = len(new)
add = sum(words)
print ('Average number of words used by ', user_1,' is ',(add/div))

### finally a plot to show the number of songs per year and the number of
### words per song

dat1 = pd.DataFrame({'Year' : dates,'Count': words})
sns.catplot('Year','Count',data=dat1)
plt.title('''Each point on the graph represents a song, the plot shows the date of
release (if there is one) and the number of words in the song''')
plt.show()

'''
Artists with ~400 songs ~ 5-6 min runtime
Artists with ~100 songs ~ 1-2 min runtime   
'''