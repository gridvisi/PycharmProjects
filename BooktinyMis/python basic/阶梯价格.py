
def prices(n):
    priceMap = [
        {'min':1,
         'max':5,
         'price':5},

        {'min': 6,
         'max': 20,
         'price':4.5},

        {'min': 21,
         'max': 50,
         'price': 3.5},

        {'min': 51,
         'max': float('inf'),
         'price': 2.5},
            ]
    for p in priceMap:
        if n >= p['min'] and n <= p['max']:
            return n * p['price']

n = 1000
print(prices(n))