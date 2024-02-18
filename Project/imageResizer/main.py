import cv2

def resize_image(source_path, destination_path, scale_percentage):
    try:
        image = cv2.imread(source_path, cv2.IMREAD_UNCHANGED)

        if image is None:
            print(f"Error: Image file not found at: {source_path}")
            return False

        width, height = image.shape[1], image.shape[0]

        if not scale_percentage:
            print("Error: Please specify a valid scale percentage.")
            return False

        new_width = int(width * scale_percentage / 100)
        new_height = int(height * scale_percentage / 100)

        new_image = cv2.resize(image, (new_width, new_height))

        cv2.imwrite(destination_path, new_image)
        print(f"Image resized successfully and saved to: {destination_path}")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Get user input for source, destination, and scale percentage
source_path = input("Enter the full path of the image: ")
destination_path = input("Enter the full desired path of the image to save: ")
scale_percentage = float(input("Enter the desired scaling percentage (e.g., 50 for 50%): "))

# Call the resize_image function with user-provided input
success = resize_image(source_path, destination_path, scale_percentage)

if success:
    print("Image resizing completed.")
else:
    print("Image resizing failed. Please check the provided information and try again.")

