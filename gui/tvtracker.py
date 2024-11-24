#!/usr/bin/env python
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("TV Show Completion Tracker")
    headers = ["No.", "Title", "Air Date", "Watched", "Rating"]
    for col, header in enumerate(headers):
        label = tk.Label(root, text=header, font=('Arial', 12, 'bold'))
        label.grid(row=0, column=col, padx=10, pady=5)
    
    episodes = [
        {
            "No.": "1",
            "Title": "Pimento",
            "Air Date": "5/9/2024",
            "Watched": False,
            "Rating": 0
        }
    ]

    for row, episode in enumerate(episodes, start=1):
        # Episode number
        no_label = tk.Label(root, text=episode["No."], font=('Arial', 10))
        no_label.grid(row=row, column=0, padx=10, pady=5)
        
        # Title
        title_label = tk.Label(root, text=episode["Title"], font=('Arial', 10))
        title_label.grid(row=row, column=1, padx=10, pady=5)
        
        # Air Date
        date_label = tk.Label(root, text=episode["Air Date"], font=('Arial', 10))
        date_label.grid(row=row, column=2, padx=10, pady=5)
        
        # Watched checkbox
        watched_var = tk.IntVar()
        watched_checkbox = tk.Checkbutton(root, variable=watched_var)
        watched_checkbox.grid(row=row, column=3, padx=10, pady=5)
        
        # Rating input
        rating_frame = tk.Frame(root)
        rating_entry = tk.Entry(rating_frame, width=2)
        rating_entry.grid(row=0, column=0)
        
        slash_label = tk.Label(rating_frame, text="/ 10", font=('Arial', 10))
        slash_label.grid(row=0, column=1)
        
        rating_frame.grid(row=row, column=4, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()