from ctypes import resize
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# OR img.convert('L') -> for grey image
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save("blur.png", "png")

filter_img = img.convert('L')
box = (100, 100, 400, 400)
region = filter_img.crop(box)
region.save("grey.png", "png")

# filter_img.show()

resize = img.resize((300, 300))
resize.save('small_img.png', 'png')

print(img)
print(img.format)
print(img.size)
print(img.mode)


img2 = Image.open('./astro.jpg')
print(img2.size)
img2.thumbnail((400, 400))
img2.save('thumbnail.jpg')
