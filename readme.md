# Base API Url
    https://imsudip-weather.herokuapp.com/
# Wikipedia API
Scrapped Article data from Wikipedia using BeutifulSoup
## Endpoints

    /wikisearch?q={ Search Query}

>  Pass the search string
>  *Demo Output*
>  https://imsudip-weather.herokuapp.com/wikisearch?q=doctor

    [
		"Doctor", 
		["Doctor", "Doctor Who", .....],
	    ["", "", .........],
	    ["https://en.wikipedia.org/wiki/Doctor", "https://en.wikipedia.org/wiki/Doctor_Who", .......]
	]


> 

     /wiki?link={Wikipedia Article Link}

>  Use the https link of the wikipedia article
> 
> Demo output
> https://imsudip-weather.herokuapp.com/wiki?link=https://en.wikipedia.org/wiki/Doctor_Who

    {
        "highlight": "science fiction television programme",
        "link": "https://en.wikipedia.org/wiki/Science_fiction_on_television",
        "summary": "Doctor Who is a British science fiction television programme broadcast by BBC One since 1963. The programme depicts the adventures of a Time Lord called the Doctor, an extraterrestrial being who appears to be human. The Doctor explores the universe in a time-travelling space ship called the TARDIS. The TARDIS exterior appears as a blue British police box, which was a common sight in Britain in 1963 when the series first aired. With various companions, the Doctor combats foes, works to save civilisations and helps people in need.\n",
        "title": "Science fiction on television"
    }


# Weather API
Api scraped from **weather.com**
## Endpoints

    /weather?city={cityName}

>   change the ***{cityName}*** to the name of the city.


# Zedge Ringtone API

Api scraped from **https://www.zedge.net/**
## Endpoints

    /zedgeRingtonesAll?page={page_no}

> For getting trending ringtones,
> **{page_no}**=page number

    /zedgeSearch?q={query}&page={page_no}
   > For getting search results from keywords,
> **{page_no}**=page number,
> **{query}**=query

    /zedgeRelatedSearches?q={query}
   > For getting related tags from keyword,
> **{qeury}**=qeury

# Ringtone API

Api scraped from **https://bestringtones.net/**
## Endpoints

    /ringtonesHome

> For getting ringtones from home page


    /ringtones?q={query}&page={page_no}
   > For getting search results from keywords,
   > For getting results from categories,
> **{page_no}**=page number
> **{query}**=query

    mention the categories in lowercase
    -   Top
    -   Popular
    -   2021
    -   2020
    -   Bollywood
    -   Punjabi
    -   Love
    -   TikTok
    -   Tamil
    -   BGM
    -   Funny
    -   Games
    -   Remix
    -   Sound
    -   Animals
    -   Pop
    -   Baby
    -   Guitar
    -   Instrumental
    -   iPhone
    -   Samsung
    -   Message

## Use Reqbin for testing and getting the model json.

> **https://reqbin.com/**

