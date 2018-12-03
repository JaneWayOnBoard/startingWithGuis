from guizero import App, Text, TextBox, PushButton, Slider, Picture

app = App(title="Hello my Dear")

"""Define functions at the top of your program"""

"""Function refering to the welcome_message Text widget"""
def say_my_name():
    welcome_message.value = my_name.value

"""Slider widget to change the text size"""
def change_text_size(slider_value):
    welcome_message.size = slider_value


"""Insert a Text widget with a keyword argument before the display loop"""
welcome_message = Text(app, text="Let's go somewhere !", size = 40, font="Times New Roman", color="lightblue")

"""Insert a TextBox widget to the GUI"""
my_name = TextBox(app)

"""Insert a PushButton widget to the GUI"""
update_text=PushButton(app, command=say_my_name,text="enter the code")

"""Insert Slider widget to the GUI"""
text_size = Slider(app, command=change_text_size, start=10, end=80)

"""Insert a Picture widget"""
movie_picture= Picture(app, image="/home/pi/Desktop/pythonWorks/startingWithGuis/guiTest/HermioneAndHarry.gif")


app.display()

