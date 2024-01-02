from tkinter import *
import requests
import json 

root = Tk()
root.geometry("4000x4000")
root.title("News Project")
root.configure(background = "light green")

heading = Label(root, text = "BBC News Update", font = ("Arial", 40, "bold"), fg = "blue")
heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

news1 = Label(root, font = ("Arial", 20, "bold"), fg = "red", wraplength = 500)
news1.place(relx = 0.5, rely = 0.2, anchor = CENTER)

news1_description = Label(root, font = ("Arial", 15, "normal"), wraplength = 500)
news1_description.place(relx = 0.5, rely = 0.25, anchor = CENTER)

news2 = Label(root, font = ("Arial", 20, "bold"), fg = "red", wraplength = 500)
news2.place(relx = 0.5, rely = 0.35, anchor = CENTER)

news2_description = Label(root, font = ("Arial", 15, "normal"), wraplength = 500)
news2_description.place(relx = 0.5, rely = 0.4, anchor = CENTER)

news3 = Label(root, font = ("Arial", 20, "bold"), fg = "red", wraplength = 500)
news3.place(relx = 0.5, rely = 0.55, anchor = CENTER)

news3_description = Label(root, font = ("Arial", 15, "normal"), wraplength = 500)
news3_description.place(relx = 0.5, rely = 0.6, anchor = CENTER)

news4 = Label(root, font = ("Arial", 20, "bold"), fg = "red", wraplength = 500)
news4.place(relx = 0.5, rely = 0.7, anchor = CENTER)

news4_description = Label(root, font = ("Arial", 15, "normal"), wraplength = 500)
news4_description.place(relx = 0.5, rely = 0.75, anchor = CENTER)

news5 = Label(root, font = ("Arial", 20, "bold"), fg = "red", wraplength = 500)
news5.place(relx = 0.5, rely = 0.85, anchor = CENTER)

news5_description = Label(root, font = ("Arial", 15, "normal"), wraplength = 500)
news5_description.place(relx = 0.5, rely = 0.9, anchor = CENTER)

api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=7613f5503e044f8ba51d98c5a73067ed")
open_bbc_page = json.loads(api_request.content)

news1["text"] = open_bbc_page["articles"][0]["title"]
news1_description["text"] = open_bbc_page["articles"][0]["description"]

news2["text"] = open_bbc_page["articles"][1]["title"]
news2_description["text"] = open_bbc_page["articles"][1]["description"]

news3["text"] = open_bbc_page["articles"][2]["title"]
news3_description["text"] = open_bbc_page["articles"][2]["description"]

news4["text"] = open_bbc_page["articles"][3]["title"]
news4_description["text"] = open_bbc_page["articles"][3]["title"]

news5["text"] = open_bbc_page["articles"][4]["title"]
news5_description["text"] = open_bbc_page["articles"][4]["title"]

root.mainloop()

