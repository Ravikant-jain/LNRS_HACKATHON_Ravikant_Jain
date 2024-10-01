import streamlit as st
from PIL import Image
import numpy as np
import random
import os
import io

# Function to encrypt an image
def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    original_shape = image_array.shape

    flat_array = image_array.flatten()

    random.seed(key)
    shuffled_indices = list(range(len(flat_array)))
    random.shuffle(shuffled_indices)

    encrypted_array = flat_array[shuffled_indices]
    encrypted_image_array = encrypted_array.reshape(original_shape)

    encrypted_image = Image.fromarray(encrypted_image_array.astype('uint8'))

    save_folder = r'B:\Playground\LNRS\Streamlit\en_docs'
    os.makedirs(save_folder, exist_ok=True)

    original_filename = os.path.basename(image_path)
    encrypted_image.save(os.path.join(save_folder, original_filename))

    return os.path.join(save_folder, original_filename)

# Function to decrypt an image
def decrypt_image(encrypted_image_path, key, original_shape):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)
    flat_encrypted_array = encrypted_array.flatten()

    random.seed(key)
    shuffled_indices = list(range(len(flat_encrypted_array)))
    random.shuffle(shuffled_indices)

    decrypted_array = np.empty_like(flat_encrypted_array)
    for i, shuffled_index in enumerate(shuffled_indices):
        decrypted_array[shuffled_index] = flat_encrypted_array[i]

    decrypted_image_array = decrypted_array.reshape(original_shape)
    decrypted_image = Image.fromarray(decrypted_image_array.astype('uint8'))

    return decrypted_image

# Function to list available images in a folder
def get_image_list(folder_path):
    supported_formats = ['png', 'jpg', 'jpeg']
    return [f for f in os.listdir(folder_path) if f.split('.')[-1].lower() in supported_formats]

def show():
    st.title("Encryption/Decryption")

    # Choose between Encrypt or Decrypt
    option = st.radio("Choose an option", ["Encrypt an image", "Decrypt an image"])

    if option == "Encrypt an image":
        # Encryption flow
        uploaded_image = st.file_uploader("Upload an image to encrypt", type=["png", "jpg", "jpeg"])
        encryption_key = st.text_input("Enter a PIN for encryption", type="password")

        if st.button("Encrypt"):
            if uploaded_image is None:
                st.error("Please upload an image.")
            elif not encryption_key:
                st.error("Please enter a PIN.")
            else:
                # Save uploaded image with its original name
                image_path = os.path.join("temp", uploaded_image.name)  # Save it as the original name in a temp folder
                os.makedirs("temp", exist_ok=True)  # Create the folder if it doesn't exist
                with open(image_path, "wb") as f:
                    f.write(uploaded_image.getbuffer())

                # Encrypt the image
                encrypted_image_path = encrypt_image(image_path, encryption_key)

                st.success(f"Image successfully encrypted and saved to: {encrypted_image_path}")

    elif option == "Decrypt an image":
        # Decryption flow
        encrypted_image_folder = r'B:\Playground\LNRS\Streamlit\en_docs'  # Folder where encrypted images are stored

        # Get list of encrypted images
        image_list = get_image_list(encrypted_image_folder)

        if not image_list:
            st.error("No encrypted images found in the folder.")
        else:
            selected_image = st.selectbox("Select an encrypted image to decrypt", image_list)
            decryption_key = st.text_input("Enter the PIN for decryption", type="password")

            if st.button("Decrypt"):
                if not selected_image:
                    st.error("Please select an encrypted image.")
                elif not decryption_key:
                    st.error("Please enter the PIN.")
                else:
                    # Get the full path of the selected image
                    encrypted_image_path = os.path.join(encrypted_image_folder, selected_image)

                    # Load the image to get its shape (assuming it's the same as original)
                    encrypted_image = Image.open(encrypted_image_path)
                    original_shape = np.array(encrypted_image).shape

                    # Decrypt the image
                    decrypted_image = decrypt_image(encrypted_image_path, decryption_key, original_shape)

                    # Provide download option for the decrypted image
                    buf = io.BytesIO()
                    decrypted_image.save(buf, format="PNG")
                    byte_data = buf.getvalue()

                    st.success("Image successfully decrypted.")
                    st.download_button(label="Download Decrypted Image", data=byte_data, file_name="decrypted_image.png", mime="image/png")
