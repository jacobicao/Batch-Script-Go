import os
name = 'album'
L = {}
root = os.path.dirname(os.path.realpath(__file__)) 
for i in os.listdir(root):
    if not os.path.isfile(os.path.join(root,i)):
        continue
    d = os.path.splitext(i)
    if d[1] != '.txt' or d[0] == name:
        continue
    with open(i,'r') as f:
        c = f.read()
        L[d[0]] = c.strip()

fc = open('%s.txt'%name,'w')
keys = sorted(L.keys(),reverse=True)
for k in keys:
    fc.write(k)
    fc.write('\n')
    fc.write(L.get(k))
    fc.write('\n'+'='*20+'\n\n')

fc.close()
