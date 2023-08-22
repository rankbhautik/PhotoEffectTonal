from PIL import Image, ImageFilter

def apply_tonal_effect(image_path):
    # Open the image
    original_image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = original_image.convert("L")
    
    # Apply a custom tonal transformation (you can modify this to achieve the desired effect)
    tonal_image = Image.eval(grayscale_image, lambda x: x * 1.5)
    
    return tonal_image

# Path to your input image
input_image_path =  'your_image.png'

# Apply the tonal effect
tonal_result = apply_tonal_effect(input_image_path)

# Show the original and tonal images
tonal_result.show()
