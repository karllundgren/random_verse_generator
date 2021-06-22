import json
import random
from .constants import *
from django.contrib.staticfiles.storage import staticfiles_storage

def volumeFinder():
    RANDOM_NUMBER = random.randint(1, TOTAL_SCRIPTURE_VERSES)
    vFinder = getVolumeFinder()
    volume = ScriptureVolumes[vFinder[RANDOM_NUMBER]]
    print("volume in volumeFinder: " + volume)
    return volume

# True random verses*******************************************************************
def getRandomBook(TOTAL_VERSES, getBookFinder):

    # Weight books according to number of verses (books with more verses get more hits)
    RANDOM_NUMBER = random.randint(1, TOTAL_VERSES)

    #RANDOM_BOOK = getBook(RANDOM_NUMBER)
    print("RANDOM_BOOK_NUMBER: " + str(RANDOM_NUMBER))
    RANDOM_BOOK = getBookFinder[RANDOM_NUMBER]

    return RANDOM_BOOK

#**************************************************************************************


# Pseudo Pseudo random verse generator*************************************************
# Picks random book, then chapter, then verse

#def pseudoGetRandomBook():
    # Get Random Book
    #NUM_BOOKS = len(data['books'])
    #RANDOM_BOOK = random.randint(0, NUM_BOOKS-1)
    #print("Random Book: " + str(RANDOM_BOOK))

def pseudoGetRandomChapter(RANDOM_BOOK, volumeData, isDC):
    if isDC:
        # Because D&C has only sections and verses (not books, chapters, and verses),
        # We assign RANDOM_BOOK and RANDOM_CHAPTER the same value for ease of implementation
        return RANDOM_BOOK

    # Get Random Chapter
    print("volumeData: " + str(type(volumeData)))
    print("volumeData['books'] type: " + str(type(volumeData['books'])))

    #NUM_CHAPTERS = len(volumeData['books'][RANDOM_BOOK]['chapters'])
    NUM_CHAPTERS = len(volumeData['books'][RANDOM_BOOK]['chapters'])
    print("Book Index: " + str(RANDOM_BOOK))
    print("NUM_CHAPTERS: " + str(NUM_CHAPTERS))
    RANDOM_CHAPTER = random.randint(0, NUM_CHAPTERS-1)
    return RANDOM_CHAPTER

def pseudoGetRandomVerse(RANDOM_BOOK, RANDOM_CHAPTER, volumeData, isDC):
    if isDC:
        # Get Random Verse 
        NUM_VERSE = len(volumeData['sections'][RANDOM_BOOK]['verses'])
        
        RANDOM_VERSE = random.randint(0, NUM_VERSE-1)
        VERSE = volumeData['sections'][RANDOM_BOOK]['verses'][RANDOM_VERSE]
        return [RANDOM_VERSE, VERSE]

    print("Book: " + str(RANDOM_BOOK))
    print("Chapter: " + str(RANDOM_CHAPTER))
    print("books length: "+ str(len(volumeData['books'])))
    print("chapters length: "+ str(len(volumeData['books'][RANDOM_BOOK]['chapters'])))
    print("verse length: "+ str(len(volumeData['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'])))








    # Get Random Verse
    VERSES = volumeData['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses']
    NUM_VERSE = len(VERSES)
    
    RANDOM_VERSE = random.randint(0, NUM_VERSE-1)
    VERSE = volumeData['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'][RANDOM_VERSE]
    return [RANDOM_VERSE, VERSE]

# Print the verse!
#print("Random Book: " + str(RANDOM_BOOK))
#print("Random Chapter: " + str(RANDOM_CHAPTER))
#print("Random Verse: " + str(RANDOM_VERSE))
#print(data['books'][RANDOM_BOOK]['chapters'][RANDOM_CHAPTER]['verses'][RANDOM_VERSE])

#****************************************************************************************

