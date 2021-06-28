# ba57bc15204e4fd6a1b4c44ede43f518
import datetime
import requests

def remove(data):
    for i in range(len(data)-1,0,-1):
        if data[i] == '-':
            return data[:i-1]
    return data

def get_news():
    news = []
    d1 = datetime.datetime.now().strftime("%Y-%m-")
    d = d1 + "01"
    print(d)
    url = ('http://newsapi.org/v2/everything?'
        'q=indian%20stock%20market&'
        'from='+d+'&'
        'sortBy=popularity&'
        'pageSize=10&'
        'apiKey=ba57bc15204e4fd6a1b4c44ede43f518')
    response = requests.get(url).json()
    i=0
    for data in response['articles']:
        if data['urlToImage']:
            temp={}
            temp['id'] = i
            i+=1
            temp['source'] = data['source']['name']
            if data['author']:
                temp['author'] = data['author']
            else:
                temp['author'] = "Not Available"
            temp['title'] = remove(data['title'])
            temp['desc'] = data['description']
            temp['url'] = data['url']
            temp['image'] = data['urlToImage']
            news.append(temp)
    return news

# print(get_news())