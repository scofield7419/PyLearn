#常用第三方模块
#基本上，所有的第三方模块都会在 PyPI - the Python Package Index 上注
#册，只要找到对应的模块名字，即可用 pip 安装。

#PIL  Python Imaging Library
#已经是 Python 平台事实上的图像处理标准库了。PIL 功能非常强大，但 API 却非常简单易用。
#PIL 提供了操作图像的强大功能

from PIL import Image, ImageFilter
# 打开一个 jpg 图像文件，注意是当前路径:
im = Image.open('test.png')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到 50%:
#im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用 png 格式保存:
#im.save('thumbnail.png', 'png')


# 打开一个 png 图像文件，注意是当前路径:
im = Image.open('test.png')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png', 'png')




















