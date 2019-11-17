import tkinter as tk
import smtplib

def search(data, location):
    for i in location:
        if i == data:
            return True

    return False

def main():
    root = tk.Tk()
    root.title("Sending Email")
    root.minsize(300, 450)

    frame = tk.Frame(bg="#999999")
    frame.place(relx = 0.1 , rely = 0.1 , relheight = 0.8, relwidth = 0.8)

    textEmail = tk.Label(frame, text = "Type your email", bg="#999999")
    textEmail.pack()
    email_address = tk.Entry(frame)
    email_address.pack()

    space = tk.Label(frame ,text="", bg="#999999")
    space.pack()

    textPassword = tk.Label(frame ,text="Type your password", bg="#999999")
    textPassword.pack()
    email_password = tk.Entry(frame, show="-")
    email_password.pack()

    space = tk.Label(frame ,text="", bg="#999999")
    space.pack()

    textReciever = tk.Label(frame, text = "Type reciever email", bg="#999999")
    textReciever.pack()
    reciever = tk.Entry(frame)
    reciever.pack()

    space = tk.Label(frame ,text="", bg="#999999")
    space.pack()

    subjectText = tk.Label(frame, text="Type subject of the message", bg="#999999")
    subjectText.pack()

    subject = tk.Entry(frame)
    subject.pack()

    space = tk.Label(frame ,text="" , bg="#999999")
    space.pack()

    messageText = tk.Label(frame, text = "Type content of message", bg="#999999")
    messageText.pack()

    message = tk.Entry(frame)
    message.pack()

    space = tk.Label(frame ,text="" , bg="#999999")
    space.pack()

    submit = tk.Button(frame, text = "Submit", bg="#FFA500", command = lambda:sendEmail(email_address.get(),email_password.get(), reciever.get(), subject.get(), message.get()))
    submit.pack()

    space = tk.Label(frame ,text="" , bg="#999999")
    space.pack()

    root.mainloop()


def sendEmail(email_address, email_password, reciever, subject, msg):

    if search("@",email_address) and search("@",reciever):

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            subject = subject
            body = msg

            msg = f"Subject: {subject}\n\n{body}"

            print("Sending Email...")
            smtp.sendmail(email_address, reciever , msg)
            print("Email Sent...")
            
            main()

    else:
        print("Wrong emails was given")
        time.sleep(1.5)
        main()

main()
