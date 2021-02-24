import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from getFromSection import getAllFromSection
from category import getCategoriesUrl
def getTrendingRingtones():
    ringtoneResult = {
        'success': True,
        'sections': []
    }
    try:
        htmlBody = requests.get(
            'https://bestringtones.net/')
    except requests.exceptions.RequestException as e:
        ringtoneResult['success'] = False
        ringtoneResult['error'] = str(e.strerror)
        return ringtoneResult
    soup = BeautifulSoup(htmlBody.content, 'lxml')
    cards = soup.find_all('div', class_='home-section')
    for card in cards:
        section = getAllFromSection(card)
        if section != None:
            ringtoneResult['sections'].append(section)

    return ringtoneResult

def getRingtonesFromCat(cat,page):
    ringtoneResult = {
        'success': True,
        'sections': []
    }
    url=getCategoriesUrl(cat)+'?&per_page='+str((int(page)-1)*24)
    print(url)
    try:
        htmlBody = requests.get(url)
    except requests.exceptions.RequestException as e:
        ringtoneResult['success'] = False
        ringtoneResult['error'] = str(e.strerror)
        return ringtoneResult
    soup = BeautifulSoup(htmlBody.content, 'lxml')
    anchors=soup.find('ul',class_='pages').find_all('li')
    nPages=''
    anchor=anchors[len(anchors)-1].find('a')
    print(anchor)
    nPages= anchor['href']   
    upages=nPages.split('_page=')[1]
    ringtoneResult['total pages'] =(int(upages)//24)   
    cards = soup.find_all('div', class_='home-section v')
    for card in cards:
        section = getAllFromSection(card)
        if section != None:
            ringtoneResult['sections'].append(section)
    return ringtoneResult
