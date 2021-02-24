def getCategoriesUrl(cat):
    a = [
        {
            "link": "https://bestringtones.net/top-ringtones.html",
            "title": "Top"
        }, {
            "link": "https://bestringtones.net/popular-ringtones.html",
            "title": "Popular"
        },
        {
            "link": "https://bestringtones.net/ringtone-download-2021.html",
            "title": "2021"
        }, {
            "link": "https://bestringtones.net/ringtone-download-2020.html",
            "title": "2020"
        }, {
            "link": "https://bestringtones.net/bollywood.html",
            "title": "Bollywood"
        }, {
            "link": "https://bestringtones.net/punjabi-ringtones.html",
            "title": "Punjabi"
        }, {
            "link": "https://bestringtones.net/love-ringtones.html",
            "title": "Love"
        }, {
            "link": "https://bestringtones.net/tik-tok-ringtones.html",
            "title": "TikTok"
        }, {
            "link": "https://bestringtones.net/tamil-ringtones.html",
            "title": "Tamil"
        }, {
            "link": "https://bestringtones.net/bgm-ringtones-download.html",
            "title": "BGM"
        }, {
            "link": "https://bestringtones.net/funny-ringtones.html",
            "title": "Funny"
        }, {
            "link": "https://bestringtones.net/games-ringtones.html",
            "title": "Games"
        }, {
            "link": "https://bestringtones.net/remix-ringtones.html",
            "title": "Remix"
        }, {
            "link": "https://bestringtones.net/sound-effects-free-download.html",
            "title": "Sound"
        }, {
            "link": "https://bestringtones.net/animals-sounds.html",
            "title": "Animals"
        }, {
            "link": "https://bestringtones.net/pop-ringtones.html",
            "title": "Pop"
        }, {
            "link": "https://bestringtones.net/baby-ringtone.html",
            "title": "Baby"
        }, {
            "link": "https://bestringtones.net/guitar-ringtones-free-download.html",
            "title": "Guitar"
        }, {
            "link": "https://bestringtones.net/instrumental-ringtones.html",
            "title": "Instrumental"
        }, {
            "link": "https://bestringtones.net/free-ringtones-for-iphone.html",
            "title": "iPhone"
        }, {
            "link": "https://bestringtones.net/samsung-ringtones-free-download.html",
            "title": "Samsung"
        }, {
            "link": "https://bestringtones.net/message-ringtone-download.html",
            "title": "Message"
        },

    ]
    for b in a:
        if cat == b['title'].lower():
            return b['link']


def getPopularUrl():
    return "https://bestringtones.net/popular-ringtones.html"


def getTopUrl():
    return "https://bestringtones.net/top-ringtones.html"
