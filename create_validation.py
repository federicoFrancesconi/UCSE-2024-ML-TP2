import os
import shutil
import random

# Paths to directories
base_dir = '/media/federico/secondary/Repositorios/UCSE/MachineLearning/data_tp2/'
train_dir = base_dir + 'train'
validation_dir = base_dir + 'validation'

# Percentage of images to move to validation
val_split = 0.2

# Create validation subdirectories
os.makedirs(validation_dir, exist_ok=True)
for class_name in os.listdir(train_dir):
    class_train_dir = os.path.join(train_dir, class_name)
    class_val_dir = os.path.join(validation_dir, class_name)
    os.makedirs(class_val_dir, exist_ok=True)

    # List images in the current class directory
    images = os.listdir(class_train_dir)
    val_count = int(len(images) * val_split)
    val_images = random.sample(images, val_count)
    
    # Move selected images to validation folder
    for image in val_images:
        src = os.path.join(class_train_dir, image)
        dst = os.path.join(class_val_dir, image)
        shutil.move(src, dst)

print("Validation set created successfully.")