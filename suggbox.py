import tkinter as tk
import mysql.connector
from tkinter import messagebox

class SuggestionBox(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title("Suggestion Box")
        self.root.geometry("400x300")
        self.root.configure(bg="#D3D3D3")  # Set lighter gray background color

        self.label_name = tk.Label(self.root, text="Your Name:", bg="#D3D3D3", fg="black", font=("Helvetica", 12))
        self.label_name.pack(pady=(10, 5))

        self.name_entry = tk.Entry(self.root, width=40, bg="white", font=("Helvetica", 10), bd=2, relief=tk.FLAT, highlightbackground="#A9A9A9")
        self.name_entry.pack(pady=5)

        self.label_email = tk.Label(self.root, text="Your Email:", bg="#D3D3D3", fg="black", font=("Helvetica", 12))
        self.label_email.pack(pady=(10, 5))

        self.email_entry = tk.Entry(self.root, width=40, bg="white", font=("Helvetica", 10), bd=2, relief=tk.FLAT, highlightbackground="#A9A9A9")
        self.email_entry.pack(pady=5)

        self.label_suggestion = tk.Label(self.root, text="Suggestion:", bg="#D3D3D3", fg="black", font=("Helvetica", 12))
        self.label_suggestion.pack(pady=5)

        self.suggestion_entry = tk.Text(self.root, width=40, height=5, bg="white", font=("Helvetica", 10), bd=2, relief=tk.FLAT, highlightbackground="#A9A9A9")
        self.suggestion_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_suggestion, bg="#4CAF50", fg="white", font=("Helvetica", 10), padx=10, pady=5, bd=0)
        self.submit_button.pack(pady=5)

        # Connect to the database
        self.conn = mysql.connector.connect(
            host='localhost', username='root', password='230201074@ist', database='weather_db')
        self.cursor = self.conn.cursor()

    def submit_suggestion(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        suggestion = self.suggestion_entry.get("1.0", tk.END)
        if name and email and suggestion:
            try:
                # Execute SQL INSERT query
                query = "INSERT INTO SUGG_BOX (name_, email, Suggestion) VALUES (%s, %s, %s)"
                values = (name, email, suggestion)
                self.cursor.execute(query, values)
                self.conn.commit()
                messagebox.showinfo("Success", f"Thank you, {name}, for your suggestion. We will contact you at {email} if needed.")
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.suggestion_entry.delete("1.0", tk.END)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to submit suggestion: {e}")
        else:
            messagebox.showerror("Error", "Please enter your name, email, and suggestion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SuggestionBox(root)
    app.pack()
    root.mainloop()

