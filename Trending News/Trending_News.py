from GoogleNews import GoogleNews          #GoogleNews is the module to fetch the trending news
googlenews = GoogleNews()                  #Image is not working in the latest version
googlenews = GoogleNews(period='7d')
googlenews.search('INDIA')                #mentioning the place 
result = googlenews.result()
for x in result:
    print("-"*50)
    print("Title--",x['title'])         #title
    print("Date/Time--", x['date'])     #Date
    print("Desciption--", x['desc'])
    print("Link--", x['link'])            #Even it can fetch the url link also
