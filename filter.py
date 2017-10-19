# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:41:49 2017

After: Dicom_sort.py

Do _self: Isolate, rename and delete superficial files.

Then: Convert DCM2NII (?)

@author: lars
"""

#Base directory or input directory of the sorted files.
sorted_dir = "/home/lars/Convert/dicom_sort_copy/"

#We want to have a file where we can write possible errors!
troubleshoot_dir = "/home/lars/Convert/"
troubleshoot_name = "urgent_please_check.txt"

trouble_path = troubleshoot_dir + troubleshoot_name
trouble_file = open(trouble_path,"w")

#Retrieve IDs.
import os
import shutil
id_dir_list = os.listdir(sorted_dir)

#Keywords for identifying desired subdirectories.
key_1 = "T1_3D_SAG"
key_2 = "T2_FLAIR_3D"
key_3 = "3D_TOF"
key_4 = "SWI_Images"

#Iterate through the IDs.
for i in id_dir_list:
    
    sub_dir = sorted_dir + i + "/"
    modality_dir_list = os.listdir(sub_dir)
    
    key_1_matched = 0
    key_2_matched = 0
    key_3_matched = 0
    key_4_matched = 0
    
    #By default every modality-directory should not be renamed.
    rename_index = [0]*len(modality_dir_list)
    
    #Iterate through the modalities.
    modal_iter = 0
    for j in modality_dir_list:
        
        #We do this to split the "random" number from the matching tag.
        split_dir_name = j.split('-')
        
        if(split_dir_name[1] == key_1):
            key_1_matched = key_1_matched + 1
            rename_index[modal_iter] = 1
        
        if(split_dir_name[1] == key_2):
            key_2_matched = key_2_matched + 1
            rename_index[modal_iter] = 2
        
        if(split_dir_name[1] == key_3):
            key_3_matched = key_3_matched + 1
            rename_index[modal_iter] = 3
        
        if(split_dir_name[1] == key_4):
            key_4_matched = key_4_matched + 1
            rename_index[modal_iter] = 4
        
        modal_iter = modal_iter + 1
        #End modality iteration.
    
    #Write to trouble file if more than 4 keys have been successfully matched.
    #As these files have to be inspected more closely.
    similar_directories_flag = False    
    sum_keys = key_1_matched + key_2_matched + key_3_matched + key_4_matched
    
    if(sum_keys > 4):
        text_to_trouble = i + "," + str(sum_keys) + "\n"
        trouble_file.write(text_to_trouble)
        similar_directories_flag = True
    
    #Iterate through rename_index to change names
    modal_iter = 0
    rename_count = 0
    for k in rename_index:
        
        if(k>0 & similar_directories_flag == False):
            if(k == 1):
                old_name = modality_dir_list[modal_iter]
                new_name = key_1
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                
            if(k == 2):
                old_name = modality_dir_list[modal_iter]
                new_name = key_2
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                
            if(k == 3):
                old_name = modality_dir_list[modal_iter]
                new_name = key_3
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                
            if(k == 4):
                old_name = modality_dir_list[modal_iter]
                new_name = key_4
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
        
        if(k>0 & similar_directories_flag == True):
            if(k == 1):
                old_name = modality_dir_list[modal_iter]
                new_name = key_1 + "_" + str(rename_count)
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                rename_count = rename_count + 1
                
            if(k == 2):
                old_name = modality_dir_list[modal_iter]
                new_name = key_2 + "_" + str(rename_count)
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                rename_count = rename_count + 1
                
            if(k == 3):
                old_name = modality_dir_list[modal_iter]
                new_name = key_3 + "_" + str(rename_count)
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                rename_count = rename_count + 1
                
            if(k == 4):
                old_name = modality_dir_list[modal_iter]
                new_name = key_4 + "_" + str(rename_count)
                old_path = sub_dir + old_name + "/"
                new_path = sub_dir + new_name + "/"
                
                os.rename(old_path,new_path)
                rename_count = rename_count + 1
                
        modal_iter = modal_iter + 1        
        #End rename_index iteration.
    
    #Iterate through rename_index to remove dirs that haven't changed name.
    modal_iter = 0    
    for l in rename_index:
        if(l == 0):
            this_name = modality_dir_list[modal_iter]
            this_path = sub_dir + this_name + "/"
            
            shutil.rmtree(this_path)
        
        modal_iter = modal_iter + 1
        #End rename_index iteration.
    
    #End ID iteration.


#End the script by closing the trouble_file
trouble_file.close()
