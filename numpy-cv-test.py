import cv2
import numpy as np
import shutil
import random
import time
import os 
import glob
import struct

def test_all_py_packages(path,a,b):
    print("path ",path," a ",a," b ",b)
    print("in python function test_all_py_packages")  
    print("test cv2 and numpy first by random initializing a picture, crop and save it!")
    x = np.empty([224,224,1], dtype = int)
    x = np.clip(x,0,255)
    
    cv2.imwrite("random_picture1-224.png", x)
    x_crop=cv2.resize(x.astype('float32'),(100,100),interpolation=cv2.INTER_AREA)
    cv2.imwrite("random_picture2-100.png",x_crop)
    
    print("test time package\n")
    localtime = time.localtime(time.time())
    print("time:",localtime)

    print("test random package\n")
    print(random.random())

    print("test shutil and os package\n")
    print("Is random_picture1-224.png in PWD? ","random_picture1-224.png" in os.listdir(os.curdir))
    shutil.copy("random_picture1-224.png", "random_picture1-224-copy.png")
    print("Is random_picture1-224-copy.png in PWD? ","random_picture1-224-copy.png" in os.listdir(os.curdir))

    print("test glob package\n")
    file_list=glob.glob(r'../*.py')
    print("py file list in current dir!",file_list)

    print("test struct package\n")
    print("expected result: b'\x00\x9c@c'\n","test result: ",struct.pack('>I', 10240099))


test_all_py_packages("hahah",1,2)