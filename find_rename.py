import os
import glob
for name in glob.glob('/root/shri/distribution/folds/*'):
   if os.path.isdir(name):
         for i in glob.glob('{}/*'.format(name)):
              new_name = os.path.split(i)[1].split('-')[0] + '.latest.ear'
              #print(i)
              #print(new_name)
              #print(os.path.split(i)[0])
              os.rename(i, '{}/{}'.format(os.path.split(i)[0], new_name))
