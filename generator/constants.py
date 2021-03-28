
#VOLUMES ------------------------------------------------------
oldTestament = "Old Testament"
newTestament = "New Testament"
bookOfMormon = "Book of Mormon"
doctrineAndCovenants = "Doctrine and Covenants"
pearlOfGreatPrice = "Pearl of Great Price"

#BOOKS ------------------------------------------------------
#OLD TESTAMENT
genesis = "genesis"
exodus = "exodus"
leviticus = "leviticus"
numbers = "numbers"
deuteronomy = "deuteronoy"
joshua = "joshua"
judges = "judges"
ruth = "ruth"
oneSamuel = "oneSamuel"
twoSamuel = "twoSamuel"
oneKings = "oneKings"
twoKings = "twoKings"
oneChronicles = "oneChronicles"
twoChronicles = "twoChronicles"
ezra = "ezra"
nehemiah = "nehemiah"
esther  = "esther"
job = "job"
psalms = "psalms"
proverbs = "proverbs"
ecclesiastes = "ecclesiastes"
songOfSolomon = "songOfSolomon"
isaiah = "isaiah"
jeremiah = "jeremiah"
lamentations = "lamentations"
ezekiel = "ezekiel"
daniel = "daniel"
hosea = "hosea"
joel = "joel"
amos = "amos"
obadiah = "obadiah"
jonah = "jonah"
micah = "micah"
nahum = "nahum"
habakkuk = "habakkuk"
zephaniah = "zephaniah"
haggai = "haggai"
zechariah = "zechariah"

#NEW TESTAMENT
malachi = "malachi"
matthew = "matthew"
mark = "mark"
luke = "luke"
john = "john"
acts = "acts"
romans = "romans"
oneCorinthians = "oneCorinthians"
twoCorinthians  = "twoCorinthians"
galatians = "galatians"
ephesians  = "ephesians"
philippians  = "philippians"
colossians  = "colossians"
oneThessalonians = "oneThessalonians"
twoThessalonians = "twoThessalonians"
oneTimothy  = "oneTimothy"
twoTimothy = "twoTimothy"
titus  = "titus"
philemon  = "philemon"
hebrews  = "hebrews"
james  = "james"
onePeter = "onePeter"
twoPeter  = "twoPeter"
oneJohn = "oneJohn"
twoJohn = "twoJohn"
threeJohn  = "threeJohn"
jude  = "jude"
revelation = "revelation"

#BOOK OF MORMON
oneNephi = "oneNephi"
twoNephi = "twoNephi"
jacob = "jacob"
enos = "enos"
jarom = "jarom"
omni = "omni"
wordsOfMormon = "wordsOfMormon"
mosiah = "mosiah"
alma = "alma"
helaman = "helaman"
threeNephi = "threeNephi"
fourNephi = "fourNephi"
mormon = "mormon"
ether = "ether"
moroni = "moroni"

#PEARL OF GREAT PRICE
moses = "moses"
abraham = "Abraham"
josephSmithMatthew = "josephSmithMatthew"
josephSmithHistory = "josephSmithHistory"
articlesOfFaith = "articlesOfFaith"

#JSON FILES ------------------------------------------------------
BOM_JSON = 'book-of-mormon.json'
DC_JSON = 'doctrine-and-covenants.json'
PGP_JSON = 'pearl-of-great-price.json'
NT_JSON = 'new-testament.json'
OT_JSON = 'old-testament.json'

#TOTALS ------------------------------------------------------
TOTAL_OT_VERSES = 23145
TOTAL_OT_CHAPTERS = 929

TOTAL_NT_VERSES = 7958
TOTAL_NT_VERSES = 260

TOTAL_BOM_VERSES = 6604

TOTAL_DC_VERSES = 3654
TOTAL_DC_SECTIONS = 138

TOTAL_PGP_VERSES = 635
TOTAL_PGP_VERSES = 16


#DICTIONARIES ------------------------------------------------------
numVersesInBook = {
    "oneNephi" :618,
    "twoNephi" : 779,
    "jacob" : 203,
    "enos" : 27,
    "jarom" : 15,
    "omni" : 30,
    "wordsOfMormon" : 18,
    "mosiah" : 785,
    "alma" : 1975,
    "helaman" : 497,
    "threeNephi" : 785,
    "fourNephi" : 49,
    "mormon" : 227,
    "ether" : 433,
    "moroni" : 163,
}
numChaptersInBook = {
    "oneNephi" : 22,
    "twoNephi" : 33,
    "jacob" : 7,
    "enos" : 1,
    "jarom" : 1,
    "omni" : 1,
    "wordsOfMormon" : 1,
    "mosiah" : 29,
    "alma" : 63,
    "helaman" : 16,
    "threeNephi" : 30,
    "fourNephi" : 1,
    "mormon" : 9,
    "ether" : 15,
    "moroni" : 10,
}
totalVerseBookIndex = {
    "oneNephi" :618,
    "twoNephi" : 1397,
    "jacob" : 1600,
    "enos" : 1627,
    "jarom" : 1642,
    "omni" : 1672,
    "wordsOfMormon" : 1690,
    "mosiah" : 2475,
    "alma" : 4450,
    "helaman" : 4947,
    "threeNephi" : 5732,
    "fourNephi" : 5781,
    "mormon" : 6008,
    "ether" : 6441,
    "moroni" : 6604,
}

#SPECIAL DICTIONARIES ------------------------------------------------------

class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range): # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) # or super(RangeDict, self) for Python 2

def getBookOfMormonBookFinder():
    bookOfMormonBookFinder = RangeDict({
        range(1, 618) : "oneNephi",
        range(618, 1397) : "twoNephi",
        range(1397, 1600) : "jacob",
        range(1600, 1627) : "enos",
        range(1627, 1642) : "jarom",
        range(1642, 1672) : "omni",
        range(1672, 1690) : "wordsOfMormon",
        range(1690, 2475) : "mosiah",
        range(2475, 4450) : "alma",
        range(4450, 4947) : "helaman",
        range(4947, 5732) : "threeNephi",
        range(5732, 5781) : "fourNephi",
        range(5781, 6008) : "mormon",
        range(6008, 6441) : "ether",
        range(6441, 6604) : "moroni",
    })
    return bookOfMormonBookFinder