# Weather App project

import requests
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
# BACKEND
CITY = "st. john's"
API_KEY = "976d9bc8d6b81c4e3cf656cd1130ed02"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city="st. john's"):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    weather_dictionary = requests.get(url)
    if weather_dictionary.status_code == 200:
        return weather_dictionary.json()


# Frontend

root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")
root.resizable(width=False, height=False)
# Optional The image should be put in a folder named 'icon' within the main weather app folder
ico = PhotoImage(file="icon/02d@4x.png")
root.iconphoto(True, ico)

frame = tk.Frame(root, bg="light blue", padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# City entry and label
ttk.Label(frame, background="light blue", font=20, text="Enter City:").grid(row=1, column=1)
city_variable = tk.StringVar()
city_box = ttk.Entry(frame, width=30, font=15, background="light blue", textvariable=city_variable).grid(row=1, column=2, columnspan=2)

# Weather Condition such as ("snowy", "sunny")
weather_descript_lab_var = tk.StringVar(value="Current Weather Condition: ")
weather_descript_lab = tk.Label(frame, font=13, background="light blue", textvariable=weather_descript_lab_var, height=2).grid(row= 4, column=2, columnspan=2)

# Current Temp label:
current_temp_var = tk.StringVar(value="Current Temp: ")
current_templ_lab = tk.Label(frame, font=13, background="light blue", textvariable=current_temp_var, height=2).grid(row=5, columnspan=2, column=2)

# Feels like temp label
feels_like_var = tk.StringVar(value="Feels Like: ")
feels_like_lab = tk.Label(frame, font=13, background="light blue", textvariable=feels_like_var, height=2).grid(row=6, columnspan=2, column=2)

# Wind Speed
wind_speed_var = tk.StringVar(value="Wind Speed: ")
wind_speed_lab = tk.Label(frame, font=13, background="light blue", textvariable=wind_speed_var, height=2).grid(row=7, columnspan=2, column=2)

#Wind Gust
wind_gust_var = tk.StringVar(value="Wind Gust: ")
wind_gust_lab =tk.Label(frame, font=13, background="light blue", textvariable=wind_gust_var, height=2).grid(row=8, columnspan=2, column=2)

#Wind Deg
wind_direction_var = tk.StringVar(value= "Wind Direction: ")
wind_direct_lab = tk.Label(frame, font=13, background="light blue", textvariable=wind_direction_var, height=2).grid(row=9, columnspan=2, column=2)

# The main button which refreshes text boxes when clicked
def get_weather_btn():
    weather_dictionary = get_weather(city_variable.get())
    print(weather_dictionary)
    if type(weather_dictionary) == dict:
        weather_descript_lab_var.set(f"Current Weather Condition: {weather_dictionary['weather'][0]['main']}({weather_dictionary['weather'][0]['description']})")
        current_temp_var.set(f"Current Temp: {weather_dictionary['main']['temp']}°C")
        feels_like_var.set(f"Feels Like: {weather_dictionary['main']['feels_like']}°C")
        wind_speed_var.set(f"Wind Speed: {weather_dictionary['wind']['speed']}m/s")
        if 'gust' in weather_dictionary['wind'].keys():
            wind_gust_var.set(f"Wind Gust: {weather_dictionary['wind']['gust']}m/s")
        else:
            wind_gust_var.set(f"Wind Gust: No Info")
        wind_deg = weather_dictionary['wind']['deg']
        if 338 < wind_deg and wind_deg < 22:
            wind_direction_var.set(f"Wind Direction: North-{wind_deg}°")
        elif 23 < wind_deg and wind_deg < 67:
            wind_direction_var.set(f"Wind Direction: North East-{wind_deg}°")
        elif 68 < wind_deg and wind_deg < 112:
            wind_direction_var.set(f"Wind Direction: East-{wind_deg}°")
        elif 113 < wind_deg and wind_deg < 157:
            wind_direction_var.set(f"Wind Direction: South East-{wind_deg}°")
        elif 158 < wind_deg and wind_deg < 201:
            wind_direction_var.set(f"Wind Direction: South-{wind_deg}°")
        elif 202 < wind_deg and wind_deg < 246:
            wind_direction_var.set(f"Wind Direction: South West-{wind_deg}°")
        elif 247 < wind_deg and wind_deg < 292:
            wind_direction_var.set(f"Wind Direction: West-{wind_deg}°")
        elif 293 < wind_deg and wind_deg < 337:
            wind_direction_var.set(f"Wind Direction: North West-{wind_deg}°")
        # This displays the weather condition icon
        r = requests.get(f"http://openweathermap.org/img/wn/"+ weather_dictionary['weather'][0]['icon'] + "@2x.png").content
        img = PhotoImage(data=r)
        imgcanvas1 = tk.Label(frame, image=img, background="light blue", borderwidth=2, relief= "raised").grid(column= 4, row =6, rowspan=3)
        root.mainloop()
        print(img)
    else:
        city_variable.set("Name Error")

get_weather_btn = tk.Button(frame, width= 20, font=(20), text="Get City",command=get_weather_btn).grid(column=2, row=2, columnspan=2, pady= 10)

root.mainloop()




