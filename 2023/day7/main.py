import math
from functools import cmp_to_key
cards = open(0).read().split("\n")
cards = [ card.split()  for card in cards ]
cards = [ (card[0], int(card[1]))  for card in cards ]

leafs = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"][::-1]
leafDict = {
    k: v for v, k in enumerate(leafs)
}
print(leafDict)

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

def getStrength(card):
    counts = {}
    for l in card:
        counts.setdefault(l, 0)
        counts[l]+=1
    countsList = []
    for k, c in counts.items():
        countsList.append((c, k))
    def compare_count_card_combo(card_a, card_b):
        # print(card_a, card_b)
        if card_a[0] != card_b[0]:
            return card_a[0] > card_b[0]
        print(card_a, card_b, leafDict[card_a[1]] < leafDict[card_b[1]])
        return leafDict[card_a[1]] < leafDict[card_b[1]]
    sorted(countsList, key = cmp_to_key(make_comparator(compare_count_card_combo)))
    print(countsList)

for c, bid in cards:
    getStrength(c)