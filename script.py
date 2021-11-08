from PIL import Image
import numpy as np
import json

img = Image.open('img.png')

# print(img.format)
# print(img.size)
# print(img.mode)

numpydata = np.asarray(img)
# print(numpydata)


mapping ={}
for row in numpydata:
    for pixel in row:
        rgb=json.dumps({'r':int(pixel[0]),'g':int(pixel[1]),'b':int(pixel[2])})
        # print(rgb)
        s=json.dumps(rgb)
        if s in mapping:
            mapping[json.dumps(rgb)]=mapping[json.dumps(rgb)]+1
        else:
            mapping[json.dumps(rgb)]=1

# print("*"*50)
# mylist=[]

# # finalnparray=np.array([255,0,0])
# finalnparray=np.array([]).reshape((0,3))
# print(finalnparray)

# for element in sorted(mapping, key=mapping.get, reverse=True):
#     val=mapping[element]
#     key=json.loads(element)
#     key=json.loads(key)
#     print(key)
#     print(type(key))
#     red=key.get('r')
#     green=key.get('g')
#     blue=key.get('b')

#     # print(red)
#     # print(green)
#     # print(blue)

#     rgbnumpy=np.array([red,green,blue])

#     print(type(rgbnumpy))
#     print(rgbnumpy)

#     # finalnparray=np.append(finalnparray,rgbnumpy,axis=1)
#     finalnparray=np.vstack((finalnparray,rgbnumpy))
#     print(finalnparray)

# finalnparray=np.array([finalnparray])
# PIL_image = Image.fromarray(np.uint8(finalnparray)).convert('RGB')
# print(PIL_image)

# PIL_image.save("color_pallete_1px.png")

#end of solution 1, second impl for larger color palette

largeimglist=[]

for element in sorted(mapping, key=mapping.get, reverse=True):
    val=mapping[element]
    key=json.loads(element)
    key=json.loads(key)
    # print(key)
    # print(type(key))
    red=key.get('r')
    green=key.get('g')
    blue=key.get('b')
    largeimglist.append(Image.new(mode = "RGB", size = (64, 64),color = (red, green, blue)))

images = largeimglist
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('color_pallete_64px.png')

#todo, limit to 5 colors
#expose api for image upload and return color codes/generated pallete image
#display result on webpage
#add image upload and result display in UI
#add multi threading support. Divide image in equal parts.
#Create benchmark for 1 to 16 number of threads
#Use GPU if possible
# https://stackoverflow.com/questions/41825593/python-pillow-library-uses-cpu-for-image-processing-can-it-be-done-on-gpu

#write browser only code in javascript
#https://stackoverflow.com/questions/46074473/efficiently-iterating-through-image-in-javascript

#provide 3 color version free, donation for unlimited/30/etc version