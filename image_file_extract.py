#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import os.path
import re
import shutil
import subprocess

origin_path = os.path.abspath(os.curdir)


def my_copytree(src, dst, symlinks=False):  
    names = os.listdir(src)  
    if not os.path.isdir(dst):  
        os.makedirs(dst)  
          
    errors = []  
    for name in names:  
        srcname = os.path.join(src, name)  
        dstname = os.path.join(dst, name)  
        try:  
            if symlinks and os.path.islink(srcname):  
                linkto = os.readlink(srcname)  
                os.symlink(linkto, dstname)  
            elif os.path.isdir(srcname):  
                my_copytree(srcname, dstname, symlinks)  
            else:  
                if os.path.isdir(dstname):  
                    os.rmdir(dstname)  
                elif os.path.isfile(dstname):  
                    os.remove(dstname)  
                shutil.copy2(srcname, dstname)  
            # XXX What about devices, sockets etc.?  
        except (IOError, os.error) as why:  
            errors.append((srcname, dstname, str(why)))  
        # catch the Error from the recursive copytree so that we can  
        # continue with other files  
        except OSError as err:  
            errors.extend(err.args[0])  
    try:  
        shutil.copystat(src, dst)  
    except OSError as why:  
        errors.extend((src, dst, str(why)))  
    #if errors:  
    #    raise Error(errors) 


def mkdir(list):
	for item in list:
		if not os.path.exists(item):
			os.makedirs(item)

def change_path(file_name):
	for file in os.listdir(os.curdir):
		if re.match(file_name,file):
			os.chdir(file)
			print os.path.abspath(os.curdir)
			break

def extract_marshmallow(list):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	for item in list:
		change_path(item)
	#change_path(file_name_1)
	#change_path('images')
	#change_path('marshmallow')
	#change_path('(\w*)'+file_name_2+'(\w*)')
	for file in os.listdir(os.curdir):
		print file
		if os.path.isfile(os.path.abspath(file)):
			if re.match('system.img*',file):
				continue
			shutil.copy(os.path.abspath(file),abs_file_dst)
		if os.path.isdir(os.path.abspath(file)):
			my_copytree(os.path.abspath(file),os.path.join(abs_file_dst,file))
	os.chdir(origin_path)


def extract_system(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)MM')
	change_path('out')
	change_path('target')
	change_path('product')
	change_path('(\w*)'+file_name_2+'(\w*)')
	for file in os.listdir(os.curdir):
		if os.path.isdir(os.path.abspath(file)) and file == "system":
			my_copytree(os.path.abspath(file),os.path.join(abs_file_dst,file))
	os.chdir(origin_path)


def extract_linux_x86(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)MM')
	change_path('prebuilts')
	change_path('tools')
	change_path('linux-x86')
	for file in os.listdir(os.curdir):
		if os.path.isdir(os.path.abspath(file)) and file == "crc" or file == "secureboot":
			my_copytree(os.path.abspath(file),os.path.join(abs_file_dst,file))
	os.chdir(origin_path)

def extract_security(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)MM')
	change_path('device')
	change_path('(\w*)'+file_name_2+'(\w*)')
	change_path('(\w*)'+file_name_2+'(\w*)')
	change_path('security')
	for file in os.listdir(os.curdir):
		if os.path.isfile(os.path.abspath(file)) and file == "AESupgrade.bin" or file == "RSAimage_priv.txt" or file == "RSAimage_pub.txt":
			shutil.copy(os.path.abspath(file),abs_file_dst)
	os.chdir(origin_path)
			
def extract_tmp_image(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)Supernova')
	change_path('target')
	change_path('dvb.mainz')
	change_path('tmp_image')
	for file in os.listdir(os.curdir):
		if os.path.isdir(os.path.abspath(file)) and file == "tvconfig" or file == "tvdatabase":
			my_copytree(os.path.abspath(file),os.path.join(abs_file_dst,file))
	os.chdir(origin_path)

def extract_ext4(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(image_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)Supernova')
	change_path('target')
	change_path('dvb.mainz')
	change_path('images')
	change_path('ext4')
	for file in os.listdir(os.curdir):
		if os.path.isfile(os.path.abspath(file)) and file == "tvdatabase.img" or file == "tvconfig.img":
			continue
		shutil.copy(os.path.abspath(file),abs_file_dst)
	os.chdir(origin_path)

def extract_SN_scripts(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(SN_scripts_file_dst)
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)Supernova')
	change_path('target')
	change_path('tools')
	for file in os.listdir(os.curdir):
		if os.path.isfile(os.path.abspath(file)) and file == "make_ext4fs" or file == "file_contexts":
			shutil.copy(os.path.abspath(file),abs_file_dst)
	os.chdir(origin_path)

def extract_MM_scripts(file_name_1,file_name_2):
	abs_file_dst = os.path.abspath(MM_scripts_file_dst)
	abs_file_dst_2 = os.path.abspath(MM_lib_file_dst)
	print "111"+abs_file_dst_2
	print abs_file_dst
	change_path(file_name_1)
	change_path('(\w*)MM')
	change_path('out')
	change_path('host')
	change_path('linux-x86')
	change_path('bin')
	for file in os.listdir(os.curdir):
		if os.path.isfile(os.path.abspath(file)) and file == "make_ext4fs" or file == "lzop":
			shutil.copy(os.path.abspath(file),abs_file_dst)
	os.chdir("../lib64")
	print os.path.abspath(os.curdir)
	for file in os.listdir(os.curdir):
		if os.path.isfile(os.path.abspath(file)) and file == "libc++.so" or file == "libcutils.so" or file == "liblog.so" or file == "libselinux.so":
			print file
			shutil.copy(os.path.abspath(file),abs_file_dst_2)
	os.chdir(origin_path)


if __name__ == '__main__':
	import sys
	if len(sys.argv)<4 or sys.argv[1].startswith('-'):
		print "\033[1;35m Usage:./xxx.py [src_name] [project_name] [tv_system] [MM_device]\033[0m"
		print "\033[1;35m Ex:./xxx.py 348_DVB_xxx 348 DVB ktc\033[0m"
		print "\033[1;35m Tips:348_DVB_xxx为源码文件夹名 必须要包含MM和SN\033[0m"
		sys.exit(1)

	src_name = sys.argv[1]
	project_name = sys.argv[2]
	tv_system = sys.argv[3]
	device_name = sys.argv[4]
	
	file_name ="project_"+project_name+"_"+tv_system 
	image_file_dst = file_name +"/images_tst"
	SN_scripts_file_dst = file_name+"/my_scripts/SN_scripts"
	MM_scripts_file_dst = file_name+"/my_scripts/MM_scripts"
	MM_lib_file_dst = file_name+"/my_scripts/my_lib"
	
	make_dir_list = [image_file_dst,SN_scripts_file_dst,MM_scripts_file_dst,MM_lib_file_dst]
	mkdir(make_dir_list)
	
	marshmallow_path_list = [src_name,'images','marshmallow',device_name]
	extract_marshmallow(marshmallow_path_list)
	
	system_path_list = [src_name,'(\w*)MM','out','target','product',device_name]
	extract_system(src_name,device_name)
	extract_linux_x86(src_name,device_name)
	extract_security(src_name,device_name)
	extract_tmp_image(src_name,device_name)
	extract_SN_scripts(src_name,device_name)
	extract_MM_scripts(src_name,device_name)
