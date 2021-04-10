import json
import random
from .constants import *
from django.contrib.staticfiles.storage import staticfiles_storage


# True random verses*******************************************************************
def getRandomBook(TOTAL_VERSES, getBookFinder):
    # Get Random Book
    

    # Weight books according to number of verses (books with more verses get more hits)
    
    RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
    #RANDOM_BOOK = getBook(RANDOM_NUMBER)
    RANDOM_BOOK = getBookFinder[RANDOM_NUMBER]
    """
    if volume == oldTestament:
        RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
        #RANDOM_BOOK = getBook(RANDOM_NUMBER)
        RANDOM_BOOK = getBookOfMormonBookFinder()[RANDOM_NUMBER]
    elif volume == newTestament:
        RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
        #RANDOM_BOOK = getBook(RANDOM_NUMBER)
        RANDOM_BOOK = bookOfMormonBookFinder[RANDOM_NUMBER]
    elif volume == bookOfMormon:
        RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
        #RANDOM_BOOK = getBook(RANDOM_NUMBER)
        RANDOM_BOOK = bookOfMormonBookFinder[RANDOM_NUMBER]
    elif volume == doctrineAndCovenants:
        RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
        #RANDOM_BOOK = getBook(RANDOM_NUMBER)
        RANDOM_BOOK = bookOfMormonBookFinder[RANDOM_NUMBER]
    elif volume == pearlOfGreatPrice:
        RANDOM_NUMBER = random.randint(1, TOTAL_BOM_VERSES)
        #RANDOM_BOOK = getBook(RANDOM_NUMBER)
        RANDOM_BOOK = bookOfMormonBookFinder[RANDOM_NUMBER]
    else:
        # This is an error condition!
        print("Invalid volume received in function: getScripture, volume: " + volume)
        RANDOM_BOOK = "INVALID VOLUME ERROR"
    """
    return RANDOM_BOOK

#**************************************************************************************


# Pseudo Pseudo random verse generator*************************************************
# Picks random book, then chapter, then verse

#def pseudoGetRandomBook():
    # Get Random Book
    #NUM_BOOKS = len(data['books'])
    #RANDOM_BOOK = random.randint(0, NUM_BOOKS-1)
    #print("Random Book: " + str(RANDOM_BOOK))

def pseudoGetRandomChapter(RANDOM_BOOK, volumeData):
    # Get Random Chapter
    print("volumeData: " + str(type(volumeData)))
    print("volumeData['books'] type: " + str(type(volumeData['books'])))

    #NUM_CHAPTERS = len(volumeData['books'][RANDOM_BOOK]['chapters'])
    NUM_CHAPTERS = len(volumeData['books'][RANDOM_BOOK])
    
    print("NUM_CHAPTERS: " + str(NUM_CHAPTERS))
    RANDOM_CHAPTER = random.randint(0, NUM_CHAPTERS-1)
    return RANDOM_CHAPTER

def pseudoGetRandomVerse(RANDOM_BOOK, RANDOM_CHAPTER, volumeData):
    # Get Random Verse
    NUM_VERSE = len(volumeData['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'])
    RANDOM_VERSE = random.randint(0, NUM_VERSE-1)
    return RANDOM_VERSE

# Print the verse!
#print("Random Book: " + str(RANDOM_BOOK))
#print("Random Chapter: " + str(RANDOM_CHAPTER))
#print("Random Verse: " + str(RANDOM_VERSE))
#print(data['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'][RANDOM_VERSE])

#****************************************************************************************


def getScripture(volume):
    random.seed()
    if volume == oldTestament:
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
    elif volume == newTestament:
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
    elif volume == bookOfMormon:
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
    elif volume == doctrineAndCovenants:
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
    elif volume == pearlOfGreatPrice:
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
    else:
        # This is an error condition!
        print("Invalid volume received in function: getScripture, volume: " + volume)
        RANDOM_BOOK = "INVALID VOLUME ERROR" 


    volumeData = json.load(open(jsonVolumeFile, 'r'))
    #print("volumeData: " + str(type(volumeData)))
    #print(volumeData)
    RANDOM_BOOK = getRandomBook(TOTAL_VERSES, getBookFinder)
    print("random book: " + str(RANDOM_BOOK))

    RANDOM_CHAPTER = pseudoGetRandomChapter(RANDOM_BOOK, volumeData)
    RANDOM_VERSE = pseudoGetRandomVerse(RANDOM_BOOK, RANDOM_CHAPTER, volumeData)
    result = [
        RANDOM_BOOK,
        RANDOM_CHAPTER,
        RANDOM_VERSE,
    ]
    print(result)
    return result

