# Description: Randomizes the cohort then pairs two of them together. 
# Whoever is left is solo
import random

Cohort = ["Aidan", "Asanda", "Cadee", "Courtney", "Ethan", "Lindo", "Phomello", "Ronny", "Sibu", "Tom", "Ulrich", "Mieke"]
random.shuffle(Cohort)

# Pair students together
pairs = []
while len(Cohort) > 1:
    pair = (Cohort.pop(), Cohort.pop())
    pairs.append(pair)

# If there's an odd number of students, the last one is left alone
left_alone = Cohort[0] if Cohort else None

# Print the pairs and the student left alone
for pair in pairs:
    print(f"Pair: {pair[0]} with {pair[1]}")

if left_alone:
    print(f"Solo: {left_alone}")
