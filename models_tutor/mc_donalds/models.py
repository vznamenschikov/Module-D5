from datetime import datetime

# from models_tutor.mc_donalds.resources import POSITIONS, cashier
from .resources import POSITIONS, cashier
from django.db import models  # импорт
# from models_tutor.mc_donalds.resources import POSITIONS, cashier

# CREATE TABLE STAFF (
#     staff_id INT AUTO_INCREMENT NOT NULL,
#     full_name CHAR(255) NOT NULL,
#     position CHAR(255) NOT NULL,
#     labor_contract INT NOT NULL,
#
#     PRIMARY KEY (staff_id)
# );


# # resources.py
# director = 'DI'
# admin = 'AD'
# cook = 'CO'
# cashier = 'CA'
# cleaner = 'CL'
#
# POSITIONS = [
#     (director, 'Директор'),
#     (admin, 'Администратор'),
#     (cook, 'Повар'),
#     (cashier, 'Кассир'),
#     (cleaner, 'Уборщик')
# ]


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.IntegerField()


# CREATE TABLE ORDERS (
#     order_id INT AUTO_INCREMENT NOT NULL,
#     time_in DATETIME NOT NULL,
#     time_out DATETIME,
#     cost FLOAT NOT NULL,
#     pickup INT NOT NULL,    staff INT NOT NULL,
#
#     PRIMARY KEY (order_id),
#     FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
# );

# CREATE TABLE PRODUCT (
#     product_id INT AUTO_INCREMENT NOT NULL,
#     name CHAR(255) NOT NULL,
#     price FLOAT NOT NULL,
#
#     PRIMARY KEY (product_id)
# );


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Order(models.Model):  # наследуемся от класса Model
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now() - self.time_in).total_seconds() // 60


class ProductOrder(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # amount = models.IntegerField(default=1)
    _amount = models.IntegerField(default=1, db_column='amount')

    def product_sum(self):
        return self.product.price * self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()


class Author(models.Model):
    full_name = models.CharField(max_length=64)
    name = models.CharField(null=True, max_length=64)

    def some_method(self):
        self.name = self.full_name.split()[0]
        self.save()


# print(Author.some_method())