#coding:utf-8
"""
# File Name:   PIL_Transparent_Image_Merge.py        
# Author:      Songyi Gao
# CreateTime:  2018.5.11
# Description: Paste the transparent to the other image.
"""

import os,sys
import random
import numpy as np
from PIL import Image

#生成的数字串数目
num = 1000

#生成的数字串长度，限定最短和最长
s,l = 16,19

#数字素材文件夹
fonts_dir = './num_images/'

#产生的图片存放文件夹
images_dir = './images/'

#准备程序运行环境
def bs():
    global images_dir
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
        print('创建图片存放目录： %s' % images_dir)
    try:
        global fonts_dir
        fonts = os.listdir(fonts_dir)
        assert len(fonts) > 0
    except:
        print('没有图片素材可用')


#随机产生数字串
def gen_datas(data_length):
    data = ''
    for i in range(data_length):
        data = data + str(random.randint(0,10))
    return data

#添加透明数字串图片到银行卡图片上
def add_nums_data(newIm,img_b,w_p,h_p):
    #打开背景图片
    #o_imgs = os.listdir('/home/code/gen_data/o_imgs/')
    #o_img_path = os.path.join('/home/code/gen_data/o_imgs/',random.choice(o_imgs))
    #newIm = Image.open(o_img_path)
    w, h = newIm.size
    w1 = 700
    h1 = int((w1*h) / w) - int((w1*h) / w) % 4
    newIm = newIm.resize((w1, h1),Image.ANTIALIAS)
    w1,h1 = newIm.size
    
    r,g,b,a = img_b.split() 
    newIm.paste(img_b,(w_p,h_p),mask = a) 
    
    return newIm

#添加字符串到图片
def add_num(data,data_img_path):   
    #初始化必要变量
    #生成的图片的高度和宽度
    w = h = 0
    
    #数字之间间隔像素
    num_d = 3
    
    #存储数字图片地址列表
    data_imgs_path = []
    ws = []
    hs = []
    
    #随机增加间隔
    p = random.randint(0,5)
    p_w = 15
    
    #随机字体颜色
    data_color = 'red'
    
    #选择数字图片拼接
    for i,d in enumerate(data):
        d_img_path = os.path.join(data_img_path,str(d)+'.png')
        d_img_data = Image.open(d_img_path)
        (d_img_w,d_img_h) = d_img_data.size
        
        ws.append(w)
        hs.append(h)
        
        w += (d_img_w+num_d)
        h += (d_img_h+num_d)
        
        #加间隔
        if p <= 4 and i % 4 ==3:
                w += p_w
        if p == 5 and i%5 == 4:
            w += p_w
        
        if p == 6 and i%6 ==5:
            w += p_w
            
        
        data_imgs_path.append(d_img_path)
        
    #拼接图片
    img_b = Image.new(mode='RGBA', size=(w, 35)) 
    
    for i,j,k in zip(data_imgs_path,ws,hs):
        imq = Image.open(i)
        """
        (w_q,h_q) = imq.size
        imq = np.array(imq)

        for m in range(w_q):
            for n in range(h_q):
                if imq[n][m][-1] == 255:
                    imq[n][m] = [233,233,216,255]
                    
        imq = Image.fromarray(np.uint8(imq))
        """            
        r,g,b,a = imq.split() 
        img_b.paste(imq,(j,0),mask = a)
    
    return img_b

def get_data_img():
    data_length = random.randint(s,l+1)
    data = gen_datas(data_length)
    os_d = os.listdir(fonts_dir)
    data_img_path = os.path.join(fonts_dir,os_d[random.randint(0,len(os_d)-1)])
    img_b = add_num(data,data_img_path)
    return img_b
    
def main():
    #准备环境
    bs()
    
    #随机生成一个图片
    img_p = get_data_img()
    #存储图片
    img_p.save(os.path.join(images_dir,'test.png'))
    
    """
    #透明图片粘贴到背景图片#
    img_b = Image.open(img_path).convert("RGBA") 
    r,g,b,a = img_b.split() 
    img_b.paste(img_p,(w_locate,h_locate),mask = a) 
    """
    
if __name__ == "__main__：
    main()
