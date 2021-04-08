# The final project in the Functions, Files, and Dictionaries course from this specialization

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']       # Will be used to remove punctuation from tweets

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:       # This is a placeholder file. This section creates a list of positive words from a text file
    for lin in pos_f:                     
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:       # This is also a placeholder file. This does the same but with negative words
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):                    # This removes all punctuation from each word, we will use this in later functions
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

def get_pos(sentence):                          # Here we get the positive score of any particular tweet via accumulation - it gets a point for each word in the tweet 
    accum = 0                                   # that is also found in the positive_words list
    words = list(sentence.split())
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            accum += 1
    accum_pos = accum
    return accum_pos

def get_neg(sentence):                          # Likewise here, except with a negative score, referencing the negative_words list
    accum = 0
    words = list(sentence.split())
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            accum += 1
    accum_neg = accum
    return accum_neg

fileref = open("project_twitter_data.csv", "r") # We are pulling the tweets from this csv file
data = fileref.readlines()
    
filewr = open("resulting_data.csv", "w")        # Creating a new file to write to                                                   
filewr.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")    # This is the header 
filewr.write("\n")

for i in data[1:]:                              # This for loop grabs each tweet (line) in the data file and applies our functions to it, then formats the output into csv format
    item = i.strip().split(',')                 # and writes it to the new file.
    item_entry = ("{},{},{},{},{}".format(item[1], item[2], get_pos(item[0]), get_neg(item[0]), (get_pos(item[0])-get_neg(item[0]))))
    filewr.write(item_entry)
    filewr.write('\n')
    
filewr.close()
