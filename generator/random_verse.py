import json
import random
from .constants import *
random.seed()

# True random verses*******************************************************************
def getRandomBook(volume):
    # Get Random Book
    

    # Weight books according to number of verses (books with more verses get more hits)
    
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
    
    return RANDOM_BOOK

#**************************************************************************************


# Pseudo Pseudo random verse generator*************************************************
# Picks random book, then chapter, then verse

#def pseudoGetRandomBook():
    # Get Random Book
    #NUM_BOOKS = len(data['books'])
    #RANDOM_BOOK = random.randint(0, NUM_BOOKS-1)
    #print("Random Book: " + str(RANDOM_BOOK))

def pseudoGetRandomChapter():
    # Get Random Chapter
    NUM_CHAPTERS = len(data['books'][RANDOM_BOOK]['chapters'])
    RANDOM_CHAPTER = random.randint(0, NUM_CHAPTERS-1)
    return RANDOM_CHAPTER

def pseudoGetRandomVerse():
    # Get Random Verse
    NUM_VERSE = len(data['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'])
    RANDOM_VERSE = random.randint(0, NUM_VERSE-1)
    return RANDOM_VERSE

# Print the verse!
#print("Random Book: " + str(RANDOM_BOOK))
#print("Random Chapter: " + str(RANDOM_CHAPTER))
#print("Random Verse: " + str(RANDOM_VERSE))
#print(data['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'][RANDOM_VERSE])

#****************************************************************************************


def getScripture(volume):

        
    RANDOM_BOOK = getRandomBook(volume)
    print("random book: " + RANDOM_BOOK)
    #RANDOM_CHAPTER = pseudoGetRandomChapter(RANDOM_BOOK)
    #RANDOM_VERSE = pseudoGetRandomVerse(RANDOM_BOOK, RANDOM_CHAPTER)
    #result = [
    #    RANDOM_BOOK,
    #    RANDOM_CHAPTER,
    #    RANDOM_VERSE,
    #]

