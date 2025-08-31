import cv2

print("1. Display Image")
print("2. Display Black & White Image")
print("3. Edit Image")
choice = int(input("Enter a number: "))

a = input("Enter image path: ")
image = cv2.imread(a)

if image is None:
    print("Error: Image not found or unable to load.")
else:
    match choice:
        case 1:  # Show original image
            cv2.imshow("Shown Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        case 2:  # Convert to grayscale and show
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Black & White Image", gray_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        case 3:  # Resize and save
            name_file = input("Enter output image file name (with extension, e.g., output.jpg): ")
            resized_image = cv2.resize(image, (100, 100))
            cv2.imwrite(f"{name_file}", resized_image)
            print("Image edited and saved successfully.")

        case _:  # Default case
            print("Invalid choice")


