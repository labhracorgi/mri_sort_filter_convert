#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:19:57 2018

Script to extract age and gender from DICOM files.
Or other types of DICOM meta information.

This program, as is, presupposes DICOM-sorted data.

@author: lars
"""

import pydicom
import os
import glob
import csv

dicomsorted_dirs        = ["/home/lars/Desktop/testing_dicomsort/test_folder_3_dest_reruns/"] #Should be a list in case of multiple sorted directories.
csv_saving_directory    = "/home/lars/Desktop/testing_dicomsort/output_pydicomtest/"

n_ids = 0

for i in dicomsorted_dirs:
    #Loop over different dicomsorted directories
    print "*******************************************************************"
    current_dir_i = i
    print "Currently working in path: " + current_dir_i
    id_list = os.listdir(current_dir_i) #This could probably be omitted (due to glob), but provides a nice layer of specificity at this moment.
    
    for j in id_list:
        #Loop over different ID folders
        n_ids = n_ids + 1
        print "---------------------------------------------------------------"
        print "Current ID: " + str(j) + " as number: " + str(n_ids)
        
        globbing_static_path    = current_dir_i + j + "/"
        globbing_dynamic_path   = "*3D_TOF/1.dcm" #Can be changed with no problem as long, assuming the folders exist for a subject.
        globbing_path           = globbing_static_path + globbing_dynamic_path
        
        read_dicom_path = glob.glob(globbing_path) #Should ONLY return 1 path...
        read_dicom_path = read_dicom_path[0]
        
        print "Reading from dicom path: " + read_dicom_path
        
        #This reads in the DICOM object with "all" meta-info.
        this_dicom_object = pydicom.dcmread(read_dicom_path)
        
        #Extracting data: 
        # (If you want to add your own, the DCMDUMP command can help show what types of data the study specific DICOM files contain;
        #  do simply use the most righthand name.)
        ##Patient data
        patient_name    = this_dicom_object.PatientName
        patient_id      = this_dicom_object.PatientID
        patient_age     = this_dicom_object.PatientAge
        patient_sex     = this_dicom_object.PatientSex
        patient_dob     = this_dicom_object.PatientBirthDate
        
        ##Study data:
        patient_studytime = this_dicom_object.StudyTime
        patient_studydate = this_dicom_object.StudyDate
        
        ##Attempting coil data:
        patient_coil_used = this_dicom_object.TransmitCoilName
        #patient_coil_used = this_dicom_object.ReceiveCoilActiveElements
        #patient_coil_used = this_dicom_object.ReceiveCoilName ###Must be retrieved from json file post nifti convert?
        
        #Showing values extracted for logging purposes:
        print "Patient Name: " + patient_name
        print "Patiend ID: " + patient_id
        print "Patient Age: " + patient_age
        print "Patient Sex: " + patient_sex
        print "Patient DoB: " + patient_dob
        
        print "Study Time: " + patient_studytime
        print "Study Date: " + patient_studydate
        
        print "Coil Info: " + patient_coil_used
        #Writing to csv:
        list_of_interest = [j,
                            patient_id,
                            patient_age,
                            patient_sex,
                            patient_dob,
                            patient_studytime,
                            patient_studydate]
        
        output_file_name = csv_saving_directory + "dicom_metainfo.csv"
        with open(output_file_name, "a") as output:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerow(list_of_interest)    
            
        print "---------------------------------------------------------------"
        #End loop ID folders
    
    
    
    
    print "*******************************************************************"
    #End loop Dicomsort directories

print "A total of " + str(n_ids) + " subjects have had their values extracted."