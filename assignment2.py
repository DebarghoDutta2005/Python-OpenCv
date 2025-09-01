import cv2
import os

file_path = input("Enter the file location: ")

if os.path.isfile(file_path):
    print(f"File found at: {file_path}")
    
    with open(file_path, 'r') as file:
        
        image = cv2.imread(file_path)
        if image is None:
            print("Error: Image not found or unable to load.")
        else:
            cv2.imshow("Original Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("1. line")
            print("2. circle")
            print("3. rectangle")
            print("4. text")
            choice = int(input("Enter a number: "))
            match choice:
                case 1:
                    start_x = int(input("Enter starting x coordinate: "))
                    start_y = int(input("Enter starting y coordinate: "))
                    end_x = int(input("Enter ending x coordinate: "))
                    end_y = int(input("Enter ending y coordinate: "))
                    color = (0, 255, 0)
                    thickness = int(input("Enter line thickness: "))
                    cv2.line(image, (start_x, start_y), (end_x, end_y), color, thickness)
                    cv2.imshow("Image with Line", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    ask = input("Do you want to save the image? (yes/no): ")
                    if ask.lower() == 'yes':
                        output_name = input("Enter output image file name (with extension, e.g., output.jpg): ")
                        cv2.imwrite(output_name, image)
                        print("Image saved successfully.")
                    else:
                        print("Image not saved.")
                case 2:
                    center_x = int(input("Enter center x coordinate: "))
                    center_y = int(input("Enter center y coordinate: "))
                    radius = int(input("Enter radius: "))
                    color = (255, 0, 0)
                    thickness = int(input("Enter circle thickness (use -1 for filled circle): "))
                    cv2.circle(image, (center_x, center_y), radius, color, thickness)
                    cv2.imshow("Image with Circle", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    ask = input("Do you want to save the image? (yes/no): ")
                    if ask.lower() == 'yes':
                        output_name = input("Enter output image file name (with extension, e.g., output.jpg): ")
                        cv2.imwrite(output_name, image)
                        print("Image saved successfully.")
                    else:
                        print("Image not saved.")
                case 3:
                    top_left_x = int(input("Enter top-left x coordinate: "))
                    top_left_y = int(input("Enter top-left y coordinate: "))
                    bottom_right_x = int(input("Enter bottom-right x coordinate: "))
                    bottom_right_y = int(input("Enter bottom-right y coordinate: "))
                    color = (0, 0, 255)
                    thickness = int(input("Enter rectangle thickness (use -1 for filled rectangle): "))
                    cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color, thickness)
                    cv2.imshow("Image with Rectangle", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    ask = input("Do you want to save the image? (yes/no): ")
                    if ask.lower() == 'yes':
                        output_name = input("Enter output image file name (with extension, e.g., output.jpg): ")
                        cv2.imwrite(output_name, image)
                        print("Image saved successfully.")
                    else:
                        print("Image not saved.")
                case 4:
                    text = input("Enter the text to add: ")
                    org_x = int(input("Enter x coordinate for text: "))
                    org_y = int(input("Enter y coordinate for text: "))
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = float(input("Enter font scale (e.g., 1.0): "))
                    color = (255, 255, 255)
                    thickness = int(input("Enter text thickness: "))
                    cv2.putText(image, text, (org_x, org_y), font, font_scale, color, thickness, cv2.LINE_AA)
                    cv2.imshow("Image with Text", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    ask = input("Do you want to save the image? (yes/no): ")
                    if ask.lower() == 'yes':
                        output_name = input("Enter output image file name (with extension, e.g., output.jpg): ")
                        cv2.imwrite(output_name, image)
                        print("Image saved successfully.")
                    else:
                        print("Image not saved.")
                case _:
                    print("Invalid choice")

else:
    print("File does not exist. Please check the path.")
