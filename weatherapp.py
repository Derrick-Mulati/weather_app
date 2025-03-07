import tkinter as tk
import requests
import threading

# Function to get weather data
def get_weather():
    city = city_entry.get().strip() or "Karen"  # Default to "Karen" if no input
    base_url = f'http://wttr.in/{city}?format=%C+%t+%h+%P'

    label.config(text="Fetching weather...", fg="blue")
    root.update()

    def fetch():
        try:
            response = requests.get(base_url, timeout=5)
            if response.status_code == 200:
                weather_info = response.text.split()
                if len(weather_info) < 4:
                    label.config(text="Incomplete data received.", fg="red")
                    return
                
                condition, temperature, humidity, pressure = weather_info[:4]
                formatted_weather = (
                    f"Condition: {condition}\n"
                    f"Temperature: {temperature}\n"
                    f"Humidity: {humidity}\n"
                    f"Pressure: {pressure}"
                )
                label.config(text=formatted_weather, fg="green")
            else:
                label.config(text="City Not Found!", fg="red")
        except requests.exceptions.RequestException:
            label.config(text="Error fetching weather data.", fg="red")

    threading.Thread(target=fetch, daemon=True).start()

# Function to clear input and output
def clear():
    city_entry.delete(0, tk.END)
    label.config(text="", fg="black")

# Create GUI window
root = tk.Tk()
root.title("Weather Update")
root.geometry("400x300")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter City:").pack(side=tk.LEFT)
city_entry = tk.Entry(input_frame, width=20)
city_entry.pack(side=tk.LEFT, padx=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Get Weather", command=get_weather).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear).pack(side=tk.LEFT, padx=5)

# Weather Display
label = tk.Label(root, font=('Helvetica', 14), justify=tk.LEFT, wraplength=350)
label.pack(pady=20)

root.mainloop()
