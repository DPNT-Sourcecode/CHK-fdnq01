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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
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
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)],
}

FREEBIES = {
    "E": (2, "B"),
    "N": (3, "M"),
    "R": (3, "Q"),
}

GROUPS = {
    # Need to sort as some items are better to be in the offer than others
    "".join(sorted(group, key=lambda l: COST[l], reverse=True)): offers
    for group, offers in [
        ("STXYZ", (3, 45))
    ]
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter(skus)
    total_cost = 0

    for offer, (count, freebie) in FREEBIES.items():
        max_free = counter[offer] // count
        counter[freebie] = max(counter[freebie] - max_free, 0)

    for group, (count, cost) in GROUPS.items():
        total_offers = sum(counter[sku] for sku in group) // count
        print("TOTAL OFFERS", total_offers)
        if total_offers == 0:
            continue

        offers_applied = 0
        current_group_count = 0
        sku_index = 0

        while offers_applied < total_offers:
            sku = group[sku_index]
            # this sku can fully consume the remaining group
            if counter[sku] >= current_group_count:
                counter[sku] -= count - current_group_count
                total_cost += cost
                offers_applied = 1
            else:
                current_group_count += counter[sku]
                counter[sku] = 0
                sku_index += 1

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



