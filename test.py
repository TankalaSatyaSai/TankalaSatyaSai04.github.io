import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageDraw, ImageSequence, Image

# Load the base image
image = Image.open("/home/satyasai04/portfolio/assets/img/header-img.png").convert("RGBA")
frames = []

# Function to move the arm (wave effect)
def move_arm(base_image, angle):
    img_copy = base_image.copy()
    draw = ImageDraw.Draw(img_copy)

    # Manipulate the coordinates for a waving arm effect
    # (assuming left arm is the one waving based on image orientation)
    # This is a simple mock for demonstration (move arm up or down slightly)

    wave_offsets = {
        0: (-5, -10),
        1: (5, 10),
        2: (-10, -5),
        3: (10, 5)
    }
    
    offset = wave_offsets[angle % 4]
    draw.ellipse([(160 + offset[0], 200 + offset[1]), (200 + offset[0], 240 + offset[1])], fill=(255, 255, 255, 255))
    return img_copy

# Function to simulate eye blinking
def blink_eyes(image, blink_frame):
    img_copy = image.copy()
    draw = ImageDraw.Draw(img_copy)

    if blink_frame % 2 == 0:
        # Simulate eyes closed
        draw.rectangle([(165, 115), (210, 130)], fill=(0, 0, 0, 255))
    else:
        # Keep eyes open (original state)
        pass
    return img_copy

# Create frames for the gif
for i in range(8):
    # Waving arm effect
    waving_frame = move_arm(image, i)
    
    # Add eye blinking every 4 frames
    blinking_frame = blink_eyes(waving_frame, i)

    # Add frame to list
    frames.append(blinking_frame)

# Save as GIF
gif_path = "/mnt/data/robot_wave_blink.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=200, loop=0)

gif_path  # Output path for the generated GIF
