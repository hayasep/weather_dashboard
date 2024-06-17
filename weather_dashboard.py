import requests
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.font import Font

# Function to fetch weather data
def get_weather(city):
    api_key = '9dab2587dc4bf5f64f9faad78cdf79b9'  # Your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display weather data
def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        location_label.config(text=f"{weather['name']}, {weather['sys']['country']}")
        temp_label.config(text=f"Temperature: {weather['main']['temp']}°C")
        desc_label.config(text=f"Description: {weather['weather'][0]['description']}")
        humidity_label.config(text=f"Humidity: {weather['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {weather['wind']['speed']} m/s")
    else:
        showerror("Error", "City not found")

# Set up the GUI
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x300")
root.resizable(False, False)

# Configure styles
style = ttk.Style(root)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Set up custom font for title
title_font = Font(family="Helvetica", size=16, weight="bold")

# Main frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title
title_label = ttk.Label(frame, text="Weather Dashboard", font=title_font)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# City input
ttk.Label(frame, text="Enter city name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Get weather button
get_weather_button = ttk.Button(frame, text="Get Weather", command=show_weather)
get_weather_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

# Weather information
location_label = ttk.Label(frame, text="", font=("Helvetica", 14))
location_label.grid(row=2, column=0, columnspan=3, pady=10)

temp_label = ttk.Label(frame, text="", font=("Helvetica", 12))
temp_label.grid(row=3, column=0, columnspan=3, pady=5)

desc_label = ttk.Label(frame, text="", font=("Helvetica", 12))
desc_label.grid(row=4, column=0, columnspan=3, pady=5)

humidity_label = ttk.Label(frame, text="", font=("Helvetica", 12))
humidity_label.grid(row=5, column=0, columnspan=3, pady=5)

wind_label = ttk.Label(frame, text="", font=("Helvetica", 12))
wind_label.grid(row=6, column=0, columnspan=3, pady=5)

root.mainloop()
