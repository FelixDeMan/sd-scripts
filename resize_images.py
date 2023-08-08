import os
from PIL import Image

extensions = ['jpg', 'jpeg', 'png']

folder = 'newstuff/pics/white-chair_denoised'
for image in os.listdir(folder):
    if image.split('.')[-1] not in extensions:
        print(image)
        continue
    img_path = os.path.join(folder,image)
    print(img_path)
    img = Image.open(img_path)
    img = img.resize((1024, 1024))
    img.save(img_path)

