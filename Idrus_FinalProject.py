import smtplib #simple mail transfer protocol library
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

email_address = 'idruspython@gmail.com'
email_pass = input('What is your email password? ')

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice) # calling google API to convert our voice to text
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() # transport layer security
    # Make sure to give app access in your Google account
    server.login(email_address, email_pass)
    email = EmailMessage()
    email['From'] = email_address
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
        'indonesia ai': 'nihaopython21@gmail.com'
  }


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey bro. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    if 'no' in send_more:
        pass

get_email_info()