'''
The purpose of this file is to prep raw text format
stepmania files into files ready for the main program to
actually use.
'''

import os

print("Rename the ssc file to the corresponding song name with the endfix being .txt")
target = folder_path = os.path.dirname(os.path.realpath(__file__)) + '\\songs\\' + input("Please enter the name of the txt file : ") + '.txt'
print(target)