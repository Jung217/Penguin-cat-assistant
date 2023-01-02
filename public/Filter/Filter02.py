from PIL import Image,ImageFilter

img = Image.open(r"C:\Users\alex2\Desktop\照片\img1.png")

imgFilter = img.filter(ImageFilter.BLUR) #模糊
imgFilter.save("BLUR.jpg") 
imgFilter.show()

imgFilter = img.filter(ImageFilter.CONTOUR) #增強輪廓
imgFilter.save("CONTOUR.jpg")
imgFilter.show()

imgFilter = img.filter(ImageFilter.DETAIL) #增強細節
imgFilter.save("DETAIL.jpg") 
imgFilter.show()

imgFilter = img.filter(ImageFilter.EDGE_ENHANCE) #增強邊緣
imgFilter.save("EDGE_ENHANCE.jpg")
imgFilter.show()

imgFilter = img.filter(ImageFilter.EDGE_ENHANCE_MORE) #深度增強邊緣
imgFilter.save("EDGE_ENHANCE_MORE.jpg") 
imgFilter.show()

imgFilter = img.filter(ImageFilter.EMBOSS) #浮雕
imgFilter.save("EMBOSS.jpg")
imgFilter.show()

imgFilter = img.filter(ImageFilter.FIND_EDGES) #找出圖片邊緣資訊
imgFilter.save("FIND_EDGES.jpg") 
imgFilter.show()

imgFilter = img.filter(ImageFilter.SMOOTH) #平滑 使圖片亮度平緩漸變
imgFilter.save("SMOOTH.jpg")
imgFilter.show()

imgFilter = img.filter(ImageFilter.SMOOTH_MORE) #深度平滑
imgFilter.save("SMOOTH_MORE.jpg") 
imgFilter.show()

imgFilter = img.filter(ImageFilter.SHARPEN) #銳化
imgFilter.save("SHARPEN.jpg")
imgFilter.show()