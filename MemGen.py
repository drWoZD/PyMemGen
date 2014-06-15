#!/usr/bin/python
#-*- ecoding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from getopt import getopt
import sys
import os

class MemGen:
    def __init__(self, image="", uptext="", downtext="", font="", color="white"):
        if image: self.setImage(image)
        if uptext: self.setUpText(uptext)
        if downtext: self.etDownText(downtext)
        if font: self.setFont(font)
        if color: self.setColor(color)
        
    def setImage(self, image):
        self.img  = Image.open(image)
        self.draw = ImageDraw.Draw(self.img)
        self.size = self.img.size

    def setUpText(self, text):
        self.uptext = text
        
    def setDownText(self, text):
        self.downtext = text
        
    def setFont(self, name):
        self.fontname = name
        
    def setColor(self, name):
        self.color = name
        
    def printUp(self):
        n = int(self.size[1]/6)

        font = ImageFont.truetype(self.fontname, n)
        txtsz = self.draw.textsize(self.uptext, font)
        while (self.size[0]-txtsz[0]) < 10:
           del font
           n = n - 1
           font = ImageFont.truetype(self.fontname, n)
           txtsz = self.draw.textsize(self.uptext, font)

        textpos = (int((self.size[0] - txtsz[0])/2), 0)
        self.draw.text(textpos, self.uptext, fill=self.color, font=font)
    
    def printDown(self):
        n = int(self.size[1]/6)

        font = ImageFont.truetype(self.fontname, n)
        txtsz = self.draw.textsize(self.downtext, font)
        while (self.size[0]-txtsz[0]) < 10:
            del font
            n = n - 1
            font = ImageFont.truetype(self.fontname, n)
            txtsz = self.draw.textsize(self.downtext, font)

        textpos = (int((self.size[0] - txtsz[0])/2), self.size[1]-txtsz[1])
        self.draw.text(textpos, self.downtext, fill=self.color, font=font)
    
    def generate(self):
        if self.uptext:
	    self.printUp()
	if self.downtext:
	    self.printDown()
	    
    def save(self, path="out.png"):
        self.img.save(path, "PNG")
        
if __name__ == "__main__":
    #out = "out.png"
    #color = "green"
    #font = os.path.realpath(__file__)) + 
    opts, args = getopt(sys.argv[1:], "u:d:s:o:c:f:", ["uptext=", "downtext=", "source-image=", "output-image=", "color=", "font="])
    mem = MemGen(font=os.path.dirname(os.path.realpath(__file__)) + "/ttf/DejaVuSans.ttf")
    for o, a in opts:
        if o in ("-u", "--uptext"):
            mem.setUpText(unicode(a, 'utf-8'))
        elif o in ("-d", "--downtext"):
            mem.setDownText(unicode(a, 'utf-8'))
        elif o in ("-s", "--source-image"):
            file = os.path.dirname(os.path.realpath(__file__)) + "/images/" + a
            file = [a, file][os.path.exists(file)]
            mem.setImage(file)
        elif o in ("-o", "--output-image"):
            out = a
        elif o in ("-c", "--color"):
            mem.setColor(a)
        elif o in ("-f", "--font"):
            file = os.path.dirname(os.path.realpath(__file__)) + "/ttf/" + a
            file = [a, file][os.path.exists(file)]
            mem.setFont(file)

    mem.generate()
    mem.save();
    """ 
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
    """
