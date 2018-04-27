#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:26:20 2018

@author: lars
"""


import os
import csv

#read_dirs = ["/media/lars/LaCie/sort_fix/", #Should contain 1491
#             "/media/lars/LaCie/sort_fix_fault/", #Should contain 31
#             "/media/lars/LaCie/batch2/"] #Should contain 302

              
read_dirs = ["/media/lars/LaCie/copy_tos7_all_notbatch1/sorted/"]

output_file_name = "/home/lars/Desktop/output_python/ids_tos7_all_210318_sorted_299/sorted_299_ids.csv"

print_list = []

for i in read_dirs:
    
    current_ids = os.listdir(i)
    
    print_list = print_list + current_ids
    
    
#Storing data:
with open(output_file_name, "w") as output:
    writer = csv.writer(output, lineterminator="\n")
    for val in print_list:
        writer.writerow([val])


