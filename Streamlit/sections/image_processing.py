import streamlit as st
from PIL import Image
import os
from Tools import model
import random
import numpy as np

def decrypt_image(encrypted_image_path, key, original_shape):
    # encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image_path)
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

# Function to list image files from a specific folder
def get_image_list(folder_path):
    supported_formats = ['png', 'jpg', 'jpeg']
    return [f for f in os.listdir(folder_path) if f.split('.')[-1].lower() in supported_formats]

def show():
    st.title("Documents Processing")

    # Path to the folder where pre-existing images are stored
    image_folder = r'B:\Playground\LNRS\Streamlit\en_docs'  # Change this to the path of your folder containing images

    # Choose between uploading a new image or selecting one from the folder
    option = st.radio("Choose an option", ["Upload a new image", "Select from existing images"])

    uploaded_image = None  # Initialize to handle conditional logic later
    
    if option == "Upload a new image":
        # Upload image
        uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        
    elif option == "Select from existing images":
        # Get list of images in the folder
        image_list = get_image_list(image_folder)
        
        # If there are no images in the folder, show an error
        if not image_list:
            st.error("No images available in the folder.")
        else:
            # Select an image from the list
            selected_image = st.selectbox("Choose an Secured Document:", image_list)
            key = st.text_input("Enter the Encryption Key:")
            
            # Load the selected image
            image_path = os.path.join(image_folder, selected_image)
            uploaded_image = Image.open(image_path)

    # Text input
    user_input = st.text_input("Enter your query:")

    # Process button
    if st.button("Process"):
        if uploaded_image is None:
            st.error("Please upload or select an image.")
        elif not user_input:
            st.error("Please enter some text.")
        else:
            # Display the uploaded or selected image
            if option == "Upload a new image":
                image = Image.open(uploaded_image)  # Open the uploaded image
            else:
                image = uploaded_image  # Use the selected image from the folder
            original_shape = np.array(image).shape
            # st.write(key,original_shape,type(key))
            image=decrypt_image(image,key,original_shape)
            out=model.noice(image,user_input)
            
            if out=='':
                out="Can't Answer"
            
            st.subheader("Answer:",out)
            st.image(image, caption="Selected Image", use_column_width=True)