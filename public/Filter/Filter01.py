from PIL import Image

img = Image.open(r"C:\Users\alex2\Desktop\照片\img1.png")

imgG = img.convert('L') # 灰階
imgG.save("GRAY.jpg")
imgG.show()

w,h = img.size

for i in range(w):
    for j in range(h):
        if imgG.getpixel((i,j)) < 150:  # < n 可自行調整
            imgG.putpixel((i,j),(0))
        else:
            imgG.putpixel((i,j),(255))

imgG.save("THRESH.jpg") #黑白
imgG.show()