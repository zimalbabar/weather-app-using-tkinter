from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import * 
import requests 
import pytz
from PIL import Image, ImageTk
import mysql.connector
from suggbox import SuggestionBox
from viewer import DatabaseViewer



class WeatherApp(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, bg="#2E4053")
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("890x490+300+300")
        self.root.configure(bg="slategrey")
        self.root.resizable(False,False)
        self.create_widgets()
        self.create_menu()
    def create_menu(self):
        menubar = Menu(self.root,   font=('Helvetica', 10, 'bold'))
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0,   font=('Helvetica', 10, 'bold'))
        menubar.add_cascade(label="FILE", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

        help_menu = Menu(menubar, tearoff=0,   font=('Helvetica', 10, 'bold'))
        menubar.add_cascade(label="HELP", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
        sugg_menu = Menu(menubar, tearoff=0,   font=('Helvetica', 10, 'bold'))
        menubar.add_cascade(label="OTHER", menu=sugg_menu)
        sugg_menu.add_command(label="Open sugg box", command=self.opensugg)
        sugg_menu.add_command(label="Open Tables", command=self.openviewer)
        sugg_menu.add_command(label="Open Mining Tables", command=self.open_mining)
        update_menu = Menu(menubar, tearoff=0,   font=('Helvetica', 10, 'bold'))
        menubar.add_cascade(label="QUERY", menu=update_menu)
        update_menu.add_command(label="update data", command=self.refresh)
        update_menu.add_command(label="delete data", command=self.delete_and_clear)
        update_menu.add_command(label="clear app", command=self.clear_input)
        
        
        
    def open_mining(self):
        root.destroy()
        import mining   

    def show_about(self):
        messagebox.showinfo("About", "Weather App\nVersion 1.0")
        
    def opensugg(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = SuggestionBox(self.new_win)
    def openviewer(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = DatabaseViewer(self.new_win)
        
        
    def create_widgets(self):
        
        self.image_icon = PhotoImage(file="Images/logo.png")
        self.root.iconphoto(False,self.image_icon)

        
        round_box = Image.open("Images/Rounded Rectangle 1.png")

        # Resize the image
        resized_image = round_box.resize((220, 130), Image.BILINEAR)

        # Convert the resized image to a PhotoImage
        self.rb_image = ImageTk.PhotoImage(resized_image)
        Label(self.root, image=self.rb_image, bg="#57adff").place(x=30, y=110)




##label
        self.label1 = Label(self.root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
        self.label1.place(x=50,y=120)

        self.label2 = Label(self.root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
        self.label2.place(x=50,y=140)

        self.label3 = Label(self.root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
        self.label3.place(x=50,y=160)

        self.label4 = Label(self.root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
        self.label4.place(x=50,y=180)

        self.label5 = Label(self.root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
        self.label5.place(x=50,y=200)


##Search box
        self.Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
        self.myimage=Label(image=self.Search_image,bg="slategrey")
        self.myimage.place(x=270,y=120)

        self.weat_image=PhotoImage(file="Images/Layer 7.png")
        self.weatherimage=Label(self.root,image=self.weat_image,bg="#203243")
        self.weatherimage.place(x=290,y=127)

        self.textfield=tk.Entry(self.root,justify='center',width=15,font=('poppins',20,'bold'),bg = "#203243",border=0, fg="white")
        self.textfield.place(x=370,y=130)
        self.textfield.focus()

        self.Search_icon = PhotoImage(file="Images/Layer 6.png")
        self.myimage_icon=Button(image=self.Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=self.getWeather)
        self.myimage_icon.place(x=645,y=125)


#Bottom box
        self.frame=Frame(self.root,width=900,height=180,bg="#203243")
        self.frame.pack(side=BOTTOM)

##bottom boxes
        firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
        secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

        Label(self.frame,image=firstbox,bg="#212120").place(x=20,y=20)
        Label(self.frame,image=secondbox,bg="#212120").place(x=300,y=30)
        Label(self.frame,image=secondbox,bg="#212120").place(x=400,y=30)
        Label(self.frame,image=secondbox,bg="#212120").place(x=500,y=30)
        Label(self.frame,image=secondbox,bg="#212120").place(x=600,y=30)
        Label(self.frame,image=secondbox,bg="#212120").place(x=700,y=30)
        Label(self.frame,image=secondbox,bg="#212120").place(x=800,y=30)


#clock
        self.clock=Label(self.root,text="CLOCK",font=("Helvetica",30,'bold'),fg="white",bg="slategrey")
        self.clock.place(x=30,y=20)

#timezone
        self.timezone=Label(self.root,text="TIME ZONE",font=("Helvetica",20),fg="white",bg="slategrey")
        self.timezone.place(x=600,y=20)


        self.long_lat=Label(self.root,text="Longitude / Latitude",font=("Helvetica",10),fg="white",bg="slategrey")
        self.long_lat.place(x=600,y=50)

#thpwd
        self.t=Label(self.root,font=("Helvetica",11),fg="white",bg="#203243")
        self.t.place(x=150,y=120)
        self.h=Label(self.root,font=("Helvetica",11),fg="white",bg="#203243")
        self.h.place(x=150,y=140)
        self.p=Label(self.root,font=("Helvetica",11),fg="white",bg="#203243")
        self.p.place(x=150,y=160)
        self.w=Label(self.root,font=("Helvetica",11),fg="white",bg="#203243")
        self.w.place(x=150,y=180)
        self.d=Label(self.root,font=("Helvetica",11),fg="white",bg="#203243")
        self.d.place(x=150,y=200)


#first cell
        self.firstframe=Frame(self.root, width=230,height=132,bg="#282829")
        self.firstframe.place(x=25,y=315)

        self.day1=Label(self.firstframe,font="arial 20",bg="#282829",fg="#fff")
        self.day1.place(x=100,y=5)

        self.firstimage=Label(self.firstframe,bg="#282829")
        self.firstimage.place(x=1,y=17)

        self.day1temp=Label(self.firstframe,bg="#282829",fg="#DAA520",font="arial 13 bold")
        self.day1temp.place(x=100,y=50)



#second cell
        self.secondframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.secondframe.place(x=305,y=325)

        self.day2=Label(self.secondframe, bg="#282829", fg="#fff")
        self.day2.place(x=10,y=5)

        self.secondimage=Label(self.secondframe,bg="#282829")
        self.secondimage.place(x=7,y=23)

        self.day2temp=Label(self.secondframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day2temp.place(x=2,y=70)

#third cell
        self.thirdframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.thirdframe.place(x=405,y=325)

        self.day3=Label(self.thirdframe, bg="#282829", fg="#fff")
        self.day3.place(x=10,y=5)

        self.thirdimage=Label(self.thirdframe,bg="#282829")
        self.thirdimage.place(x=7,y=23)

        self.day3temp=Label(self.thirdframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day3temp.place(x=2,y=70)

#fourth cell
        self.fourthframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.fourthframe.place(x=505,y=325)

        self.day4=Label(self.fourthframe, bg="#282829", fg="#fff")
        self.day4.place(x=10,y=5)

        self.fourthimage=Label(self.fourthframe,bg="#282829")
        self.fourthimage.place(x=7,y=23)

        self.day4temp=Label(self.fourthframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day4temp.place(x=2,y=70)


#fifth cell
        self.fifthframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.fifthframe.place(x=605,y=325)

        self.day5=Label(self.fifthframe, bg="#282829", fg="#fff")
        self.day5.place(x=10,y=5)

        self.fifthimage=Label(self.fifthframe,bg="#282829")
        self.fifthimage.place(x=7,y=23)

        self.day5temp=Label(self.fifthframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day5temp.place(x=2,y=70)

#sixth cell
        self.sixthframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.sixthframe.place(x=705,y=325)

        self.day6=Label(self.sixthframe, bg="#282829", fg="#fff")
        self.day6.place(x=10,y=5)

        self.sixthimage=Label(self.sixthframe,bg="#282829")
        self.sixthimage.place(x=7,y=23)

        self.day6temp=Label(self.sixthframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day6temp.place(x=2,y=70)

#seventh cell
        self.seventhframe=Frame(self.root, width=70,height=115,bg="#282829")
        self.seventhframe.place(x=805,y=325)

        self.day7=Label(self.seventhframe, bg="#282829", fg="#fff")
        self.day7.place(x=10,y=5)

        self.seventhimage=Label(self.seventhframe,bg="#282829")
        self.seventhimage.place(x=7,y=23)

        self.day7temp=Label(self.seventhframe,bg="#282829",fg="#fff",font="arial 7 bold")
        self.day7temp.place(x=2,y=70)
        
        
        self.day_labels = [self.day1temp, self.day2temp, self.day3temp, self.day4temp, self.day5temp, self.day6temp, self.day7temp]

        self.image_labels = [self.firstimage, self.secondimage, self.thirdimage, self.fourthimage, self.fifthimage, self.sixthimage, self.seventhimage]

        self.day_n = [self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7]

        current_date = datetime.now()
        self.day_names = [(current_date + timedelta(days=i)).strftime('%A') for i in range(7)]
# Function to get the weather data
    def init_db(self):
        conn = mysql.connector.connect(
            host='', username='root', password='',
            database='weather_db'
        )
        return conn
    

    
    def fetch_weather_data(self,city):
        # try:
        geolocator = Nominatim(user_agent="Weather App")
        location = geolocator.geocode(city)
        
        api_key = '34579d925f013e6b7cd03e2cbbd78bbb'  # Replace with your OpenWeather API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(api_url)
        json_data = response.json()

        return json_data
        
        
    def fetch_weather_forecast(self, city):
        try:
            api_key = '34579d925f013e6b7cd03e2cbbd78bbb'  # Replace with your OpenWeather API key
            api_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

            response = requests.get(api_url)
            json_data = response.json()

            forecast_data = []

        # Extract forecast data for the next few days
            for forecast in json_data.get('list', []):
               forecast_date = forecast.get('dt_txt', '').split()[0]  # Get forecast date
               forecast_day = datetime.strptime(forecast_date, '%Y-%m-%d').date()

            # Check if the forecast is for the current day or the next day (skip today's forecast)
               if forecast_day > datetime.now().date():
                # Extract relevant forecast information
                    temp_day = forecast.get('main', {}).get('temp_max')
                    temp_night = forecast.get('main', {}).get('temp_min')
                    icon = forecast.get('weather', [{}])[0].get('icon')  # Extract 'icon' field

                # Append forecast data to the list
                    forecast_data.append({
                    'date': forecast_day,
                    'temp_day': temp_day,
                    'temp_night': temp_night,
                    'icon': icon
                    })

                # Limit the forecast to 7 days
                    if len(forecast_data) >= 7:
                       break

            return forecast_data

        except Exception as e:
            print(f"Error fetching weather forecast data: {e}")
            return None

        messagebox.showerror('Error', f'Failed to update weather data for {city} in the database: {err}')
    def update_weather_db(self, city):
        json_data = self.fetch_weather_data(city)
        try:
            if json_data is not None:
            # Extract relevant information from the JSON data
                main_data = {
                'temp': json_data['main']['temp'],
                'humidity': json_data['main']['humidity'],
                'pressure': json_data['main']['pressure'],
                'wind_speed': json_data['wind']['speed'],
                'description': json_data['weather'][0]['description']
                }

                connector = mysql.connector.connect(
                host='localhost', username='root', password='230201074@ist',
                database='weather_db'
                )
                cursor = connector.cursor()

            # Update current weather data in weather_db table
                query = '''UPDATE weather_db SET temp = %s, humidity = %s, pressure = %s, wind_speed = %s, description = %s
                       WHERE city = %s'''
                val_main = (main_data['temp'], main_data['humidity'],
                        main_data['pressure'], main_data['wind_speed'],
                        main_data['description'], city)
                cursor.execute(query, val_main)
        

                connector.commit()
                connector.close()
                messagebox.showinfo('Success', f'Weather data for {city} has been updated in the database.')
            else:
                messagebox.showerror('Error', f'Failed to fetch weather data for {city}.')
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'Failed to update weather data for {city} in the database: {err}')
    
    def delete_weather_db(self,city):
        try:
            connector =  mysql.connector.connect(
            host='localhost', username='root', password='230201074@ist',
            database='weather_db'
            )
            cursor = connector.cursor()
        
            query = "DELETE FROM weather_db WHERE city = %s"
            cursor.execute(query, (city,))
            query1 = "DELETE FROM weather_days WHERE city = %s"
            cursor.execute(query1, (city,))
            connector.commit()
            cursor.close()
            connector.close()
            messagebox.showinfo('Success', f'Weather data for {city} has been deleted in the database.')
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'Failed to Delete weather data for {city} in the database: {err}')

    def refresh(self):
        city = self.textfield.get()
        self.update_weather_db(city)
        self.getWeather()
    
    
    # Clearing labels containing weather data
    def clear_input(self):
        self.textfield.delete(0, END) 
        self.t.config(text="")
        self.h.config(text="")
        self.p.config(text="")
        self.w.config(text="")
        self.d.config(text="")

    # Clearing labels containing forecast data
        for label in self.day_labels:
           label.config(text="")

    # Clearing labels containing day names
        for label, day_name in zip(self.day_n, self.day_names):
           label.config(text=day_name)

    # Clearing image labels
        for image_label in self.image_labels:
            image_label.config(image="")

    def delete_and_clear(self):
        city = self.textfield.get()
        self.delete_weather_db(city)
        self.clear_input()

    

       

    def getWeather(self):
        # Get the city name from the input field
        city = self.textfield.get()

        geolocator = Nominatim(user_agent="Weather APP")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        # Use timezonefinder to get the timezone of the location
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # Update the timezone label with
        self.timezone.configure(text=result)
        self.long_lat.config(text=f"{round(location.latitude,4)}°N{round(location.longitude,4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        self.clock.config(text=current_time)

        try:
            conn = self.init_db()
            cursor = conn.cursor()

            # Fetch current weather data from the database
            query = "SELECT temp, humidity, pressure, wind_speed, description FROM weather_db WHERE city = %s"
            cursor.execute(query, (city,))
            weather_data = cursor.fetchone()

            # Fetch weather data for the upcoming days from the database
            query_days = "SELECT temp_day, temp_night, icon FROM weather_days WHERE city = %s"
            cursor.execute(query_days, (city,))
            weather_days_data = cursor.fetchall()

            conn.close()
        except mysql.connector.Error as error:
            messagebox.showerror('Error', f'Failed to fetch weather data for {city} from the database: {error}')
            return None

        # Update the labels with the current weather data
        if weather_data:
            temp, humidity, pressure, wind, description = weather_data

            self.t.config(text=(f"{temp} °C"))
            self.h.config(text=(f"{humidity} %"))
            self.p.config(text=(f"{pressure} hPa"))
            self.w.config(text=(f"{wind} m/s"))
            self.d.config(text=description)
        else:
            messagebox.showinfo('Info', f'Weather data for {city} not found in the database.')

        # Update weather icons and temperatures for the upcoming days
        for i in range(min(len(weather_days_data), 7)):
            temp_day, temp_night, icon = weather_days_data[i]

            # Update temperature labels
            self.day_labels[i].config(text=f"Day: {temp_day}°C\nNight: {temp_night}°C")

            # Update weather icons
            if icon:
                try:
                    img = Image.open(f"icon/{icon}@2x.png")
                    resized_image = img.resize((50, 50))
                    photo = ImageTk.PhotoImage(resized_image)
                    self.image_labels[i].config(image=photo)
                    self.image_labels[i].image = photo
                except FileNotFoundError:
                    messagebox.showerror('Error', f'Icon image for {city} not found.')
            else:
                messagebox.showinfo('Info', f'Icon data for {city} not found in the database.')

        for i in range(min(len(self.day_names), 7)):
            self.day_n[i].config(text=self.day_names[i])


if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()