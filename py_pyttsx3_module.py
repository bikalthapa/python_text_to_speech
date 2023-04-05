import pyttsx3 # pip install pyttsx3

# Initializing speaker to make it speak someting
speaker = pyttsx3.init()

# This will take the property to speed of speaking
rate = speaker.getProperty("rate")

# This will take two voices man and Women
voices = speaker.getProperty("voices")

# This will take the volume of system
volume = speaker.getProperty("volume")

message = "Hello  World  ! How are you ? Myself bekal thapa. How can i help you"

# Deciding the speed of speaking
speaker.setProperty("rate", rate-20)

# Deciding wether girl or a boy will speak
speaker.setProperty('voice',voices[1].id)

# Deciding the volume of system.
speaker.setProperty("volume", volume-0.1)

# Telling python to speak our message variable 
speaker.say(message)

# This function will stop speaking
speaker.runAndWait()
