from collections import Counter


COST = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

OFFERS = {
    # Order offers by best value
    "A": [
        (5, 200),
        (3, 130),
    ],
    "B": [(2, 45)],
    "F": [(3, 20)],  # implementation and marketing can be independent..
    "H": [(10, 80), (5, 45)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)],
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter(skus)

    # requirement likely to change, so let's go with easiest approach for now
    free_bs = counter["E"] // 2
    counter["B"] = max(counter["B"] - free_bs, 0)

    total_cost = 0

    for sku, count in counter.items():
        remaining = count

        if sku in OFFERS:
            for amount, offer_cost in OFFERS[sku]:
                if remaining >= amount:
                    offer_count = remaining // amount
                    remaining -= offer_count * amount
                    total_cost += offer_cost * offer_count

        if remaining > 0:
            try:
                total_cost += COST[sku] * remaining
            except KeyError:
                return -1
    return total_cost






