# QR-code-generator
# QR Code Generator App

A simple and user-friendly QR Code Generator built using Python and Tkinter. This application allows users to create custom QR codes by providing a URL and title, select a save location for the QR code image, and view the generated QR code directly within the app.

## Features

- **Intuitive User Interface**: A sleek, Netflix-themed design with clear input fields and buttons.
- **QR Code Generation**: Generate QR codes by providing a URL and a custom title.
- **Directory Selection**: Choose a specific directory to save your QR code images.
- **Preview Functionality**: View the generated QR code directly in the application before using it.
- **Error Notifications**: Informative error messages to guide users through the process.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**
- Required Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `Pillow`
  - `qrcode`

Install missing libraries with the following command:
```bash
pip install pillow qrcode

How to Run
Clone this repository or download the QR Code Generator Python file.
Open a terminal and navigate to the directory containing the file.
Run the script with:
bash
Copy
Edit
python qr_code_generator.py
The application window will appear.
Usage
Enter or paste the URL in the "Enter or paste the URL" field.
Provide a title for the QR code in the "Enter the title for your QR code" field.
Click the "Choose Save Location" button to select a directory where the QR code image will be saved.
Press "Generate" to create and save the QR code.
The generated QR code will be displayed on the left panel, and a success notification will appear.
ilable.

Error Handling
If no URL or title is provided, an error message will appear.
If a save location is not selected, the app will prompt the user to choose one.
All errors are displayed in the left panel for better user guidance.
Customization
The theme and design elements can be modified by adjusting the bg, fg, and font parameters in the code. Currently, the app uses a Netflix-inspired dark theme with red highlights.

Future Enhancements
Add the ability to customize QR code colors.
Implement functionality to scan QR codes directly.
Include URL validation before generating QR codes.
Save app theme preferences for the user.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
The Pillow library for image manipulation.
The qrcode library for creating QR codes
