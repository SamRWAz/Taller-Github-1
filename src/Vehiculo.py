class Vehiculo:
    """
    Representa un vehículo con sus atributos básicos.

    Attributes:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        año (int): Año de fabricación.
        kilometraje (int): Kilometraje actual.
        estado_actual (str): Estado actual del vehículo (ej: "bueno", "malo").
        tipo_combustible (str): Tipo de combustible utilizado.
    """

    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.estado_actual = estado_actual
        self.tipo_combustible = tipo_combustible

    # Métodos getter y setter
    def get_marca(self):
        return self.marca

    def set_marca(self, nueva_marca):
        self.marca = nueva_marca

    # ... (similarmente para los demás atributos)

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año})"