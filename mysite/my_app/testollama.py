import ollama
import json

cvmodelfile = '''
FROM qwen2:0.5b
SYSTEM You are a CV parser. Convert the given CV into a JSON representation with only the following fields: name, address, skills, phone, email.
USER My CV is as follows:

'''

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_cv = '''Nishesh Gautam
Email: mynishesh@gmail.com
Mobile: 9848315171
Github: https://github.com/Nishesh73?tab=repositories
Linkedin: https://www.linkedin.com/in/nishesh50/

Summary
Flutter app developer proficient at developing responsive mobile applications. Passionate about working
with dedicated teams to build robust and efficient applications as per the client’s desire.

Programming Skills
• Concepts: OOP, Provider State Management
• Languages: Dart (Proficient), Java, Python
• Frontend: Flutter (Proficient), React
• Backend: Firebase (Proficient)
• Software Tools: Git/Github, Android Studio, Visual Studio

Education
Kathmandu Engineering College, IOE Kalimati, Kathmandu
B.E (Electronics and Communication); Percentage: 61 2019 A.D.

Prime International H. S. School, HSEB board Khusibu Nayabajar, Kathmandu
Class 12; Percentage: 61.60 2011 A.D.

Kalika English Secondary Boarding School, NG Board: Bijuwar 7 Tari, Pyuthan
Class 10; Percentage: 65 2009 A.D.

Projects
• Instagram clone App: A Flutter app which is a clone of the Instagram App. It has basic functions such as
liking, commenting, deleting posts, etc. To make this app I used the Firebase database as the backend.
• Freelance App like Fiverr: A Flutter App in which employers can post their job vacancies. The app contains
features like job posting, commenting on the job post, deleting the job post only by the specific job poster, etc.
• Blog App: A Flutter App useful for posting different types of blogs. While making this app I used the Firebase database as the backend.
• Weather App: A Flutter App that shows the temperature and weather description of Kathmandu city.
Weather data is fetched from an API. I used the concept of JSON parsing.
• Tic-tac-toe Game App: An Android Game app made using Java.
• Tmdb Movie App: A Flutter app that fetches different types of popular movies using the Tmdb API.
    '''
    print(ollama.list())
    json_value = ollama.generate(model="qwen2:0.5b", prompt=(cvmodelfile + my_cv))["response"]
    print(json_value)

    json_object = json.loads(json_value)
    # print(json_object)

    print(json_object["email"])

# !pip install PyMuPDF
# import sys, fitz

# fileName = '/content/drive/MyDrive/Resume/test/Sagar Aryal CV.pdf'
# doc = fitz.open(fileName)
# text = " "
# for page in doc:
#   text = text + str(page.get_text())
# text

# See PyCharm help at https://www.jetbrains.com/help/pycharm/