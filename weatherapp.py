import tkinter as tk
import requests

# Function to get weather data
def get_weather():
    api_key = 'your_api_key_here'  # Replace with your actual API key
    city = 'Karen, KE'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        
        weather_info = f"Temperature: {temperature}°C\n"
        weather_info += f"Pressure: {pressure} hPa\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Description: {weather_description}"
    else:
        weather_info = "City Not Found!"
    
    label.config(text=weather_info)

# Creating the GUI window
root = tk.Tk()
root.title("Karen Weather Update")

label = tk.Label(root, font=('Helvetica', 12))
label.pack(pady=20)

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack(pady=10)

root.mainloop()
