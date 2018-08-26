import os
import glob
for name in glob.glob('/root/shri/distribution/*'):
   if os.path.isdir(name):
         for i in glob.glob('{}/*'.format(name)):
              print(i)
              print("-----------------")
