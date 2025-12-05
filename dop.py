#класс буфет , метод добавить блюдо, удалить, (цена и блюдо), составить заказ и чек  .добавить чтб количество в выборе было и можно было выбирать сколько штук в заказ
class ProductError(Exception):
    pass

class ProductNotFound(ProductError):
    pass

class InvalidPrice(ProductError):
    pass

class NotEnoughQuantity(ProductError):
    pass

class Product:
    def __init__(self, name: str, price: float, kolvo: int):
        if price < 0:
            raise InvalidPrice("цена не может быть отрицательной")
        if kolvo < 0:
            raise ValueError("количество не может быть отрицательным")

        self.name = name
        self.price = price
        self.kolvo = kolvo

    def __str__(self):
        return f"{self.name} — {self.price} руб ({self.kolvo} шт)"

    def reduce_quantity(self, amount: int):
        if amount > self.kolvo:
            raise NotEnoughQuantity(f"недостаточно товара '{self.name}'")
        self.kolvo -= amount

    def increase_quantity(self, amount: int):
        self.kolvo += amount


class Buffet:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        for item in self.items:
            if item.name == product.name:
                item.increase_quantity(product.kolvo)
                return
        self.items.append(product)

    def remove_product(self, name: str):
        for i, p in enumerate(self.items):
            if p.name == name:
                del self.items[i]
                return
        raise ProductNotFound(f"товар '{name}' не найден")

    def list_products(self):
        if not self.items:
            print("буфет пуст")
            return
        print("Список товаров:")
        for i, p in enumerate(self.items, 1):
            print(f"{i}. {p}")

    def make_order(self):
        if not self.items:
            print("буфет пуст")
            return
        
        order_items = []
        
        while True:
            self.list_products()
            choice = input("\nНомер товара (или 0): ")
            
            if choice == '0':
                break
            
            try:
                i = int(choice) - 1
                if 0 <= i < len(self.items):
                    product = self.items[i]
                    
                    if product.kolvo <= 0:
                        print(f"'{product.name}' нет в наличии")
                        continue
                    
                    quantity = int(input(f"Сколько штук? (доступно {product.kolvo}): "))
                    
                    if quantity <= 0:
                        print("Количество должно быть > 0")
                        continue
                        
                    if quantity > product.kolvo:
                        print(f"Недостаточно! Доступно {product.kolvo}")
                        continue
                    
                    order_items.append((product, quantity))
                    print(f"Добавлено: {product.name} - {quantity} шт")
                    
                else:
                    print("Неверный номер")
            except ValueError:
                print("Введите число")
            except Exception as e:
                print(f"Ошибка: {e}")
        
        if order_items:
            print("\nВаш заказ:")
            total_price = 0
            total_items = 0
            
            for product, quantity in order_items:
                item_total = product.price * quantity
                product.reduce_quantity(quantity)
                print(f" {product.name} - {quantity} шт × {product.price} = {item_total} руб")
                total_price += item_total
                total_items += quantity
            
            print(f"Итого: {total_items} товаров на {total_price} руб.")


def main():
    buf = Buffet()

    while True:
        print("""
=== МЕНЮ ===
1. Добавить товар
2. Удалить товар
3. Показать товары
4. Составить заказ
0. Выход
""")
        choice = input("Ваш выбор: ")

        try:
            if choice == "1":
                name = input("Название товара: ")
                price = float(input("Цена: "))
                kolvo = int(input("Количество: "))
                buf.add_product(Product(name, price, kolvo))

            elif choice == "2":
                name = input("Название товара для удаления: ")
                buf.remove_product(name)

            elif choice == "3":
                buf.list_products()

            elif choice == "4":
                buf.make_order()   

            elif choice == "0":
                break

            else:
                print("неверный пункт меню")

        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()