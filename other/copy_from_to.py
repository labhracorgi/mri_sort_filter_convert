#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:21:26 2017

Copy files from source_dir into target_dir while upholding the higher level structure.

#source_dir: Location of the files to be copied.
#target_dir: Location of where the files should be copied to.
#sub_dir: Name of the sub-folder ("under ID") containing the files desired.

@author: lars
"""

def copy_from_to(source_dir,target_dir,sub_dir):
    
    print "Source: ",source_dir, " Target: " ,target_dir, " Folder: " ,sub_dir
    
    import os
    import shutil
    
    id_list_dir = os.listdir(source_dir)
    
    n = len(id_list_dir)
    n_i = 1
    
    for i in id_list_dir:
        print "Copying ID: ", i, " Number: ", n_i, " of ", n
        
        source_i_dir = source_dir + i + sub_dir
        target_i_dir = target_dir + i + sub_dir
        shutil.copytree(source_i_dir,target_i_dir)
        
        n_i = n_i + 1
        print("ID copied...")
    
    print("Finished...")



#Test:
#s_dir = "/home/lars/Desktop/Test/copy_test/source/"
#t_dir = "/home/lars/Desktop/Test/copy_test/target/"
#f_name = "/T1_3D_SAG/"
    
#copy_from_to(s_dir,t_dir,f_name)

#s_dir = "/home/lars/Desktop/Test/copy_test/source/"
#t_dir = "/home/lars/Desktop/Test/copy_test/target/"
#f_name = "/3D_TOF/"
    
#copy_from_to(s_dir,t_dir,f_name)



#Actual call:
#s_a_dir = "/media/lars/LaCie/sorted_nifti/"
#t_a_dir = "/media/lars/LaCie/working_tof_t1/"
#f_a_name = "/T1_3D_SAG/"

#copy_from_to(s_a_dir,t_a_dir,f_a_name)

#s_a_dir = "/media/lars/LaCie/sorted_nifti/"
#t_a_dir = "/media/lars/LaCie/working_tof_t1/"
#f_a_name = "/3D_TOF/"

#copy_from_to(s_a_dir,t_a_dir,f_a_name)

