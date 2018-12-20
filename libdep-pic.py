#!/usr/bin/python3

import sys, os, re

analyzedlist = []

# get the libs prog depends on and write the results into opened file f
def dep(f, prog):
   # one lib may be used by several users
   if prog in analyzedlist:
       return
   else:
       analyzedlist.append(prog) 

   pname = prog.split('/')[-1]
   needed=os.popen("ldd "+prog)
   neededso=re.findall(r'[>](.*?)[(]', needed.read())
   for so in neededso:
       if(len(so.strip()) > 0):
           f.write('"' + pname + '" -> "' + so.split('/')[-1] + '";\n')
           dep(f, so)

def main(argv):
   f = open('/tmp/libdep.dot','w',encoding='utf-8')
   f.write('digraph graphname {\n')
   dep(f, argv)
   f.write('}\n')
   f.close()
   os.popen("dot -Tpng -o ./libdep.png /tmp/libdep.dot")

if __name__ == "__main__":
   if len(sys.argv) == 2:
       main(sys.argv[1])
   else:
       print ("usage: libdep-pic.py [program]")
