#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:32:43 2022

@author: sharonputhuparambil
"""

# Python program to change the name of the student's exercise sheet and remove all unnecessary folders
# TO DO: change the name of the folder, what to do if submission is not in pdf but jpeg
  
import os
import json
import glob
import shutil


directory = input("directory: ")
main = directory

for path in os.listdir(directory):
    if path[0] == "2":
        path = main+"/"+path
        os.chdir(path)
        
        json_file = open('.student-info.json')
        data = json.load(json_file)
    
        # exercise_sheet_number_str = data["serie"]
        # exercise_sheet_number_str_modified = exercise_sheet_number_str[1:]
        # exercise_sheet_number = int(exercise_sheet_number_str_modified)
        # data["serie"] gives as output something like "s05"
        exercise_sheet_number = int(data["serie"][1:])
        
        surname = data["lastname"]
        new_name = "Analysis_S"+str(exercise_sheet_number)+"_"+surname+".pdf"
        
        for file in glob.glob("*.pdf"):
            os.rename(file, new_name)
        json_file.close()
        shutil.move(path +'/'+ new_name, directory)

os.chdir(directory)

for path in os.listdir(directory):
    if path[0] == "2":
        shutil.rmtree(directory + '/' +path)

print("Name changed successfully.")


        
# TODO: change name of folder
# os.rename(directory, "ciao")

  
