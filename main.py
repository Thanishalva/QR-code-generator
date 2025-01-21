import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode as qr
import os


root = tk.Tk()
root.title("Generate QR Code")
root.geometry("900x500")
root.configure(bg="#00008B")  
directory = None

# Global variables
qr_label = None
notification_label = None

# Function to display messages in the left frame
def update_notification(message, color="black"):
    global notification_label
    if notification_label is None:
        # Create the label if it doesn't exist
        notification_label = tk.Label(
            left_frame, text=message, font=("Arial", 12), fg=color, bg="#F5F5DC", wraplength=400
        )
        notification_label.pack(pady=10)
    else:
        # Update the text and color of the existing label
        notification_label.config(text=message, fg=color)

#getting path to store the QR code file
def select_directory():
    global directory
    directory = filedialog.askdirectory()
    if directory:
        update_notification(f"Directory selected: {directory}", color="blue")
    else:
        update_notification("No directory selected!", color="red")

# Function to create the QR code
def generate_qrcode(link, title):
    global qr_label
    if not link or not title:
        update_notification("Error: Please provide both a URL and a title!", color="red")
        return
    if not directory:
        update_notification("Error: Please select a save location!", color="red")
        return

    try:
        # Generate QR code
        qr_code_image = qr.make(link)

        # checking if the title has a .png extension
        if not title.endswith(".png"):
            title += ".png"
        file_path = os.path.join(directory, title)

        # Save the QR code image
        qr_code_image.save(file_path)

        # Convert the QR code image for Tkinter display
        qr_code_image = qr_code_image.resize((300, 300))  # Resize to fit in the left frame
        tk_image = ImageTk.PhotoImage(qr_code_image)

        # Update or create the label in the left frame to display the QR code
        if qr_label is not None:  
            qr_label.configure(image=tk_image)
            qr_label.image = tk_image  
        else:
            qr_label = tk.Label(left_frame, image=tk_image, bg="#F5F5DC")
            qr_label.image = tk_image  
            qr_label.pack(pady=20)

        
        update_notification("QR Code generated and saved successfully!", color="green")
    except Exception as e:
        update_notification(f"Error: {str(e)}", color="red")

root.resizable(False, False)

# Left frame 
left_frame = tk.Frame(root, bg="#F5F5DC", width=500, height=500)  
left_frame.pack(side="left", fill="y")  

# Right frame 
right_frame = tk.Frame(root, bg="#000000", width=400, height=500)  
right_frame.pack(side="right", fill="both", expand=True)

title_label = tk.Label(
    right_frame, text="GENERATE QR CODE", bg="#000000", fg="#FFFFFF",  
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)

url_label = tk.Label(
    right_frame, text="Enter or paste the URL", bg="#000000", fg="#FFFFFF",  
    font=("Arial", 12)
)
url_label.pack(anchor="w", padx=30)


url_entry = tk.Entry(right_frame, width=40, font=("Arial", 12))
url_entry.pack(pady=10, padx=30)


title_label = tk.Label(
    right_frame, text="Enter the title for your QR code", bg="#000000", fg="#FFFFFF",  
    font=("Arial", 12)
)
title_label.pack(anchor="w", padx=30)


title_entry = tk.Entry(right_frame, width=40, font=("Arial", 12))
title_entry.pack(pady=10, padx=30)


browse_button = tk.Button(
    right_frame, text="Choose Save Location", font=("Arial", 12), bg="#E50914", fg="#FFFFFF", 
    relief="flat", command=select_directory
)
browse_button.pack(pady=20)


generate_button = tk.Button(
    right_frame, text="Generate", font=("Arial", 12), bg="#E50914", fg="#FFFFFF", 
    relief="flat", width=15, command=lambda: generate_qrcode(url_entry.get(), title_entry.get())
)
generate_button.pack()


root.mainloop()

