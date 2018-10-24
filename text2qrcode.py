# -*- coding: utf-8 -*
import qrcode, zlib
import os, sys, getopt
line = 100

if len(sys.argv) < 2:
    raise Exception("Please input one file name as a object!")
name = sys.argv[1]
if not os.path.exists(name):
    raise Exception("The file (%s) does not exist!" % name)
suffix = ""
compress = False
opts, args = getopt.getopt(sys.argv[2:],"",["compress","line="])
for op, value in opts:
    if op == "--compress":
        compress = True
    elif op == "--line":
        line = int(value)

with open("%s"%name) as f:
    t = f.readlines()

l = len(t)//line+1
for i in range(l):
    s = ''.join(t[i*line:(i+1)*line])
    z = zlib.compress(s.encode())
    print(len(s), "before compress")
    print(len(z), "after compress")
    if compress:
        s = z
        suffix = "_compress"
        print("compress")
    try:
        img = qrcode.make(s)
    except Exception as e:
        raise Exception("Maybe the file is too long. Try to add command option --line 30.")
        break
    imgname = '%s.png'%(name.split('.')[0]+'_'+str(i+1)+suffix)
    img.save(imgname)
    print("Finish! See %s!"%imgname)