def generateLinkToVerse(URL_VOLUME, RANDOM_BOOK, BOOK_URLS, RANDOM_CHAPTER, RANDOM_VERSE):
    
    # Examples Below:
    # BOM   https://www.churchofjesuschrist.org/study/scriptures/bofm/jacob/7.27?lang=eng#p27#27
    # D&C   https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/3.18?lang=eng#p18#18
    # Pearl https://www.churchofjesuschrist.org/study/scriptures/pgp/moses/1.42?lang=eng#p42#42
    # OT    https://www.churchofjesuschrist.org/study/scriptures/ot/1-sam/15.6?lang=eng#p6#6
    # NT    https://www.churchofjesuschrist.org/study/scriptures/nt/1-cor/16.15?lang=eng#p15#15
    
    """
    Order of Concatenation:
        1. BASE_URL                 https://www.churchofjesuschrist.org/study/scriptures/
        2. URL_VOLUME               dc-testament/
        3. URL_BOOK                 dc/
        3. URL_VERSE                3.18?
        4. url_language             lang=eng
        5. URL_VERSE_HIGHLIGHTER    #p18#18
    """
    BASE_URL = 'https://www.churchofjesuschrist.org/study/scriptures/'
    # URL_VOLUME is passed in
    
    if BOOK_URLS[0] == "dc":
        URL_BOOK = BOOK_URLS[0] + "/"
    else:
        URL_BOOK = BOOK_URLS[RANDOM_BOOK] + "/"
    print("DC DEBUG*********************************************")
    print(RANDOM_CHAPTER)
    print(RANDOM_VERSE)
    URL_VERSE = str(RANDOM_CHAPTER + 1) + "." + str(RANDOM_VERSE + 1) + "?"
    url_language = "lang=eng"
    url_VERSE_HIGHLIGHTER = "#p" + str(RANDOM_VERSE + 1) + "#" + str(RANDOM_VERSE + 1)
   

   
    URL_FINAL = BASE_URL + URL_VOLUME + URL_BOOK + URL_VERSE + url_language + url_VERSE_HIGHLIGHTER
    print("DC DEBUG*********************************************")
    return URL_FINAL


def getScripture(volume):
    random.seed()
    isDC = False
    if volume == allScriptures:
        # Verse can be from any of all of the 5 STANDARD WORKS
        volume = volumeFinder()

    if volume == oldTestament:
        # OLD TESTAMENT
        TOTAL_VERSES = TOTAL_OT_VERSES
        getBookFinder = getOldTestamentBookFinder()
        jsonVolumeFile = OT_JSON
        URL_VOLUME = "ot/"
        BOOK_URLS = OT_URLS
    elif volume == newTestament:
        # NEW TESTAMENT
        TOTAL_VERSES = TOTAL_NT_VERSES
        getBookFinder = getNewTestamentBookFinder()
        jsonVolumeFile = NT_JSON
        URL_VOLUME = "nt/"
        BOOK_URLS = NT_URLS
    elif volume == bookOfMormon:
        # BOOK OF MORMON
        TOTAL_VERSES = TOTAL_BOM_VERSES
        getBookFinder = getBookOfMormonBookFinder()
        jsonVolumeFile = BOM_JSON
        URL_VOLUME = "bofm/"
        BOOK_URLS = BOM_URLS
    elif volume == doctrineAndCovenants:
        # DOCTRINE AND COVENANTS
        TOTAL_VERSES = TOTAL_DC_VERSES
        getBookFinder = getDoctrineAndCovenantsBookFinder()
        jsonVolumeFile = DC_JSON
        URL_VOLUME = "dc-testament/"
        BOOK_URLS = DC_URLS
        isDC = True
    elif volume == pearlOfGreatPrice:
        # PEARL OF GREAT PRICE
        TOTAL_VERSES = TOTAL_PGP_VERSES
        getBookFinder = getPearlOfGreatPriceBookFinder()
        jsonVolumeFile = PGP_JSON
        URL_VOLUME = "pgp/"
        BOOK_URLS = PGP_URLS
    else:
        # This is an error condition!
        print("Invalid volume received in function: getScripture, volume: " + volume)
        RANDOM_BOOK = "INVALID VOLUME ERROR" 


    volumeData = json.load(open(jsonVolumeFile, 'r',encoding='utf8'))
    #print("volumeData: " + str(type(volumeData)))
    #print(volumeData)
    RANDOM_BOOK = getRandomBook(TOTAL_VERSES, getBookFinder)
    print("random book: " + str(RANDOM_BOOK))

    RANDOM_CHAPTER = pseudoGetRandomChapter(RANDOM_BOOK, volumeData, isDC)
    VERSE_INFO = pseudoGetRandomVerse(RANDOM_BOOK, RANDOM_CHAPTER, volumeData, isDC)
    RANDOM_VERSE = VERSE_INFO[0]
    VERSE_REFERENCE = VERSE_INFO[1]['reference']
    VERSE_TEXT = VERSE_INFO[1]['text']
    
    LINK_TO_VERSE = generateLinkToVerse(URL_VOLUME, RANDOM_BOOK, BOOK_URLS, RANDOM_CHAPTER, RANDOM_VERSE)





    

    result = [
        RANDOM_BOOK,
        RANDOM_CHAPTER,
        RANDOM_VERSE,
        VERSE_REFERENCE,
        VERSE_TEXT,
        LINK_TO_VERSE,
        volume,
    ]
    print(result)
    return result

