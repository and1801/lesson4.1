class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"


# Создание объектов класса Store
store1 = Store("Магазин №1", "Улица Пушкина, 10")
store2 = Store("Магазин №2", "Улица Лермонтова, 15")
store3 = Store("Магазин №3", "Улица Чехова, 20")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("milk", 1.2)
store2.add_item("bread", 0.8)

store3.add_item("chocolate", 1.5)
store3.add_item("cheese", 2.5)

# Тестирование методов магазина
print(store1)
store1.add_item("oranges", 0.6)
print("\nПосле добавления товара 'oranges':")
print(store1)

store1.update_price("apples", 0.55)
print("\nПосле обновления цены на 'apples':")
print(store1)

print("\nЦена на 'bananas':", store1.get_price("bananas"))

store1.remove_item("bananas")
print("\nПосле удаления товара 'bananas':")
print(store1)