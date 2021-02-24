import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def removeExtra(s):
    s = s.replace('\n','')
    s = s.replace('\t','')
    return s
def getAccuweather(city,page):
    weatherReport = {
        'success': True,
        'data': []
    }
    headers = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":	"gzip, deflate, br",
        "Accept-Language":	"en-US,en;q=0.5",
        "Host":	"www.accuweather.com",
        "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    
    apiUrl=f'https://www.accuweather.com/web-api/autocomplete?query={city}&language=en-us'
    apiRes = requests.request("GET", apiUrl, headers=headers)
    key=apiRes.json()[0]['key']
    print(key)
    url = f'https://www.accuweather.com/en/in/{city}/{key}/daily-weather-forecast/{key}?page={page}'
    h = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(h.content, 'lxml')
    dateRange=soup.find('p',class_='module-title').text
    print(dateRange)
    weatherReport['startDate']=dateRange.split(' - ')[0]
    weatherReport['endDate']=dateRange.split(' - ')[1]
    cards = soup.find_all('div',class_='daily-wrapper')
    for card in cards:
        date=card.find('span',class_='module-header sub date').text
        day=card.find('span',class_='module-header dow date').text
        high=card.find('span',class_='high').text
        low=card.find('span',class_='low').text
        low=low.replace('/','')
        prec=card.find('div',class_='precip').text
        prec = removeExtra(prec)
        phrase=card.find('div',class_='phrase').text
        phrase=removeExtra(phrase)
        weatherObject = {
            "date": date,
            "day":day,
            "max": high,
            "min": low,
            "rainfall": prec,
            "condition":phrase
        }
        weatherReport["data"].append(weatherObject)
    return weatherReport
    
