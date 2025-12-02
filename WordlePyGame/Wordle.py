import random
word_bank = word_list = word_list_long = [
    "ABOUT", "ABOVE", "ACTOR", "ADOPT", "ADULT", "ADMIT", "AFTER", "AGAIN",
    "AGREE", "AHEAD", "ALARM", "ALIVE", "ALLOW", "ALONE", "ALONG", "ALTER",
    "AMONG", "ANGLE", "ANGRY", "APART", "APPLE", "APPLY", "ARENA", "ARGUE",
    "ARISE", "ARRAY", "ASIDE", "ASSET", "AUDIO", "AUDIT", "AVOID", "AWARD",
    "AWARE", "BADGE", "BASIC", "BASIS", "BEACH", "BEGIN", "BELOW", "BENCH",
    "BLADE", "BLANK", "BLOCK", "BLOOD", "BOARD", "BRAIN", "BRAND", "BREAK",
    "BREAD", "BRICK", "BRIEF", "BRING", "BROAD", "BROWN", "BUYER", "CABLE",
    "CARRY", "CATCH", "CAUSE", "CEASE", "CHAIN", "CHAIR", "CHEST", "CHIEF",
    "CHILD", "CHINA", "CHOKE", "CIVIL", "CLAIM", "CLASS", "CLEAN", "CLEAR",
    "CLICK", "CLOCK", "CLOSE", "CLOUD", "COACH", "COAST", "COLOR", "COMMA",
    "COURT", "COVER", "CRACK", "CRIME", "CROSS", "CROWD", "CROWN", "CYCLE",
    "DANCE", "DEATH", "DELAY", "DEPTH", "DIRTY", "DOUBT", "DOZEN", "DRAFT",
    "DRAMA", "DRAWN", "DREAM", "DRINK", "DRIVE", "EAGER", "EARLY", "EARTH",
    "EIGHT", "ELECT", "EMPTY", "ENEMY", "ENTRY", "EQUAL", "ERROR", "ESSAY",
    "EVENT", "EVERY", "EXACT", "EXIST", "EXTRA", "FAITH", "FALSE", "FAULT",
    "FIBER", "FIELD", "FIFTY", "FIGHT", "FINAL", "FIRST", "FIXED", "FLASH",
    "FLEET", "FLOOR", "FLUID", "FOCUS", "FORCE", "FORTH", "FORTY", "FORUM",
    "FOUND", "FRAME", "FRESH", "FRONT", "FRUIT", "FULLY", "FUNNY", "GIANT",
    "GIVEN", "GLASS", "GLOBE", "GOING", "GRACE", "GRADE", "GRAND", "GRANT",
    "GRASS", "GREAT", "GREEN", "GROSS", "GROUP", "GUEST", "GUIDE", "HABIT",
    "HANDY", "HAPPY", "HEART", "HEAVY", "HELLO", "HENCE", "HORSE", "HOTEL",
    "HOURS", "HOUSE", "HUMAN", "IDEAL", "IMAGE", "INDEX", "INNER", "INPUT",
    "ISSUE", "JOINT", "JUDGE", "KNOCK", "LABEL", "LARGE", "LASER", "LATER",
    "LAUGH", "LAYER", "LEARN", "LEAVE", "LEGAL", "LEVEL", "LIGHT", "LIMIT",
    "LOCAL", "LOOSE", "LOVER", "LOWER", "LUCKY", "LUNCH", "MAJOR", "MAKER",
    "MARCH", "MATCH", "MAXIM", "MAYBE", "MEANT", "MEDIA", "MERCY", "METAL",
    "MIGHT", "MINOR", "MINUS", "MIXED", "MODEL", "MONEY", "MONTH", "MORAL",
    "MOTOR", "MOUNT", "MOUSE", "MOUTH", "MOVIE", "NAKED", "NAVEL", "NEEDS",
    "NERVO", "NEVER", "NOBLE", "NOISE", "NORTH", "NOTED", "NOVEL", "NURSE",
    "OCEAN", "OFFER", "OFFIC", "ONION", "OPERA", "ORDER", "OTHER", "OUGHT",
    "OWNER", "PAINT", "PANEL", "PAPER", "PARTY", "PATCH", "PAUSE", "PEACE",
    "PHASE", "PHONE", "PHOTO", "PIECE", "PILOT", "PITCH", "PLACE", "PLAIN",
    "PLANE", "PLANT", "PLATE", "POINT", "POWER", "PRESS", "PRICE", "PRIME",
    "PRIZE", "PROOF", "PROUD", "PROVE", "QUEEN", "QUICK", "QUIET", "QUITE",
    "RADIO", "RANGE", "RATIO", "REACH", "REFER", "RIGHT", "RIVER", "ROBOT",
    "ROUGH", "ROUND", "ROUTE", "ROYAL", "RULER", "RURAL", "SALAD", "SCOPE",
    "SCORE", "SENSE", "SERVE", "SEVEN", "SHADE", "SHAKE", "SHALL", "SHAPE",
    "SHARE", "SHARP", "SHEET", "SHELF", "SHELL", "SHIFT", "SHIRT", "SHOCK",
    "SHOOT", "SHORT", "SHOWN", "SIGHT", "SINCE", "SIXTH", "SMALL", "SMART",
    "SMILE", "SMOKE", "SOUND", "SOUTH", "SPACE", "SPEAK", "SPEED", "SPEND",
    "SPLIT", "SPORT", "STAFF", "STAGE", "STAND", "START", "STATE", "STEEL",
    "STICK", "STILL", "STOCK", "STONE", "STORE", "STORM", "STORY", "STRIP",
    "STUDY", "SUGAR", "SUITE", "SUPER", "SWEET", "TABLE", "TASTE", "TEACH",
    "THEIR", "THEME", "THERE", "THICK", "THING", "THINK", "THIRD", "THREE",
    "THROW", "TIGHT", "TIMES", "TITLE", "TODAY", "TOPIC", "TOTAL", "TOUCH",
    "TOUGH", "TOWER", "TRACK", "TRADE", "TRAIN", "TREAT", "TREND", "TRIAL",
    "TRUCK", "TRULY", "TRUST", "TRUTH", "TWICE", "UNDER", "UNION", "UNITY",
    "UNTIL", "UPPER", "URBAN", "USAGE", "USUAL", "VALUE", "VIDEO", "VISIT",
    "VITAL", "VOICE", "WASTE", "WATCH", "WATER", "WEIGH", "WHEEL", "WHERE",
    "WHICH", "WHILE", "WHITE", "WHOLE", "WOMAN", "WORLD", "WORRY", "WORTH",
    "WOULD", "WOUND", "WRITE", "WRONG", "YIELD", "YOUNG", "YOUTH"
]
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))
  guess = input('Guess a letter: ').lower()
  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break
if attempts == 0 and '_' in guessedWord:
  print('\nYou\'ve run out of attempts! The word was: ' + word)


