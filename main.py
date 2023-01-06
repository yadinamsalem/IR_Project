# main crawler

import webScraper as wscraper
import mostplayed as mp
import tkinter as tk

def button1_clicked():
    wscraper.WebScarp()

def button2_clicked():
    mp.third_query()

def button3_clicked():
    import steamdata as sd
    import steamgui as sg

if __name__ == '__main__':

    # Create the main window
    window = tk.Tk()
    window.geometry("700x500")  # Set the size of the window
    window.title("Steam Crawler")
    # Load and resize the background image
    image = tk.PhotoImage(file="store_home_share.png")
    image = image.subsample(2, 2)  # Resize the image
    label = tk.Label(image=image)
    label.pack()

    # Create a frame to hold the buttons
    frame = tk.Frame(window, bg="#ffffff", bd=5, width=500, height=400)
    frame.place(relx=0.9, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center of the window

    # Add three buttons
    button1 = tk.Button(frame, text="Query 1", command=button1_clicked, font=("Arial", 16), fg="#000000",
                        bg="systemWindow")
    button1.pack(pady=5)
    button2 = tk.Button(frame, text="Query 2", command=button2_clicked, font=("Arial", 16), fg="#000000",
                        bg="systemWindow")
    button2.pack(pady=5)
    button3 = tk.Button(frame, text="Query 3", command=button3_clicked, font=("Arial", 16), fg="#000000",
                        bg="systemWindow")
    button3.pack(pady=5)

    # Run the main loop
    window.mainloop()

    # Query 1 - The most profitable games to buy according to high positive reviews
    # Query 2 - The current most played games
    # Query 3 - Positive / Negative Reviews according to given input games
