class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        try:
            open(self.__file_name, 'x').close()
        except FileExistsError:
            pass
    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()
    def add(self, *products):
        ex_products = set()
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                ex_products.add(line.strip())
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if str(product) in ex_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product)+'\n')
                    ex_products.add(line.strip())
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__



s1.add(p1, p2, p3)



print(s1.get_products())