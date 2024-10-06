import os
import shutil

from numpy.lib.utils import source

source_dir = '/Users/anuraggupta'
#os.mkdir('/Users/anuraggupta/Desktop/All_Mac_Images')
#print('Directory Created')
target_dir = 'All_Mac_Images'
file_type = '.csv'

#List down all the Image files in the source directory
#Working

def list_file_names(source_dir):
    for filename in os.listdir(source_dir):
      if os.path.isfile(os.path.join(source_dir, filename)):
          if filename.endswith(file_type):
            print(filename)


list_file_names(source_dir)