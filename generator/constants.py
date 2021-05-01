
#VOLUMES ------------------------------------------------------
oldTestament = "Old Testament"
newTestament = "New Testament"
bookOfMormon = "Book of Mormon"
doctrineAndCovenants = "Doctrine and Covenants"
pearlOfGreatPrice = "Pearl of Great Price"

#BOOK URLS---------------------------------------------------
BOM_URLS = [
    "1-ne",
    "2-ne",
    "jacob",
    "enos",
    "jarom",
    "omni",
    "w-of-m",
    "mosiah",
    "alma",
    "hel",
    "3-ne",
    "4-ne",
    "morm",
    "ether",
    "moro",
]
OT_URLS = [
   "gen",
    "ex",
    "lev",
    "num",
    "deut",
    "josh",
    "judg",
    "ruth",
    "1-sam",
    "2-sam",
    "1-kgs",
    "2-kgs",
    "1-chr",
    "2-chr",
    "ezra",
    "neh",
    "esth",
    "job",
    "ps",
    "prov",
    "eccl",
    "song",
    "isa", 
    "jer",
    "lam",
    "ezek",
    "dan",
    "hosea",
    "joel",
    "amos",
    "obad",
    "jonah",
    "micah",
    "nahum",
    "hab",
    "zeph",
    "hag",
    "zech",
    "mal",
]
NT_URLS = [
    "matt",
    "mark",
    "luke",
    "john",
    "acts",
    "rom",
    "1-cor",
    "2-cor",
    "gal",
    "eph",
    "philip",
    "col",
    "1-thes",
    "2-thes",
    "1-tim",
    "2-tim",
    "titus",
    "philem",
    "heb",
    "james",
    "1-pet",
    "2-pet",
    "1-jn",
    "2-jn",
    "3-jn",
    "jude",
    "rev",

]
DC_URLS = [
    "dc",
]
PGP_URLS = [
    "moses",
    "abr",
    "js-m",
    "js-h",
    "a-of-f",
]


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
PATH_TO_JSON = 'static/'
BOM_JSON = PATH_TO_JSON +  'book-of-mormon.json'
DC_JSON = PATH_TO_JSON + 'doctrine-and-covenants.json'
PGP_JSON = PATH_TO_JSON + 'pearl-of-great-price.json'
NT_JSON = PATH_TO_JSON + 'new-testament.json'
OT_JSON = PATH_TO_JSON + 'old-testament.json'

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
        range(1, 618) : 0,
        range(618, 1397) : 1,
        range(1397, 1600) : 2,
        range(1600, 1627) : 3,
        range(1627, 1642) : 4,
        range(1642, 1672) : 5,
        range(1672, 1690) : 6,
        range(1690, 2475) : 7,
        range(2475, 4450) : 8,
        range(4450, 4947) : 9,
        range(4947, 5732) : 10,
        range(5732, 5781) : 11,
        range(5781, 6008) : 12,
        range(6008, 6441) : 13,
        range(6441, 6604) : 14,
    })
    return bookOfMormonBookFinder

