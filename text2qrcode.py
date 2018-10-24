import qrcode
import zlib
import os
import sys
if len(sys.argv) is not 2:
    raise Exception("Please input one file name as a object!")
name = sys.argv[1]
if not os.path.exists(name):
    raise Exception("The file (%s) does not exist!" % name)
with open("%s"%name) as f:
    s = f.readlines()
s = ''.join(s)
z = zlib.compress(s.encode())
print(len(s), "before compress")
print(len(z), "after compress")
imgname = '%s.png'%name.split('.')[0]
img = qrcode.make(s)
img.save(imgname)
print("Finish! See %s!"%imgname)
