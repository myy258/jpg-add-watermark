# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:50:23 2021

@author: yazce
"""

import os
from PIL import Image, ImageDraw, ImageFont

def filepath(docname):
    img_suffix_list = ['jpg']
    for i in os.listdir(f"C:/Users/Yiyu.Mo/Desktop/商城水印/{docname}/"):
        if i.split('.')[-1] in img_suffix_list:
            open_img(i,docname)

def open_img(filename,docname):
    imageFile = f'C:/Users/Yiyu.Mo/Desktop/商城水印/{docname}/{filename}'
    markfile = 'C:/Users/Yiyu.Mo/Desktop/商城水印/水印.png'

    img = Image.open(imageFile)
    mark = Image.open(markfile)
    
    mark = mark.convert('RGBA')
    r, g, b, alpha = mark.split()
    alpha = alpha.point(lambda i: i>0 and 76.5)
    mark.putalpha(alpha)


    # def addTransparency(img,factor):
    #     img = img.convert('RGBA')
    #     img_blender = Image.new('RGBA', img.size, (0,0,0,0))
    #     img = Image.blend(img_blender, img, factor)
    #     return img
    # mark = addTransparency(mark,0.4)
 
    base_width = 349
    w_percent = base_width / float(mark.size[0])
    h_size = int(float(mark.size[1]) * float(w_percent))
    mark = mark.resize((base_width, h_size), Image.ANTIALIAS)
    
    img_size = img.size
    wm_size = mark.size
    
    wm_position = (int((img_size[0]-wm_size[0])/2),int((img_size[1]-wm_size[1])/2))
    layer = Image.new('RGBA', img.size)
    layer.paste(mark, wm_position)
    mark_img = Image.composite(layer, img, layer)
    
    if os.path.exists(f"C:/Users/Yiyu.Mo/Desktop/1/{docname}"):
        pass
    else:
        os.mkdir(f"C:/Users/Yiyu.Mo/Desktop/1/{docname}")
    
    mark_img.save(f"C:/Users/Yiyu.Mo/Desktop/1/{docname}/{filename}",quality=95)
    
if __name__ == '__main__':
    filepath('其他')