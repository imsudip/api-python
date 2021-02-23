import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import unquote


def getNews(category):
    newsDictionary = {
        'success': True,
        'category': category,
        'data': []
    }

    try:
        if category != 'all':
            htmlBody = requests.get(
                'https://www.inshorts.com/en/read/' + category)
        else:
            htmlBody = requests.get('https://www.inshorts.com/en/read/')

    except requests.exceptions.RequestException as e:
        newsDictionary['success'] = False
        newsDictionary['error'] = str(e.strerror)
        return newsDictionary

    soup = BeautifulSoup(htmlBody.text, 'lxml')
    newsCards = soup.find_all(class_='news-card')
    if not newsCards:
        newsDictionary['success'] = False
        newsDictionary['error'] = 'Invalid Category'
        return newsDictionary

    for index, card in enumerate(newsCards):
        try:
            title = card.find(class_='news-card-title').find('a').text.strip()
        except AttributeError:
            title = None

        try:
            imageUrl = card.find(
                class_='news-card-image')['style'].split("'")[1]
        except AttributeError:
            imageUrl = None

        try:
            url = ('https://www.inshorts.com' + card.find(class_='news-card-title')
                   .find('a').get('href'))
        except AttributeError:
            url = None

        try:
            content = card.find(class_='news-card-content').find('div').text
        except AttributeError:
            content = None

        try:
            author = card.find(class_='author').text
        except AttributeError:
            author = None

        try:
            date = card.find(clas='date').text
        except AttributeError:
            date = None

        try:
            time = card.find(class_='time').text
        except AttributeError:
            time = None

        try:
            readMoreUrl = card.find(class_='read-more').find('a').get('href')
        except AttributeError:
            readMoreUrl = None

        newsObject = {
            'title': title,
            'imageUrl': imageUrl,
            'url': url,
            'content': content,
            'author': author,
            'date': date,
            'time': time,
            'readMoreUrl': readMoreUrl
        }

        newsDictionary['data'].append(newsObject)

    return newsDictionary


def getWeather(city):
    weatherReport = {
        'success': True,
        'data': []
    }
    try:
        htmlBody = requests.get(
            'https://www.google.com/search?q='+city+'+weather')
    except requests.exceptions.RequestException as e:
        weatherReport['success'] = False
        weatherReport['error'] = str(e.strerror)
        return weatherReport
    soup = BeautifulSoup(htmlBody.content, 'lxml')
    mainlink = ''
    links = soup.findAll("a")
    for link in links:
        link_href = link.get('href')
        if "https://weather.com/" in link_href:
            if "url?q=" in link_href and not "webcache" in link_href:
                mainlink = link.get('href').split("?q=")[1].split("&sa=U")[0]
            break
    mainlink = unquote(mainlink)
    print(mainlink)
    try:
        htmlBody = requests.get(mainlink)
    except requests.exceptions.RequestException as e:
        weatherReport['success'] = False
        weatherReport['error'] = str(e.strerror)
        return weatherReport
    soup = BeautifulSoup(htmlBody.content, 'lxml')
    cards = soup.find_all('details', class_="Disclosure--themeList--uBa5q")
    for card in cards:
        try:
            date = card.find(
                'h2', class_='DetailsSummary--daypartName--1Mebr').text
        except AttributeError:
            continue
            date = None
        try:
            maximum = card.find(
                'span', class_='DetailsSummary--highTempValue--3x6cL').text
        except AttributeError:
            maximum = None
        try:
            minimum = card.find(
                'span', class_='DetailsSummary--lowTempValue--1DlJK').text
        except AttributeError:
            minimum = None
        try:
            rain = card.find(
                'div', class_='DetailsSummary--precip--2ARnx').find('span').text
        except AttributeError:
            rain = None
        try:
            condition = card.find(
                'div', class_='DetailsSummary--condition--mqdxh').find('span').text
        except AttributeError:
            condition = None
        print(date, minimum, maximum)
        weatherObject = {
            "date": date,
            "max": maximum,
            "min": minimum,
            "rainfall": rain,
            "condition":condition

        }
        weatherReport["data"].append(weatherObject)
    weatherReport["length"] = len(weatherReport["data"])
    return weatherReport
