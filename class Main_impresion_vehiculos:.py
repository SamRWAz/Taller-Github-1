class Main:
    def __init__(self):
        self.flota_vehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.flota_vehiculos.append(vehiculo)

    def buscarVehiculoPorAño(self, año):
        return [vehiculo for vehiculo in self.flota_vehiculos if vehiculo.getAño() == año]

    def imprimirFlota(self):
        if not self.flota_vehiculos:
            print("No hay vehículos registrados en la flota.")
        else:
            for vehiculo in self.flota_vehiculos:
                print(
                    f"Marca: {vehiculo.getMarca()}, Modelo: {vehiculo.getModelo()}, Año: {vehiculo.getAño()}, "
                    f"Kilometraje: {vehiculo.getKilometraje()}, Estado: {vehiculo.getEstadoActual()}, "
                    f"Combustible: {vehiculo.getTipoCombustible()}"
                )
