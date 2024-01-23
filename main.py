from PIL import Image
import os

def custom_resize(input_path, output_path, dimensions=(512, 512)):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(dimensions, Image.LANCZOS)  
            
            # Save the resized image
            resized_img.save(output_path)
            
            print(f"Image successfully resized and saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def batch_resize_images(input_dir, output_dir, dimensions=(512, 512)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            custom_resize(input_path, output_path, dimensions)

if __name__ == "__main__":
    input_directory = "." 
    output_directory = "resized_images"
    
    # Resize all images in the current directory
    batch_resize_images(input_directory, output_directory)
