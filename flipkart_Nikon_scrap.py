
import requests
from bs4 import BeautifulSoup
from pprint import pprint 
def page_url():
	res=requests.get("https://www.flipkart.com/search?q=nikon+cameras&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_2_na_na_na&as-pos=2&as-type=RECENT&suggestionId=nikon+cameras&requestId=70d85ff9-bf65-4fa7-a4e9-1b1f8bea6b57&as-searchtext=ni")
	soup=BeautifulSoup(res.text,"html.parser")
	url=soup.find("div",class_="_2zg3yZ")
	text=url.find_all("a")
	link_list=[]
	for f in text:
		u=f.get("href")
		link="https://www.flipkart.com"+u
		link_list.append(link)
	return link_list	

url=page_url()
def all_Nikon_details(url):
	b=0
	for url1 in url:
		# print(url1)
		name_list=[]
		price_list=[]
		All_Detailes=[]
		res=requests.get(url1)
		# print(res)
		soup=BeautifulSoup(res.text,"html.parser")
		name=soup.find_all("div",class_="_3wU53n")
		a=0
		for i in name:
			a+=1
			name_list.append(i.text)
		# print(name_list)
		rate=soup.find_all("div",class_="_1vC4OE")
		for j in rate:
			price_list.append(j.text)

		# print(price_list)
		detailes=soup.find_all("ul",class_="vFw0gD")
		for n in detailes:
			detaile=n.find_all("li",class_="tVe95H")
			detailes1=[]
			dic={}
			for m in detaile:
				detailes1.append(m.text)
				dic["All Detailes"]=detailes1
			All_Detailes.append(dic)

		# # dic1={}
		# # for h in range(len(name_list)):
		# # 	dic1["name"]=name_list[h]
		# # 	dic1["price"]=price_list[h]
		# # 	dic1["detailes"]=All_Detailes[h]	
		# # 	pprint(dic1)	

		for k in name_list:
			for l in price_list:
				for  h in All_Detailes:
					pprint(k)
					pprint(l)
					pprint(h)
					pprint("=============================================================================================")

all_Nikon_details(url)


