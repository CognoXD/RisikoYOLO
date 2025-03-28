import os
import random 
import shutil

# Create datasets directory if it doesn't exist (YOLO wants a directory datasets/)
# and a subdirectory for the dataset, e.g. datasets/risiko

dataset_dir = 'datasets/risiko'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Create directories for images and labels
# and subdirectories for train and val, e.g. datasets/risiko/train/images
images_dir = 'images'
labels_dir = 'labels'
train_images_dir = dataset_dir + '/train/images'
train_labels_dir = dataset_dir + '/train/labels'
val_images_dir = dataset_dir + '/val/images'
val_labels_dir = dataset_dir + '/val/labels'
train_ratio = 0.8 # 80/20 rule

# Create directories if they don't exist
for dir in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir]:
    if not os.path.exists(dir):
        os.makedirs(dir)

images = os.listdir(images_dir)
#print(images)
random.shuffle(images)

# Move images and labels to train and val directories
split_index = int(len(images) * train_ratio)
train_files = images[:split_index]
val_files = images[split_index:]
print(f"Number of training images: {len(train_files)}")
print(f"Number of validation images: {len(val_files)}")


# Funzione per spostare i file
def move_files(file_list, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for file in file_list:
        img_path = os.path.join(src_img_dir, file)
        lbl_path = os.path.join(src_lbl_dir, file.replace(".jpg", ".txt"))
        
        if os.path.exists(lbl_path):
            shutil.move(img_path, dest_img_dir)
            shutil.move(lbl_path, dest_lbl_dir)

# Spostare i file nelle rispettive cartelle
move_files(train_files, images_dir, labels_dir, train_images_dir, train_labels_dir)
move_files(val_files, images_dir, labels_dir, val_images_dir, val_labels_dir)

print("Dataset suddiviso con successo!")
