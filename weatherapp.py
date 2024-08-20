import tkinter as tk
import requests

# Function to get weather data
def get_weather():
    city = 'Karen'
    base_url = f'http://wttr.in/{city}?format=%C+%t+%h+%P'

    response = requests.get(base_url)
    if response.status_code == 200:
        weather_info = response.text
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
