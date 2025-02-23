import cv2

def decode_message(img, msg_length):
    """Decodes the message from the image."""
    message = ""
    for i in range(msg_length):
        n = i // img.shape[1]  # Row index
        m = i % img.shape[1]   # Column index
        z = i % 3              # Color channel index (0: R, 1: G, 2: B)
        message += chr(img[n, m, z])
    return message

def main():
    img = cv2.imread("extract.bmp")  # Replace with the correct image path
    if img is None:
        print("Error: Image not found.")
        return

    password = input("Enter passcode for Decryption: ")
    # Assuming you have a way to verify the password, you can add that logic here.

    # Assuming you know the length of the message you want to decode.
    # For demonstration, let's say the message length is known (e.g., 10).
    # In a real scenario, you might want to store the length in the image or have a fixed length.
    msg_length = 10  # Replace with the actual length of the hidden message

    decoded_message = decode_message(img, msg_length)
    print("Decrypted message:", decoded_message)

if __name__ == "__main__":
    main()
    
