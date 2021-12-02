The test .py file is numpy-cv-test.py.
run command "seup_envs.sh" to set up envs.
run command "sh pack.sh" which uses pyinstaller to pack .py file into excutables and run the test func, which will generate three pictures in $PWD.
The excutable file is in "dist" directory.

start_excutable.cpp用来调用pyinstaller生产的可执行文件。
我查到：在编写具有SUID/SGID权限的程序时请勿使用system()，system()会继承环境变量，通过环境变量可能会造成系统安全的问题。