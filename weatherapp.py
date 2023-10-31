import tkinter as tk
import requests
from tkinter import font

# TO ADD:
#     - background image
#     - change font/boxes/colors
#     - "DRESS WARM" + "DRESS COLD" + more

HEIGHT = 400
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#'2ebf481f2079b568f1e7b5f689f7ea4c'5

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		max = weather['main']['temp_max']
		min = weather['main']['temp_min']

		message = ''
		if(temp<40):
			message = "It's cold! Dress warm!"
		else:
			message = "Have a good day!"

		final_str = 'City: %s \nConditions: %s \nCurrent Temp (°F): %s° \nHigh Temp: %s° \nLow Temp: %s° \n\n%s' % (name, desc.title(), temp, max, min, message)
	except:
		final_str = 'Please enter an input'

	return final_str

def get_weather(city):
	weather_key = '2ebf481f2079b568f1e7b5f689f7ea4c'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='jungle.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#3d9970', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=80, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#3d9970', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ('Bahnschrift Condensed', 15))
label.place(relwidth=1, relheight=1)

root.mainloop()