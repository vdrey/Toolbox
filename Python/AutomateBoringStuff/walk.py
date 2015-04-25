import os

things = 0
for folderName, subfolders, filenames in os.walk('/'):
    print('The current folder is ' + folderName)
    things += 1
    for subfolder in subfolders:
        things += 1
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        things += 1
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

print(things)
