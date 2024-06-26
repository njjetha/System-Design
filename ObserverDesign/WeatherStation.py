from Observable import Observable
class WeatherStation(Observable):
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()