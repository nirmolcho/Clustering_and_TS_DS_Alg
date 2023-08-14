class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
        }
