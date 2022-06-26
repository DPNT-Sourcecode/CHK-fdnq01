from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    cost = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }
    offers = {
        # Order offers by best value
        "A": [
            (5, 200),
            (3, 130),
        ],
        "B": [(2, 45)],
    }
    counter = Counter(skus)
    total_cost = 0

    for sku, count in counter.items():
        remaining = count

        if sku in offers:
            for amount, offer_cost in offers[sku]:
                if remaining >= amount:
                    offer_count = remaining // amount
                    remaining -= offer_count * amount
                    total_cost += offer_cost * offer_count

        if remaining > 0:
            try:
                total_cost += cost[sku] * remaining
            except KeyError:
                return -1
    return total_cost

