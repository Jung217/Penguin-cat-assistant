from urllib import request
from PIL import Image

url = "https://raw.githubusercontent.com/Jung217/Penguin-cat-assistant/main/pic/me.png"
img1 = Image.open(request.urlopen(url))
img2 = Image.open(r"後製圖片路徑")

w, h = img2.size
PY = int(h-(w/2*0.86))
imgP = img1.resize((int(w/2), int(w/2*0.87)))

foreground = imgP
Result = img2

Result.paste(foreground, (-5, PY), foreground)
Result.show()