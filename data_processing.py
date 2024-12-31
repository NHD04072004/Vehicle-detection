import os
from sklearn.model_selection import train_test_split
import shutil

source_images = 'datasource/images'
source_labels = 'datasource/labels'
destination = 'data'

os.makedirs(os.path.join(destination, 'train/images'), exist_ok=True)
os.makedirs(os.path.join(destination, 'train/labels'), exist_ok=True)
os.makedirs(os.path.join(destination, 'test/images'), exist_ok=True)
os.makedirs(os.path.join(destination, 'test/labels'), exist_ok=True)

images = [f for f in os.listdir(source_images) if f.endswith('.jpg')]
labels = [f.replace('.jpg', '.txt') for f in images]

train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

for img, lbl in zip(train_images, train_labels):
    shutil.copy(os.path.join(source_images, img), os.path.join(destination, 'train/images', img))
    shutil.copy(os.path.join(source_images, lbl), os.path.join(destination, 'train/labels', lbl))

for img, lbl in zip(test_images, test_labels):
    shutil.copy(os.path.join(source_images, img), os.path.join(destination, 'test/images', img))
    shutil.copy(os.path.join(source_images, lbl), os.path.join(destination, 'test/labels', lbl))