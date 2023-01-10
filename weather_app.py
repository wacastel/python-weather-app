# Weather App: Educational app that fetches the weather using OpenWeatherMap API
# Python programming exercise by William Castellano
# Please register at OpenWeatherMap to get your own API key
import requests

class WeatherApp:

    PATH = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = ""
    UNITS = "imperial"

    def __init__(self):
        self.name = ""

    def start_app(self):
        self.print_info()

    def print_info(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to WeatherApp! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def request_weather(self, query):
        res=requests.get(self.PATH+query+'&APPID='+self.API_KEY+'&units='+self.UNITS)
        return res.json()

    def print_menu(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(C): Look up weather by city name")
        print("(Z): Look up weather by zip code")
        print("(M): Repeat this menu")
        print("(Q): Quit program")

    def print_weather(self, data):
        city_name = data['name']
        print("\nCity name: "+city_name)
        print("{}'s temperature: {}°F ".format(city_name,data['main']['temp']))
        print("Wind speed: {} mph".format(data['wind']['speed']))
        print("Description: {}".format(data['weather'][0]['description']))
        print("Weather: {}".format(data['weather'][0]['main']))

    def menu(self):
        selection = ""
        input_data = ""
        self.print_menu()
        while (True):
            selection = input('Selection? ')
            if len(selection) == 0:
                continue
            selection = selection.capitalize()
            if selection[0] == 'Z':
                input_data = input("\nEnter zip code: ")
                if (input_data == ''):
                    input_data = '94502'
                query='zip='+input_data+',us'
            elif selection[0] == 'C':
                input_data = input("\nEnter City: ")
                if (input_data == ''):
                    res = requests.get("https://ipinfo.io/")
                    data = res.json()
                    print()
                    print(data)
                    print()
                    input_data = data['city']
                query='q='+input_data+',us'
            elif selection[0] == 'M':
                self.print_menu()
                continue
            elif selection[0] == 'Q':
                print('Goodbye')
                break
            try:
                response = self.request_weather(query)
                self.print_weather(response)
            except:
                print("Error! Weather data not found...")

    def run(self):
        self.start_app()
        self.menu()

if __name__=="__main__":
    app = WeatherApp()
    app.run()
