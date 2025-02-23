import cv2
import os

def main():
    img = cv2.imread("virat.jpg")  # Replace with the correct image path
    if img is None:
        print("Error: Image not found.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Check if the message can fit in the image
    if len(msg) > img.size // 3:
        print("Error: Message is too long to fit in the image.")
        return

    # Encoding the message
    for i in range(len(msg)):
        n, m, z = divmod(i, img.shape[1]), i % img.shape[1], i % 3
        img[n, m, z] = ord(msg[i])

    cv2.imwrite("extract.bmp", img)
    os.startfile("extract.bmp")  # Use 'os.startfile' for Windows

if __name__ == "__main__":
    main()
