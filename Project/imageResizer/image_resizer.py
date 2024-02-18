import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2

def resize_image():
    """Resizes an image based on user input and displays the result."""

    try:
        source_path = source_entry.get()
        if not source_path:
            raise ValueError("Please enter the source image path.")

        destination_path = destination_entry.get()
        if not destination_path:
            raise ValueError("Please enter the destination image path.")

        scale_percentage = float(scale_entry.get())
        if not scale_percentage:
            raise ValueError("Please enter a valid scale percentage.")

        image = cv2.imread(source_path, cv2.IMREAD_UNCHANGED)

        if image is None:
            raise FileNotFoundError(f"Image file not found at: {source_path}")

        width, height = image.shape[1], image.shape[0]
        new_width = int(width * scale_percentage / 100)
        new_height = int(height * scale_percentage / 100)

        new_image = cv2.resize(image, (new_width, new_height))

        cv2.imwrite(destination_path, new_image)
        print(f"Image resized successfully and saved to: {destination_path}")

        # Display resized image in a new window
        cv2.imshow("Resized Image", new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except ValueError as e:
        print(f"Error: {e}")
        messagebox.showerror("Invalid Input", e)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("File Not Found", e)
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", e)

def select_source_file():
    """Opens a file dialog to select the source image."""

    source_path = filedialog.askopenfilename(title="Select Image to Resize")
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_path)

def select_destination_file():
    """Opens a file dialog to select the destination for the resized image."""

    destination_path = filedialog.asksaveasfilename(title="Select Destination for Resized Image")
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_path)

# Create the Tkinter window
root = tk.Tk()
root.title("Image Resizer")

# Layout widgets for user input and button
source_label = tk.Label(root, text="Source Image:")
source_entry = tk.Entry(root, width=50)
source_button = tk.Button(root, text="Browse...", command=select_source_file)

destination_label = tk.Label(root, text="Destination:")
destination_entry = tk.Entry(root, width=50)
destination_button = tk.Button(root, text="Browse...", command=select_destination_file)

scale_label = tk.Label(root, text="Scale Percentage:")
scale_entry = tk.Entry(root, width=10)

resize_button = tk.Button(root, text="Resize", command=resize_image)

# Arrange widgets using grid layout manager
source_label.grid(row=0, column=0, sticky=tk.W)
source_entry.grid(row=0, column=1, padx=5)
source_button.grid(row=0, column=2)

destination_label.grid(row=1, column=0, sticky=tk.W)
destination_entry.grid(row=1, column=1, padx=5)
destination_button.grid(row=1, column=2)

scale_label.grid(row=2, column=0, sticky=tk.W)
scale_entry.grid(row=2, column=1, padx=5)

resize_button.grid(row=3, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
