#include<stdlib.h>
#include<iostream>
#include <csignal>
// #include<cstring> //strerror
int main() 
{ 
    //reference from https://linux.die.net/man/3/system
    int ret = system("./dist/numpy-cv-test"); 
    if (WIFSIGNALED(ret) && (WTERMSIG(ret) == SIGINT || WTERMSIG(ret) == SIGQUIT))
        std::cout<<"error occured!"<<std::endl;
    return 0;
}