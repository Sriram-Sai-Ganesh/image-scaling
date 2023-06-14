# get image filenames
import os
import glob
# scale images
import cv2
import matplotlib.pyplot as plt



###############################
# Modify image i/o location here (different locations)
IMAGE_FOLDER = "./in"
OUTPUT_FOLDER = "./out"

# Set image scale here: (above 0)
SCALE_FACTOR = 0.75

# Set interpolation method (if enlarging images):
# cv2.INTER_LINEAR 		-- The standard bilinear interpolation, ideal for enlarged images.
# cv2.INTER_NEAREST 	-- The nearest neighbor interpolation, which, though fast to run, creates blocky images.
# cv2.INTER_AREA 		-- The interpolation for the pixel area, which scales down images.
# cv2.INTER_CUBIC 		-- Bicubic interpolation with 4×4-pixel neighborhoods. High-quality images but slower to run.
# cv2.INTER_LANCZOS4 	-- Lanczos interpolation with an 8×8-pixel neighborhood. Images of the highest quality, but slowest to run.
INTERPOLATION_METHOD = cv2.INTER_LANCZOS4

DEBUG = False
###############################


assert IMAGE_FOLDER is not OUTPUT_FOLDER, "IMAGE_FOLDER cannot be the same as OUTPUT_FOLDER"
assert SCALE_FACTOR>0 , "SCALE_FACTOR must be a positive decimal number"


def get_image_filenames(folder_path):
    image_extensions = ["*.jpg", "*.jpeg", "*.png"]  # Add or remove extensions as needed
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(folder_path, extension)))
    return image_files

def scale_image(image_path):
	# read image
	original_image = cv2.imread(image_path)
	if(DEBUG): print('Image dimensions are ', original_image.shape)

	# width and height modified by SCALE_FACTOR :
	width = int(original_image.shape[1] * SCALE_FACTOR)
	height = int(original_image.shape[0] * SCALE_FACTOR)
	new_dim = (width, height)

	# resize image
	resized_image = cv2.resize(original_image, new_dim, interpolation = INTERPOLATION_METHOD)

	# save image
	if(DEBUG): print("Saving image...")
	cv2.imwrite(OUTPUT_FOLDER+image_path.split("\\")[-1], resized_image)

IMAGE_FOLDER += "/"
OUTPUT_FOLDER += "/"

# Example usage:
folder_path = IMAGE_FOLDER
image_files_list = get_image_filenames(folder_path)

if(DEBUG): 
	print("List of image file names:\n",image_files)
	print(f"resize.py:\nDownsizing all images at {IMAGE_FOLDER} to {SCALE_FACTOR}x\n")


for image_path in image_files_list:
	scale_image(image_path)

