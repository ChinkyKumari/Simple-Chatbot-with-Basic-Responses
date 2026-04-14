import tkinter as tk
from tkinter import scrolledtext
import datetime
import webbrowser
import random

# ---------------- Chatbot Logic ---------------- #

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello 👋", "Hi there 😊", "Hey! How can I help you?"])

    # Time
    elif "time" in user_input:
        return "Current time is: " + datetime.datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in user_input:
        return "Today's date is: " + datetime.datetime.now().strftime("%d-%m-%Y")

    # Calculator
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation ❌"

    # Open YouTube
    elif "youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube ▶️"

    # Open Google
    elif "google" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening Google 🌐"

    # Joke
    elif "joke" in user_input:
        return random.choice([
            "Why did the computer go to the doctor? Because it caught a virus 😂",
            "I told my laptop a joke… it didn’t laugh 😐"
        ])

    # Default intelligent fallback
    else:
        return "Hmm 🤔 I’m still learning. Try asking something else!"

# ---------------- GUI Design ---------------- #

def send_message():
    user_msg = entry_box.get()
    if user_msg.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    bot_reply = chatbot_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)
    entry_box.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("Smart AI Chatbot 🤖")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.config(bg="#2b2b2b", fg="white", state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry Box
entry_box = tk.Entry(root, font=("Arial", 14), bg="#3c3f41", fg="white")
entry_box.pack(padx=10, pady=10, fill=tk.X)

# Send Button
send_button = tk.Button(root, text="Send 🚀", command=send_message,
                        bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
send_button.pack(pady=5)

root.mainloop()