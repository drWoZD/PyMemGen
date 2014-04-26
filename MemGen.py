#!/usr/bin/python
#-*- ecoding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from getopt import getopt
import sys

def print_up(draw,  size, text, color="white", fontname="ttf/DejaVuSans.ttf"):
    n = int(size[1]/6)

    font = ImageFont.truetype(fontname, n)
    txtsz = draw.textsize(text, font)
    while (size[0]-txtsz[0]) < 10:
        del font
        n = n - 1
        font = ImageFont.truetype(fontname, n)
        txtsz = draw.textsize(text, font)
    
    textpos = (int((size[0] - txtsz[0])/2), 0)
    draw.text(textpos, text, fill=color, font=font)

def print_down(draw,  size, text, color="white", fontname="ttf/DejaVuSans.ttf"):
    n = int(size[1]/6)

    font = ImageFont.truetype(fontname, n)
    txtsz = draw.textsize(text, font)
    while (size[0]-txtsz[0]) < 10:
        del font
        n = n - 1
        font = ImageFont.truetype(fontname, n)
        txtsz = draw.textsize(text, font)
    
    textpos = (int((size[0] - txtsz[0])/2), size[1]-txtsz[1])
    draw.text(textpos, text, fill=color, font=font)
    


if __name__ == "__main__":    
    out = "out.png"
    color = "green"
    font="ttf/DejaVuSans.ttf"
    opts, args = getopt(sys.argv[1:], "u:d:s:o:c:f:", ["uptext=", "downtext=", "source-image=", "output-image=", "color=", "font="])
    for o, a in opts:
        if o in ("-u", "--uptext"):
            uptext = unicode(a, 'utf-8')
        elif o in ("-d", "--downtext"):
            downtext = unicode(a, 'utf-8')
        elif o in ("-s", "--source-image"):
            img = Image.open(a)
            draw = ImageDraw.Draw(img)
        elif o in ("-o", "--output-image"):
            out = a
        elif o in ("-c", "--color"):
	    color = a
	elif o in ("-f", "--font"):
	    font = a

    while 1:    
        try:
            print_up(draw, img.size, uptext, color, font)
            print_down(draw, img.size, downtext, color, font)
            img.save(out, "PNG")
            break
        except NameError as err:
            t = str(err).split("'")[1]
            if t == "draw":
	        img = Image.open(unicode(raw_input("Enter source file name: "), 'utf-8'))
	        draw = ImageDraw.Draw(img)
	    elif t == "uptext":
	        uptext = unicode(raw_input("Enter up text: "), 'utf-8')
	    elif t == "downtext":
	        downtext = unicode(raw_input("Enter down text: "), 'utf-8')
	