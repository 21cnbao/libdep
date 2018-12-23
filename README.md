# libdep: tools to analyze how programs depend on libraries
## symbol-dep.py: how programs depend on functions in libraries
```console
$./symbol-dep.py -s a.out -d /lib/i386-linux-gnu/libc-2.19.so 
_exit
__libc_start_main
puts
```
## libdep-pic.py: how programs depend on other libraries
```console
$ ./libdep-pic.py /usr/lib/firefox/firefox
```
you will see a diagram libdep.png, open it
```console
~/libdep$ ls
libdep-pic.py  libdep.png  README.md  symbol-dep.py
```
The diagram is like:
https://github.com/21cnbao/libdep/blob/master/example/libdep.png
