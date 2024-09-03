import os

# folder = 'File Path of the files'
# scan = os.scandir(folder)
org = '//file/path1'
dst = '//file/path2'

locate_org = os.path.join(org, 'cisco-ios7850.txt')
locate_dst = os.path.join(dst, 'cisco-ios3850.txt')

os.rename(locate_org, locate_dst)
renamed_file = os.path.join(locate_dst, 'new.txt')
print(renamed_file)
 