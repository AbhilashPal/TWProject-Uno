import bs4 as bs 
import urllib.request 

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
sauce = opener.open("https://engineering.careers360.com/news/latest/").read()

soup = bs.BeautifulSoup(sauce,'lxml')

news = []
for p in (soup.find_all('div',class_='description')):
	news.append(p.text)

newslinks = []
for url in (soup.find_all('div',class_='title')):
	newslinks.append(url.find('a').get('href'))

#saving to csv
import csv
stringstem = "https://engineering.careers360.com"
def writetocsv(L,M,yes=False):
	if yes:
		returns_path = "TEST_RESULT.csv"
		file = open(returns_path,'w')
		writer = csv.writer(file)
		writer.writerow(["RecordNo ","News ","Link "],)
		for i in range(len(L)-1):
			RecordNo = i+1
			Label1 = L[i]
			Label2 = M[i]		
			writer.writerow([RecordNo,Label1,stringstem+Label2],)
	else:
		print("Not Written")
writetocsv(news,newslinks,True)