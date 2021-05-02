
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

def getOldTestamentBookFinder():
    oldTestamentBookFinder = RangeDict({
        range(1, 1533) : 0,
        range(1533, 2746) : 1,
        range(2746, 3605) : 2,
        range(3605, 4893) : 3,
        range(4893, 5852) : 4,
        range(5852, 6510) : 5,
        range(6510, 7128) : 6,
        range(7128, 7213) : 7,
        range(7213, 8023) : 8,
        range(8023, 8718) : 9,
        range(8718, 9534) : 10,
        range(9534, 10253) : 11,
        range(10253, 11195) : 12,
        range(11195, 12017) : 13,
        range(12017, 12297) : 14,
        range(12297, 12703) : 15,
        range(12703, 12870) : 16,
        range(12870, 13940) : 17,
        range(13940, 16401) : 18,
        range(16401, 17316) : 19,
        range(17316, 17538) : 20,
        range(17538, 17655) : 21,
        range(17655, 18947) : 22,
        range(18947, 20311) : 23,
        range(20311, 20465) : 24,
        range(20465, 21738) : 25,
        range(21738, 22095) : 26,
        range(22095, 22292) : 27,
        range(22292, 22365) : 28,
        range(22365, 22511) : 29,
        range(22511, 22532) : 30,
        range(22532, 22580) : 31,
        range(22580, 22685) : 32,
        range(22685, 22732) : 33,
        range(22732, 22788) : 34,
        range(22788, 22841) : 35,
        range(22841, 22879) : 36,
        range(22879, 23090) : 37,
        range(23090, 23145) : 38,
    })
    return oldTestamentBookFinder

def getNewTestamentBookFinder():
    newTestamentBookFinder = RangeDict({
        range(1, 1071) : 0,
        range(1071, 1749) : 1,
        range(1749, 2900) : 2,
        range(2900, 3779) : 3,
        range(3779, 4786) : 4,
        range(4786, 5219) : 5,
        range(5219, 5656) : 6,
        range(5656, 5913) : 7,
        range(5913, 6062) : 8,
        range(6062, 6217) : 9,
        range(6217, 6321) : 10,
        range(6321, 6416) : 11,
        range(6416, 6505) : 12,
        range(6505, 6552) : 13,
        range(6552, 6665) : 14,
        range(6665, 6748) : 15,
        range(6748, 6794) : 16,
        range(6794, 6819) : 17,
        range(6819, 7122) : 18,
        range(7122, 7230) : 19,
        range(7230, 7335) : 20,
        range(7335, 7396) : 21,
        range(7396, 7501) : 22,
        range(7501, 7514) : 23,
        range(7514, 7528) : 24,
        range(7528, 7553) : 25,
        range(7553, 7957) : 26,
    })
    return newTestamentBookFinder

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

