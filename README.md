# libdep: tools to analyze how programs depend on libraries
## symbol-dep.py: how programs depend on functions in libraries
```console
$./symbol-dep.py -s a.out -d /lib/i386-linux-gnu/libc-2.19.so 
_exit
__libc_start_main
puts
```
