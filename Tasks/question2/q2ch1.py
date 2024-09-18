import time
from PIL import Image
import os

# Generate the number
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")

# Load the image
def load_image(folder, filename):
    path = os.path.join(folder, filename)
    return Image.open(path)

# Modify the pixels
def modify_pixels(image, n):
    width, height = image.size
    new_image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_r = (r + n) % 256
            new_g = (g + n) % 256
            new_b = (b + n) % 256
            new_image.putpixel((x, y), (new_r, new_g, new_b))
    return new_image

# Calculate sum of red pixels
def sum_red_pixels(image):
    return sum(image.getpixel((x, y))[0] for x in range(image.width) for y in range(image.height))

# Main process
input_folder = 'CSV'
input_filename = 'chapter1.jpg' 
output_filename = 'CSV/chapter1out.jpg'

original_image = load_image(input_folder, input_filename)
modified_image = modify_pixels(original_image, generated_number)
modified_image.save(output_filename)

red_sum = sum_red_pixels(modified_image)
print(f"Sum of red pixel values: {red_sum}")