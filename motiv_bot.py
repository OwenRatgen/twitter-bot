import tweepy
import random
import time

# Setting a variable up with their respective keys given from twitter in order to make lines 10-12 work
CONSUMER_KEY = 'iNnCHCS5pjjgKh9hoqJ5psT5P'
CONSUMER_SECRET = 'tJOBLJcFZd7oY5N6mfQyohnbL4KrUj10BSAfAegaE6L3tR0NCm'
ACCESS_KEY = '1394084456181518343-33iN78ZnSMh3996KlMBUUqJUy2Ibof'
ACCESS_SECRET = 'bULYtarfOhy5VvQfEk9enMRYxerFLnnLWc6AjmR9uim1N'

# Setting up auth object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# This api object reads data given from twitter then writes data into twitter (Tweeting and DMing)
api = tweepy.API(auth)


# The keyword will be used to check if the keyword is in any of the mentioned tweets
keyword = "motivation"
id_file_name = 'most_recent_id.txt'
quote_file_name = 'motiv_quotes.txt'

# These functions are used so we can store the tweet id and overwrite it with a newer
# tweet id so we don't keep going back to the first couple of tweets each time we want
# to loop through the mentions

def use_recent_id(id_file_name):

    '''
    Purpose: To read what the most recent tweet id is and use it
    Variables: file_name = the name of the file we are reading from
    Return: The tweet id that is set to a new variable
    '''

    f = open(id_file_name, 'r')
    most_recent_id = f.read()
    f.close()
    return most_recent_id

def write_recent_id(most_recent_id, id_file_name):
    '''
    Purpose: To overwrite the previous twitter id with the newest twitter id
    Variables:
    id_file_name = the name of the file we are reading from
    most_recent_id = the newest tweet id that will be written into the file_name file
    Return: None
    '''

    f = open(id_file_name, 'w')
    f.write(str(most_recent_id))
    f.close()

# Whenever the twitter bot sees that it is mentioned in a tweet, it will call
# this fucntion which will give it a random quote from a text file that I made
def get_ran_quote(quote_file_name):
    '''
    Purpose: To overwrite the previous twitter id with the newest twitter id
    Variables:
    quote_file_name = the name of the file we are reading from
    Return: A randomly selected quote from a text file
    '''
    line_num = random.randint(1, 36)
    f = open(quote_file_name, 'r')
    # for line in f.readlines():
    #     print(line)
    lines = f.readlines()
    quote = lines[line_num].rstrip("\n")
    return quote

def tweet_reply():

# This stores the most recent tweet id
    most_recent_id = use_recent_id(id_file_name)

# Setting a variable equal to the command that extracts all of the Tweets that mentions
# the developer's Twitter account and it also makes it so the newest/highest tweet id will
# only be used. This is so everytime we want to loop through the mentions, the bot will reply
# to the newer tweets by checking the tweet id
    mentions = api.mentions_timeline(most_recent_id)

# The for loop, loops through each singular tweet that mentions the bot and converts the tweet to lowercase in order to check for the keyword
# If the keyword is in the tweet, the bot will reply with a randomly selected motivational quote
# Line 69 calls the write_recent_id because it is going to replace the older tweet id with
#the newer one so the bot only reads the newest tweets that it is mentioned in

    for tweet in reversed(mentions):
        text = tweet.text.lower()
        most_recent_id = tweet.id
        write_recent_id(most_recent_id, id_file_name)
        print(text)
        print(keyword)
        quote_use = get_ran_quote(quote_file_name)
        if keyword in text:
            api.update_status("" + quote_use, most_recent_id, True)

# This infinite loops makes it so the twitter bot is checking for any new mention forever

while True:
    tweet_reply()
    time.sleep(15)
