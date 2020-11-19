class Punto:
    """
    Clase ejemplo para entender la declaración de clases en Python
    """
    def __init__(self, x, y, z):
        """
        Constructor de la clase. El primer parámetro
        representa la instancia en curso. "self" no es una
        palabra clave, podría usarse otro nombre, como "this"
        o el que se prefiera.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Sobrecarga del  método print
        :return: cadena formateada con las coordenadas del punto
        """
        return "Punto({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        """
        Operador suma (en el código será un "+")
        :param other: Punto que se desea sumar al actual
        :return: Suma de ambos puntos
        """
        return Punto(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)

    def __sub__(self, other):
        """
        Operador resta (en el código será un "-")
        :param other: Punto que se desea restar al actual
        :return: Resta de ambos puntos
        """
        return Punto(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)


# No es necesario ninguna palabra clave para invocar la construcción
# de un objeto, la propia declaración utiliza el método __init__
px = Punto(1, -3, 4)
print(px)

py = Punto(3, 3, 3)

pz = px + py
print(pz)

pz = px - py
print(pz)
