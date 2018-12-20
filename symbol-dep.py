#!/usr/bin/python3

import sys, getopt, os

def main(argv):
   srcfile = ''
   dstfile = ''
   neededsymbols=[]
   exportedsymbols=[]
   try:
      opts, args = getopt.getopt(argv,"hs:d:",["sfile=","dfile="])
   except getopt.GetoptError:
      print ('symbol-dep.py -s <srcfile> -d <dstfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('symbol-dep.py -s <srcfile> -d <dsrfile>')
         sys.exit()
      elif opt in ("-s", "--sfile"):
         srcfile = arg
      elif opt in ("-d", "--dfile"):
         dstfile = arg

   # get the symbols srcfile depends on
   src=os.popen("nm -D --undefined-only "+srcfile)
   srclist=src.read().splitlines()
   for sline in srclist:
      neededsymbols.append(sline.split()[-1])

   # get the symbols dstfile exports
   dst=os.popen("nm -D --defined-only "+dstfile)
   dstlist=dst.read().splitlines()
   for dline in dstlist:
      exportedsymbols.append(dline.split()[-1])

   # intersection of src and dest	
   for symbol in neededsymbols:
      if symbol in exportedsymbols:
         print(symbol)


if __name__ == "__main__":
   main(sys.argv[1:])
