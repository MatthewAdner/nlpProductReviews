# imports libraries
from typing import Text
from nltk.util import pr
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import math

# prints out polarity and subjectivity subjectivity is how subjective/objective it is, polarity is positive or negative
testimonial = TextBlob("Text blob is a library.")
print(testimonial.sentiment)

# tests a negative statement for polarity (postive/negative sentiment)
negTesti = TextBlob("I hate text blob and it is terrible! Who would ever use something so terrible as text blob?!")
print(f"negTesti is {negTesti.sentiment.polarity}")

# tests a positive statement for polarity
postesti = TextBlob("Text blob is great! I love it!")
print(f"posTesti is {postesti.sentiment.polarity}")

x = np.array(range(-50, 50))
y = 26*x
plt.plot(x, y)
plt.show()