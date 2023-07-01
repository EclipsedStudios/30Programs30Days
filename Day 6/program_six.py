import os
from PIL import Image

file_name = input("Enter the name of the file you want to resize (Make sure it is contained in the Day 6 folder): ")

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        resized_image = image.resize(size)
        resized_image.save(output_image_path)

current_directory = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_directory, file_name)

file_name_split = file_name.split('.')
file_name = file_name_split[0] + '_resized.' + file_name_split[1]

target_width = int(input("Enter the width of the resized image: "))
target_height = int(input("Enter the height of the resized image: "))

output_path = os.path.join(current_directory, f'{file_name}')
target_size = (target_width,target_height)

resize_image(input_path, output_path, target_size)
