from typing import Text
from nltk.util import pr
from textblob import TextBlob
testimonial = TextBlob("Text blob is a library.")
print(testimonial.sentiment)
negTesti = TextBlob("I hate text blob and it is terrible! Who would ever use something so terrible as text blob?!")
print(f"negTesti is {negTesti.sentiment.polarity}")
postesti = TextBlob("Text blob is great! I love it!")
print(f"posTesti is {postesti.sentiment.polarity}")