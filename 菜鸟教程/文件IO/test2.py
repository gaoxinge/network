import os

os.mkdir('newdir')
os.rename('newdir','olddir')
os.rmdir('olddir')
print os.getcwd()
os.chdir('C:')
print os.getcwd()
