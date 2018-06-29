#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:39:18 2018

@author: lars
"""

##Guidelines for file structure:
#https://cheba.unsw.edu.au/content/quick-start-manual

#To avoid the code unintentionally changing directories and similar,
# the UBO_X folders are required to construct manually as: target_dir/UBO_X.

#NIFTI ONLY

def ubo_copy_from_clean_to_workspace_manual_ids(source_list,source_dir,target_dir):
    
    #Prints
    print "Using the UBO workspace creation through copy NIFTI files."
    print "Source: ", source_dir, " Target: " ,target_dir, " Folder: T1 and T2"
    print "IDs to be copied: ", source_list
    
    #Constants - may be smart to glob these file paths if they vary... allowing both nii and nii.gz and deviating names.
    #Only 1 folder of each T1 and T2 i possible within an individual. Local convention as string.
    our_T1 = "/*T1_3D_SAG*/t1_3d_sag.nii*"
    our_T2 = "/*T2_FLAIR_3D*/t2_flair_3d.nii*"
    
    #UBO convention...
    UBO_T1 = "T1/"
    UBO_T2 = "FLAIR/"
    
    import shutil
    import glob
    
    id_list_dir = source_list
    
    n = len(id_list_dir)
    n_i = 1
    
    for i in id_list_dir: #Since glob is already used, this can definitely be simplified into the glob... This way ensures known "i"...
        print "---------------------------------------------------------------"
        print "Copying ID: ", i, " Number: ", n_i, " of ", n
        
        glob_T1_path = source_dir + i + our_T1
        globbed_T1_path = glob.glob(glob_T1_path) #Should only return 1 element in the list.
        
        T1_source_i_dir = globbed_T1_path[0]
        T1_target_i_dir = target_dir + UBO_T1 + i + "_T1.nii.gz"
        
        glob_T2_path = source_dir + i + our_T2
        globbed_T2_path = glob.glob(glob_T2_path) #Should only return 1 element in the list.
        
        T2_source_i_dir = globbed_T2_path[0]
        T2_target_i_dir = target_dir + UBO_T2 + i + "_T2.nii.gz"
        
        ##Copy T1
        print "Copying T1 file\n From: " + T1_source_i_dir + "\n To: " + T1_target_i_dir
        shutil.copyfile(T1_source_i_dir,T1_target_i_dir)
        ##Copy T2
        print "Copying T2 file\n From: " + T2_source_i_dir + "\n To: " + T2_target_i_dir
        shutil.copyfile(T2_source_i_dir,T2_target_i_dir)
        
        n_i = n_i + 1
        print("ID copied...")
        print "---------------------------------------------------------------"
    
    print("Finished...") #End of function...



#Test case:
copy_from = "/home/lars/Desktop/testing_dicomsort/test_folder_3_nifti/"
copy_to = "/home/lars/Desktop/testing_dicomsort/test_manual_copifyer/"
ids_list = ["100367"]

ubo_copy_from_clean_to_workspace_manual_ids(ids_list,copy_from,copy_to)





