from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import csv
toRemove = []


#rows = csv.reader(open("Amazon_Unlocked_Mobile_without_duplicates.csv", "r"))

rows = pd.read_csv("Amazon_Unlocked_Mobile_without_duplicates.csv")



#print(rows)
print(type(rows))

'''for first in rows:
    for second in rows:
        if fuzz.token_sort_ratio(first, second) < 80:
            first.pop()'''


'''for i in range(len(rows)):
    for j in range(len(rows)):
        j += i + 1
        if fuzz.token_sort_ratio(rows[i], rows[j]) < 80:
            toRemove.append(i)'''

print(toRemove)




'''newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("file.csv", "wb"))
writer.writerows(newrows)'''