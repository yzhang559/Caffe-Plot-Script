#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:49:53 2017

@author: yzhang559
"""

import os
from PIL import Image
#from PIL.ExifTags import TAGS

albumdir = 'transparent'
thumbdir = albumdir + '/thumbs'

def mkdir(dirname):
  try:
    os.mkdir(dirname)
  except:
    pass

def maxSize(image, maxSize, method = 3):
  imAspect = float(image.size[0])/float(image.size[1])
  outAspect = float(maxSize[0])/float(maxSize[1])

  if imAspect >= outAspect:
    return image.resize((maxSize[0], int((float(maxSize[0])/imAspect) + 0.5)), method)
  else:
    return image.resize((int((float(maxSize[1])*imAspect) + 0.5), maxSize[1]), method)

def processImage(imgdir, fname):
  img = Image.open(imgdir + fname)
  exif = img._getexif()
  if exif != None:
    for tag, value in exif.items():
#      decoded = TAGS.get(tag, tag)
#      if decoded == 'Orientation':
#        if value == 3: img = img.rotate(180)
#        if value == 6: img = img.rotate(270)
#        if value == 8: img = img.rotate(90)
        img = maxSize(img, (1024, 768), Image.ANTIALIAS)
  #img.save(albumdir + '/' + fname, 'JPEG', quality=100)
  img.thumbnail((256, 256), Image.ANTIALIAS)
  background = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
  background.paste(
    img, (int((256 - img.size[0]) / 2), int((256 - img.size[1]) / 2))
)
  background.save(thumbdir + '/' + fname, 'JPEG')

def main():
#  if len(sys.argv) < 2:
#    print "Usage: album.py imgdir"
#    exit(0)
#  else:

  imgdir = '/Users/Jenny/Desktop/room/val/'

  mkdir(albumdir)
  mkdir(thumbdir)
  files = os.listdir(imgdir)

  for fname in files:
    if fname.lower().endswith('.jpeg'):
      processImage(imgdir, fname)
      print fname

  print 'done'

if __name__ == "__main__":
  main()