def getDoctrineAndCovenantsBookFinder():
    doctrineAndCovenantsBookFinder = RangeDict({
        range(1, 39) : 0,
        range(39, 42) : 1,
        range(42, 62) : 2,
        range(62, 69) : 3,
        range(69, 104) : 4,
        range(104, 141) : 5,
        range(141, 149) : 6,
        range(149, 161) : 7,
        range(161, 175) : 8,
        range(175, 245) : 9,
        range(245, 275) : 10,
        range(275, 284) : 11,
        range(284, 285) : 12,
        range(285, 296) : 13,
        range(296, 302) : 14,
        range(302, 308) : 15,
        range(308, 317) : 16,
        range(317, 364) : 17,
        range(364, 405) : 18,
        range(405, 489) : 19,
        range(489, 501) : 20,
        range(501, 505) : 21,
        range(505, 512) : 22,
        range(512, 531) : 23,
        range(531, 547) : 24,
        range(547, 549) : 25,
        range(549, 567) : 26,
        range(567, 583) : 27,
        range(583, 633) : 28,
        range(633, 644) : 29,
        range(644, 657) : 30,
        range(657, 662) : 31,
        range(662, 680) : 32,
        range(680, 692) : 33,
        range(692, 719) : 34,
        range(719, 727) : 35,
        range(727, 731) : 36,
        range(731, 773) : 37,
        range(773, 797) : 38,
        range(797, 800) : 39,
        range(800, 812) : 40,
        range(812, 905) : 41,
        range(905, 940) : 42,
        range(940, 946) : 43,
        range(946, 1021) : 44,
        range(1021, 1054) : 45,
        range(1054, 1058) : 46,
        range(1058, 1064) : 47,
        range(1064, 1092) : 48,
        range(1092, 1138) : 49,
        range(1138, 1158) : 50,
        range(1158, 1202) : 51,
        range(1202, 1209) : 52,
        range(1209, 1219) : 53,
        range(1219, 1225) : 54,
        range(1225, 1245) : 55,
        range(1245, 1261) : 56,
        range(1261, 1326) : 57,
        range(1326, 1350) : 58,
        range(1350, 1367) : 59,
        range(1367, 1406) : 60,
        range(1406, 1415) : 61,
        range(1415, 1481) : 62,
        range(1481, 1524) : 63,
        range(1524, 1530) : 64,
        range(1530, 1543) : 65,
        range(1543, 1557) : 66,
        range(1557, 1592) : 67,
        range(1592, 1600) : 68,
        range(1600, 1618) : 69,
        range(1618, 1629) : 70,
        range(1629, 1655) : 71,
        range(1655, 1661) : 72,
        range(1661, 1668) : 73,
        range(1668, 1704) : 74,
        range(1704, 1823) : 75,
        range(1823, 1838) : 76,
        range(1838, 1860) : 77,
        range(1860, 1864) : 78,
        range(1864, 1869) : 79,
        range(1869, 1876) : 80,
        range(1876, 1900) : 81,
        range(1900, 1906) : 82,
        range(1906, 2026) : 83,
        range(2026, 2038) : 84,
        range(2038, 2049) : 85,
        range(2049, 2057) : 86,
        range(2057, 2198) : 87,
        range(2198, 2219) : 88,
        range(2219, 2256) : 89,
        range(2256, 2262) : 90,
        range(2262, 2264) : 91,
        range(2264, 2317) : 92,
        range(2317, 2334) : 93,
        range(2334, 2351) : 94,
        range(2351, 2360) : 95,
        range(2360, 2388) : 96,
        range(2388, 2436) : 97,
        range(2436, 2444) : 98,
        range(2444, 2461) : 99,
        range(2461, 2562) : 100,
        range(2562, 2596) : 101,
        range(2596, 2636) : 102,
        range(2636, 2722) : 103,
        range(2722, 2763) : 104,
        range(2763, 2771) : 105,
        range(2771, 2871) : 106,
        range(2871, 2879) : 107,
        range(2879, 2959) : 108,
        range(2959, 2975) : 109,
        range(2975, 2986) : 110,
        range(2986, 3020) : 111,
        range(3020, 3030) : 112,
        range(3030, 3032) : 113,
        range(3032, 3051) : 114,
        range(3051, 3052) : 115,
        range(3052, 3068) : 116,
        range(3068, 3074) : 117,
        range(3074, 3081) : 118,
        range(3081, 3082) : 119,
        range(3082, 3128) : 120,
        range(3128, 3137) : 121,
        range(3137, 3154) : 122,
        range(3154, 3299) : 123,
        range(3299, 3303) : 124,
        range(3303, 3306) : 125,
        range(3306, 3318) : 126,
        range(3318, 3343) : 127,
        range(3343, 3352) : 128,
        range(3352, 3375) : 129,
        range(3375, 3383) : 130,
        range(3383, 3449) : 131,
        range(3449, 3523) : 132,
        range(3523, 3535) : 133,
        range(3535, 3542) : 134,
        range(3542, 3584) : 135,
        range(3584, 3594) : 136,
        range(3594, 3654) : 137,
    })
    return doctrineAndCovenantsBookFinder

def getPearlOfGreatPriceBookFinder():
    pearlOfGreatPriceBookFinder = RangeDict({
        range(1, 356) : 0,
        range(356, 492) : 1,
        range(492, 547) : 2,
        range(547, 622) : 3,
        range(622, 635) : 4,
    })
    return pearlOfGreatPriceBookFinder