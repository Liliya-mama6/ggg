from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name=name
        self.weight=weight
        self.category=category

    def __str__(self):
        return f'{self.name}, {str(self.weight)}, {self.category}'

class Shop:
    __file_name='products.txt'
    def add(self, *products):
        for i in range(len(products)):
            file=open(self.__file_name, 'r')
            s=file.read()
            file.close()
            if s=='':
                file=open(self.__file_name, 'w')
                file.write(str(products[i]))
                file.close()
            elif s!='' and s.count(str(products[i]))==0:
                file = open(self.__file_name, 'a')
                file.write('\n'+str(products[i]))
                file.close()
            elif s!='' and s.count(str(products[i]))>0:
                print(f'Продукт {str(products[i].name)} уже есть в магазине')

    def get_products(self):
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        file = open(self.__file_name, 'w')
        file.write(s)
        file.close()
        return s


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
file=open('products.txt', 'r')
file.read()
