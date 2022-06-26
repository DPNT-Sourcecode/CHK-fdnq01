

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    cost = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }
    try:
        return sum([cost[sku] for sku in skus])
    except KeyError:
        return -1

