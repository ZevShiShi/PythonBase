# 使用PIL操作图像

import Image, ImageDraw, ImageFont, ImageFilter
import random


# 图像缩放操作
# try:
#     im = Image.open('nier.jpg')  # 打开一个jpg图像文件，注意路径要改成你自己的:
#     w, h = im.size  # 获得图像尺寸:
#     im.thumbnail((w / 2, h / 2))  # 缩放到50%:
#     im.save('nier.png', 'png')  # 把缩放后的图像用png格式保存:
#     print('保存图片成功')
# except Exception as e:
#     print('保存图片error:', e)

# 图像模糊效果
# try:
#     im = Image.open('nier.png')
#     im = im.filter(ImageFilter.BLUR)
#     im.save('blur.jpg', 'jpeg')
#     print('模糊图片成功')
# except Exception as e:
#     print('图片error:', e)

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


try:
    # 240 x 60:
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')
    print('保存图片成功')
except Exception as e:
    print('error', e)
