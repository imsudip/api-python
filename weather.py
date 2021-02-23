import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
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
