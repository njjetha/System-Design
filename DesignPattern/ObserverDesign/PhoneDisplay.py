from Observer import Observer
from WeatherStation import WeatherStation
# from PhoneDisplay import PhoneDisplay

class PhoneDisplay(Observer):
    def update(self,observable):
        self.observable=observable
        if isinstance(self.observable, WeatherStation):
            temp=self.observable.temperature
            print (f"Temperature is {temp} degree Celsius")

weather_station=WeatherStation()
phone_display=PhoneDisplay()

weather_station.add(phone_display)
weather_station.set_temperature(25)