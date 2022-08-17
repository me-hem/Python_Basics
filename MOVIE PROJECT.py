# for scapping import Beautifulsoup
from bs4 import BeautifulSoup as soup

# for searching in a string import re
import re

# to exchange request on the web import requests
import requests as req

# for getting random numbers to get random questions
import random

# Setting emotions:
#   Sad – Drama
#   Anger – Action
#   Anticipation – Thriller
#   Enjoyment – Comedy
#   Trust – Family
#   Surprise – Fantasy
#   Love - Romance


def main(emotion):
    if emotion == "sad":
        url = "https://www.imdb.com/search/title/?genres=drama&explore=title_type"
    elif emotion == "anger":
        url = "https://www.imdb.com/search/title/?genres=action&explore=title_type"
    elif emotion == "anticipation":
        url = "https://www.imdb.com/search/title/?genres=thriller&explore=title_type"
    elif emotion == "enjoyment":
        url = "https://www.imdb.com/search/title/?genres=comedy&explore=title_type"
    elif emotion == "trust":
        url = "https://www.imdb.com/search/title/?genres=family&explore=title_type"
    elif emotion == "surprise":
        url = "https://www.imdb.com/search/title/?genres=fantasy&explore=title_type"
    elif emotion == "love":
        url = "https://www.imdb.com/search/title/?genres=romance&explore=title_type"
    else:
        print("Sorry, I am just a machine can't handle too much emotions.\nCome with new emotions later!!!")
        exit()

# Scrapping data from webpage
    response = req.get(url)
    data = response.text

# Parsing using BeautifulSoup
    SOUP = soup(data, 'lxml')

# Extracting title from parsed data using re.

    title = SOUP.find_all(
        "a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


# getEmotion function will recognize the emotion of the user and will return the emotion
def getEmotion():
    num, points = 0, []
    
    #questions dictionary is to provide questionnaire for calculating emotion rating.
    #We have just provided some test questions which could be modified at the time of testing
    questions = {1: "If you slap a person immediately, what would be your emotion's rating?",
                 2: "You must have completed some tasks today!! What's your satisfaction rating?",
                 3: "Hey, what a pleasant weather in Massoorie!! What's your area's weather rating?",
                 4: "Are you feeling lonely!! What's your loneliness rating?",
                 5: "Are you feeling sad!! What's your sadness rating?",
                 6: "Are you feeling enthusiastic!! What's your enthusiasm rating?",
                 7: "Are you feeling bored!! What's your mood rating?",
                 8: "Are you feeling !! What's your loneliness rating?",
                 9: "Are you feeling lonely!! What's your loneliness rating?",
                 10: "Are you feeling lonely!! What's your loneliness rating?",
                 11: "Are you feeling lonely!! What's your loneliness rating?",
                 12: "Are you feeling lonely!! What's your loneliness rating?",
                 13: "Are you feeling lonely!! What's your loneliness rating?",
                 14: "Are you feeling lonely!! What's your loneliness rating?",
                 15: "Are you feeling lonely!! What's your loneliness rating?"}

    #Emotions dictionary is to provide emotion based on emotion rating average 
    emotions = {1: "sad",
                2: "anger",
                3: "enjoyment",
                4: "anticipation",
                5: "surprise",
                6: "trust",
                7: "love"
                }

    while True:
        num = int(
            input("How many questions you want to answer (between 5 to 15)?: "))
        if num > 4 and num < 16:
            break
        print("Invalid number of questions, please enter again in the range of 5-15.")

    
    if num > 10:
        points.append(7)
    else:
        points.append(num-5)

    for i in range(num):
        print("\n\n")
        print(questions[random.randint(1, 15)])
        rating = -1

        while True:
            rating = int(
                input("Please enter your emotion's rating (on scale 0-7): "))
            if rating < 8 and rating >= 0:
                break
            print("Hey emotion's rating cannot be too low or too high, so enter again in the range of 0-7!!!")

        points.append(rating)

    return emotions[round(sum(points)/len(points))]


if __name__ == "__main__":
    emotion = getEmotion()
    title_data = main(emotion)

    count = 0
    print("Your Emotion:",emotion.title(),"\nMovies recommended for you, Just Chill!!\n\n")
    for i in title_data:
        tmp = str(i).split('>')

        if(len(tmp) == 3):
            print(tmp[1][:-3])
        if(count > 13):
            break
        count += 1
