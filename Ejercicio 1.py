#Crear una Clase Producto con los siguientes atributos:
#- código
#- nombre
#- precio
#Crea su constructor, getter y setter y una función llamada calcular_total, donde le pasaremos unas unidades y nos debe
# calcular el precio final.

class Producto:

   def __init__ (self, codigo, nombre, precio):
       self.__codigo = codigo
       self.__nombre = nombre
       self.__precio = precio

   @property
   def codigo(self):
       return self.__codigo

   @codigo.setter
   def codigo(self, valor):
       self.__codigo = valor

   @property
   def nombre(self):
       return self.__nombre

   @nombre.setter
   def nombre(self, valor):
       self.__nombre = valor

   @property
   def precio(self):
       return self.__precio

   @precio.setter
   def precio(self, nuevo_valor):
       self.__precio = nuevo_valor

   def total_pedido(self, unidad):
       return self.__precio * unidad

   def __str__(self):
       return "Codigo:" + str(self.__codigo) + ",Producto:" + self.__nombre + ",Precio:" + str(self.__precio)


p1 = Producto(1, "Boli", 5)
p2 = Producto(2, "Goma", 7)
p3 = Producto(3, "Calculadora", 9)

print(p1)
print(p2)
print(p3)

print("P1:", p1.total_pedido(10))
print("P2:", p2.total_pedido(10))
print("P3:", p3.total_pedido(10))

print("Precio total:", p1.total_pedido(10) + p2.total_pedido(10) + p3.total_pedido(10), "€")

