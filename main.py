from collections import namedtuple

# Asosiy NamedTuple sinflar
BaseProduct = namedtuple('Product', ['id', 'name', 'price'])
BaseUser = namedtuple('User', ['id', 'name', 'email'])

# Metod qo'shish uchun yangi sinflar
class Product(BaseProduct):
    def get_discount_price(self, discount_percentage):
        """Chegirma hisoblab narxni qaytaradi."""
        discount = self.price * discount_percentage / 100
        return self.price - discount

class User(BaseUser):
    def display_user_info(self):
        """Foydalanuvchi haqida ma'lumotni qaytaradi."""
        return f"User ID: {self.id}, Name: {self.name}, Email: {self.email}"

# Namuna ma'lumotlar
product = Product(id=1, name="Laptop", price=1200.00)
user = User(id=1, name="Nargiza", email="nargiza@example.com")

# Metodlarni chaqirish
print(f"Original price: ${product.price}")
print(f"Discounted price (10%): ${product.get_discount_price(10)}")
print(user.display_user_info())

