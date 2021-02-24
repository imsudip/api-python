import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def getAllFromSection(card):
    section = {
        'ringtones': []
    }
    try:
        sectionName = card.find('div', class_='header').find(
            'a').find(text=True, recursive=False)
    except AttributeError:
        sectionName = None
        return
    section['topic'] = sectionName
    links = []
    players = card.find_all('script', type='text/javascript')
    
    for player in players:
        a = player.string
        link = a.split('mp3: "')[1].split('.mp3')[0]
        link = link+'.mp3'
        link = link.replace(' ', '%20')
        links.append(link)
    l = len(links)
    dtas = card.find_all('div', class_='meta audio-meta')
    for index, dta in enumerate(dtas):
        try:
            title = dta.find('b').text
        except AttributeError:
            title = None
        try:
            views = dta.find('span').text
        except AttributeError:
            views = None
        ringtone = {
            'title': title,
            'views': views,
            'link': links[index]
        }
        section['ringtones'].append(ringtone)
        section['length'] = l
    return section
