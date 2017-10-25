#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:19:58 2017

Verify filter.py results:

@author: lars
"""

verify_dir = "/media/lars/LaCie/sorted_fix/"

output_dir = "/home/lars/Desktop/sort_filter_convert/filter/"
output_name = "verify_filter.txt"

verify_path = output_dir + output_name
verify_file = open(verify_path,"w")

import os

id_dir_list = os.listdir(verify_dir)

#Keywords for identifying desired subdirectories.
key_1 = "T1_3D_SAG"
key_2 = "T2_FLAIR_3D"
key_3 = "3D_TOF"
key_4 = "SWI_Images"


for i in id_dir_list:
    print("\n ID:")
    print(str(i))
    
    sub_dir = verify_dir + i + "/"
    modality_dir_list = os.listdir(sub_dir)
    
    key_1_matched = 0
    key_2_matched = 0
    key_3_matched = 0
    key_4_matched = 0
    
    #Iterate through the modalities.
    modal_iter = 0
    for j in modality_dir_list:
        
        #We do this to split the "random" number from the matching tag.
        
        if(j == key_1):
            key_1_matched = key_1_matched + 1
        
        if(j == key_2):
            key_2_matched = key_2_matched + 1
        
        if(j == key_3):
            key_3_matched = key_3_matched + 1
        
        if(j == key_4):
            key_4_matched = key_4_matched + 1
        
        modal_iter = modal_iter + 1
        #End modality iteration.
    
    #Write num of keys matched.
    write_string = i + "," + str(key_1_matched) + "," + str(key_2_matched) + "," + str(key_3_matched) + "," + str(key_4_matched) + "\n"
    print("String to write:")
    print(write_string)
    verify_file.write(write_string)
    
verify_file.close()