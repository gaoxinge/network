from PIL import Image

im = Image.open('test.jpg')

w, h = im.size
im.thumbnail((w/2, h/2))
im.save('thumbnail.jpg')
