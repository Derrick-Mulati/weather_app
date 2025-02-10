import tkinter as tk
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get().strip() or "Karen"  # Default to "Karen" if no input
    base_url = f'http://wttr.in/{city}?format=%C+%t+%h+%P'

    # Show loading message
    label.config(text="Please wait...", fg="blue")
    root.update()  # Force update the GUI

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            weather_info = response.text.split()
            condition = weather_info[0]
            temperature = weather_info[1]
            humidity = weather_info[2]
            pressure = weather_info[3]

            # Format the weather information
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

# Function to clear the input and weather display
def clear():
    city_entry.delete(0, tk.END)
    label.config(text="", fg="black")

# Creating the GUI window
root = tk.Tk()
root.title("Weather Update")
root.geometry("400x300")  # Set a fixed window size

# City input field
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter City:").pack(side=tk.LEFT)
city_entry = tk.Entry(input_frame, width=20)
city_entry.pack(side=tk.LEFT, padx=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

get_weather_button = tk.Button(button_frame, text="Get Weather", command=get_weather)
get_weather_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear)
clear_button.pack(side=tk.LEFT, padx=5)

# Weather display label
label = tk.Label(root, font=('Helvetica', 12), justify=tk.LEFT)
label.pack(pady=20)

root.mainloop()