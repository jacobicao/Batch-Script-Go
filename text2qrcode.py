import qrcode, zlib
import os, sys, getopt
if len(sys.argv) < 2:
    raise Exception("Please input one file name as a object!")
name = sys.argv[1]
if not os.path.exists(name):
    raise Exception("The file (%s) does not exist!" % name)
suffix = ""
compress = False
opts, args = getopt.getopt(sys.argv[2:],"",["compress"])
if ("--compress","") in opts:
    compress = True
with open("%s"%name) as f:
    s = f.readlines()
s = ''.join(s)
z = zlib.compress(s.encode())
print(len(s), "before compress")
print(len(z), "after compress")
if compress:
    s = z
    suffix = "_compress"
    print("compress")
img = qrcode.make(s)
imgname = '%s.png'%(name.split('.')[0]+suffix)
img.save(imgname)
print("Finish! See %s!"%imgname)
