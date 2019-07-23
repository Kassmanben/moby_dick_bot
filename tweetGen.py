import markovify
from random import randrange

chapters = ["LOOMINGS", "THE CARPET-BAG", "THE SPOUTER-INN", "THE COUNTERPANE", "BREAKFAST", "THE STREET", "THE CHAPEL",
            "THE PULPIT", "THE SERMON", "A BOSOM FRIEND", "NIGHTGOWN", "BIOGRAPHICAL", "WHEELBARROW", "NANTUCKET",
            "CHOWDER", "THE SHIP", "THE RAMADAN", "HIS MARK", "THE PROPHET", "ALL ASTIR", "GOING ABOARD",
            "MERRY CHRISTMAS", "THE LEE SHORE", "THE ADVOCATE", "POSTSCRIPT", "KNIGHTS AND SQUIRES",
            "KNIGHTS AND SQUIRES", "AHAB", "ENTER AHAB; TO HIM", " STUBB", "THE PIPE", "QUEEN MAB", "CETOLOGY",
            "THE SPECKSYNDER", "THE CABIN-TABLE", "THE MAST-HEAD", "THE QUARTER-DECK", "SUNSET", "DUSK",
            "FIRST NIGHT-WATCH", "MIDNIGHT", " FORECASTLE", "MOBY DICK", "THE WHITENESS OF THE WHALE", "HARK!",
            "THE CHART", "THE AFFIDAVIT", "SURMISES", "THE MAT-MAKER", "THE FIRST LOWERING", "THE HYENA",
            "AHAB'S BOAT AND CREW. FEDALLAH", "THE SPIRIT-SPOUT", "THE ALBATROSS", "THE GAM", "THE TOWN-HO'S STORY",
            "OF THE MONSTROUS PICTURES OF WHALES", "OF THE LESS ERRONEOUS PICTURES OF WHALES",
            " AND TH EPICTURES OF WHALING SCENES",
            "OF WHALES IN PAINT; IN TEETH; IN WOOD; IN SHEET; IN STONE; IN MOUNTAINS; IN STARS", "BRIT", "SQUID",
            "THE LINE", "STUBB KILLS A WHALE", "THE DART", "THE CROTCH", "STUBB'S SUPPER", "THE WHALE AS A DISH",
            "THE SHARK MASSACRE", "CUTTING IN", "THE BLANKET", "THE FUNERAL", "THE SPHYNX", "THE JEROBOAM'S STORY",
            "THE MONKEY ROPE", "STUBB AND FLASK KILL A RIGHT WHALE; AND THEN HAVE OVER HIM",
            "THE SPERM WHALE'S HEAD-CONTRASTED VIEW", "THE RIGHT WHALE'S HEAD-CONTRASTED VIEW", "THE BATTERING-RAM",
            "THE GREAT HEIDELBURGH TUN", "CISTERN AND BUCKETS", "THE PRAIRE", "THE NUT", "THE PEQUOD MEETS THE VIRGIN",
            "THE HONOR AND GLORY OF WHALING", "JONAH HISTORICALLY REGARDED", "PITCHPOLING", "THE FOUNTAIN", "THE TAIL",
            "THE GRAND ARMADA", "SCHOOLS AND SCHOOLMASTERS", "FAST-FISH AND LOOSE-FISH", "HEADS OR TAILS",
            "THE PEQUOD MEETS THE ROSE-BUD", "AMBERGRIS", "THE CASTAWAY", "A SQUEEZE OF THE HAND", "THE CASSOCK",
            "THE TRY-WORKS", "THE LAMP", "STOWING DOWN AND CLEARING UP", "THE DOUBLOON", "LEG AND ARM THE PEQUOD",
            " OF NANTUCKET", " MEETS THE ENDERBY", " OF LONDON", "THE DECANTER", "A BOWER IN THE ARSACIDES",
            "MEASUREMENT OF THE WHALE'S SKELETON", "THE FOSSIL WHALE",
            "DOES THE WHALE'S MAGNITUDE DIMINISH? WILL HE PERISH?", "AHAB'S LEG", "THE CARPENTER",
            "AHAB AND THE CARPENTER", "AHAB AND STARBUCK IN THE CABIN", "QUEEQUEG IN HIS COFFIN", "THE PACIFIC",
            "THE BLACKSMITH", "THE FORGE", "THE GILDER", "THE PEQUOD MEETS THE BACHELOR", "THE DYING WHALE",
            "THE WHALE WATCH", "THE QUADRANT", "THE CANDLES", "THE DECK TOWARDS THE END OF THE FIRST WATCH",
            "MIDNIGHT-THE FORECASTLE BULWARKS", "MIDNIGHT ALOFT-THUNDER AND LIGHTNING", "THE MUSKET", "THE NEEDLE",
            "THE LOG AND LINE", "THE LIFE-BUOY", "THE DECK", "THE PEQUOD MEETS THE RACHEL", "THE CABIN", "THE HAT",
            "THE PEQUOD MEETS THE DELIGHT", "THE SYMPHONY", "THE CHASE-FIRST DAY", "THE CHASE-SECOND DAY",
            "THE CHASE-THIRD DAY", "EPILOGUE"]

def emojiMap(string):
    emojiMap = {
        "sperm whale": "🐳",
        "whale": "🐳",
        "ship":"🚢",
        "boat": "⛵",
        "ocean": "🌊",
        "sea": "🌊",
    }

    return_str = ""
    for word in string.split(" "):
        if word.lower().replace(";","").replace(".","").replace("?","").replace("!","") in emojiMap:
            return_str += emojiMap[word.lower().replace(";","").replace(".","").replace("?","").replace("!","")] + " "
        else:
            return_str += word + " "
    return return_str

# Get raw text as string.
filename = "mobydick.txt";
with open(filename) as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=3)
f = open("tweets.txt", "w+")
for i in range(50000):
    print(50000 - i)
    chapter = "Chapter " + str(randrange(101)) + " - " + chapters[randrange(len(chapters))]
    f.write(chapter + "\n" + emojiMap(text_model.make_short_sentence(183)) + "\n")

f.close()
