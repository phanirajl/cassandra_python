with open("ratingsData.dat", "r") as data:
    lines = [line for line in data]
#Set this number to the number of entries you wish to load into your database
# 0 <numEntries <= 100,000
numEntries =10	
	
import random
random_choice = random.sample(lines, numEntries)

with open("userData.data", "w") as sink:
    sink.write("".join(random_choice))	
