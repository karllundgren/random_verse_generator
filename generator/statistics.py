import json
import random
from bom_verse_generator import getBook
from .constants import *
random.seed()

# STATISTICS Calculations****************************************************************
bookSpread = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}


iterations = 100000
for i in range(iterations):
    book = getRandomBook()
    #print(book)
    bookSpread[book] += 1
print("Total spread\n")
for key, value in bookSpread.items():
    print(totalVerseBookIndex[key] + ", " + str(value))
print("*******************************\n\n")

print("What the percentage of hits should be\n")
for key, value in numVersesInBook.items():
    TOTAL_BOM_VERSES = 6604
    print(key + ": " + str(value/TOTAL_BOM_VERSES))
print("*******************************\n\n")

print("What the percentage of hits ACTUALLY is\n")
for key, value in bookSpread.items():
    print(totalVerseBookIndex[key] + ": " + str(value/iterations))
print("*******************************\n\n")
#****************************************************************************************



