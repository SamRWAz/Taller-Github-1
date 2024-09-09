class Main:
    def imprimirFlota(self):
        """Imprime los detalles de todos los vehículos de la flota, incluyendo color y potencia."""
        if not self.flota_vehiculos:
            print("No hay vehículos registrados en la flota.")
        else:
            for vehiculo in self.flota_vehiculos:
                print(
                    f"Marca: {vehiculo.getMarca()}, Modelo: {vehiculo.getModelo()}, Año: {vehiculo.getAño()}, "
                    f"Kilometraje: {vehiculo.getKilometraje()}, Estado: {vehiculo.getEstadoActual()}, "
                    f"Combustible: {vehiculo.getTipoCombustible()}, Color: {vehiculo.getColor()}, "
                    f"Potencia: {vehiculo.getPotencia()} HP"
                )
