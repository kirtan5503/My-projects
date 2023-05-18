from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = 'weather.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key'] ['key']

def weather_find(city):
    final = requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature -273.15
        f_temperature = (k_temperature -273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city,country_name,c_temperature,f_temperature,weather_display)
        
        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather: 
        location_entry['text'] =  '{}, {}'.format(weather[0],weather[1])
        temperature_entry['text'] =  '{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror('error','Please enter a valid city name')
        

root = Tk()
root.title("Weather app")
root.config(background="grey")
root.geometry("1000x500")

search_city = StringVar()
enter_city = Entry(root, textvariable=search_city, bg="black", fg="blue", font=("Times new roman ",35,"bold"))
enter_city.pack()

search_button = Button(root, text='Search Weather',width=25, bg="green", fg="white", font=("Times new roman",30,"bold"),command=print_weather)
search_button.pack()

location_entry = Label(root, text='',font=("Times new roman",35,"bold"),bg="lightgreen")
location_entry.pack()

temperature_entry = Label(root, text='',font=("Times new roman",35,"bold"),bg="lightgreen")
temperature_entry.pack()

weather_entry = Label(root, text='',font=("Times new roman",35,"bold"),bg="lightgreen")
weather_entry.pack()



root.mainloop()