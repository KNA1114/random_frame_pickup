import cv2
import pathlib
import os
import sys
import randomPickupper
import shutil

save_path = './pickedImages'

files = list(pathlib.Path(save_path).glob('*.jpg'))
idx = 0

filename = ''

collect_files = []

while idx < len(files):
    filename = save_path + '/' + files[idx].name
    img = cv2.imread(filename)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k == ord('l'):
        if idx < len(files):
            idx += 1

        collect_files.append(filename)
        print(collect_files)
    elif k == ord('h'):
        if idx > 0:
            idx -= 1

        if len(collect_files) > 0:
            filename = collect_files.pop()
        else:
            print("list is empty")

        print(collect_files)
    elif k == ord('d'):
        idx += 1
        print(collect_files)

    if len(collect_files) > 200:
        break

    print(len(collect_files))


for i in collect_files:
    shutil.copyfile(i, './pickedImages/collectImageFix/' + i[15:])
