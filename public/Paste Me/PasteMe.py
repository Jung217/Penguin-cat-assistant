from urllib import request
from PIL import Image

url = "https://raw.githubusercontent.com/Jung217/Penguin-cat-assistant/main/pic/me.png"
img1 = Image.open(request.urlopen(url))
img2 = Image.open(r"路徑") #改成要後製的圖片路徑

w, h = img2.size #取輸入圖片尺寸

if w > h or w == h:
    PY = int(h-(w/2*0.86)) #調整貼上位置
    imgP = img1.resize((int(w/2), int(w/2*0.87))) #以背景調整貼上圖片大小
if w < h:
    PY = int(h-(h/2*0.86)) #調整貼上位置
    imgP = img1.resize((int(h/2), int(h/2*0.87))) #以背景調整貼上圖片大小


foreground = imgP
Result = img2

Result.paste(foreground, (-5, PY), foreground) #貼上圖片
Result.save("paste_me1.jpg") #儲存
Result.show() #開啟展示