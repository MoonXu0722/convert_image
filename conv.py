
from PIL import Image

daughter = Image.open("H:\\puzz\\image-format-converter-master\\a.png")
rgb_im = daughter.convert('RGB'); 
rgb_im.save('a.jpg', 'JPEG');