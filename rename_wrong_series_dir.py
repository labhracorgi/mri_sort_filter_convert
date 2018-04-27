#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 18:23:37 2018

@author: lars
"""

id_dir = "/media/lars/LaCie/copy_tos7_all_notbatch1/copy_maybe_fault_curated"

import os

id_list = os.listdir(id_dir)

n = 1
for i in id_list:
    print "Current ID: " + i + " Number: " + str(n)
    n = n + 1
    
    current_id_path = id_dir + "/" + i 
    
    series_list = os.listdir(current_id_path)
    
    for j in series_list:
        print "Series: " + j
        
        current_serie_path = current_id_path + "/" + j
        
        mod_current_serie_path = current_serie_path[:-2] 
        print "Rename from: " + current_serie_path + " To: " + mod_current_serie_path
        #This assumes that we only have _1 to _9 in our data. Which should be the case...
        
        ##Renaming:
        os.rename(current_serie_path,mod_current_serie_path)
        
        #End Series loop.
    
    
    
    #End ID loop.

