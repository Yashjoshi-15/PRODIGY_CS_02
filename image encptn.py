from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode

    # Convert image data to a numpy array
    data = np.array(img)

    # Apply XOR operation with the key
    encrypted_data = data ^ key

    # Convert the encrypted data back to an image
    encrypted_img = Image.fromarray(encrypted_data)

    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode

    # Convert image data to a numpy array
    data = np.array(img)

    # Apply XOR operation with the key (same as encryption)
    decrypted_data = data ^ key

    # Convert the decrypted data back to an image
    decrypted_img = Image.fromarray(decrypted_data)

    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

# Example usage
key = 123  # Simple key for XOR operation

# Encrypt an image
encrypt_image('input_image.jpg', 'encrypted_image.jpg', key)

# Decrypt the image
decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg', key)
