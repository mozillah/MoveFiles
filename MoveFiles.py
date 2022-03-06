import re
import os
import shutil
from glob import glob



# Path to labels Folder
labels_dir = r"D:\3. Maaz Data\labels"
# Path to Image folder
img_dir = r"D:\3. Maaz Data\img"
# Move Files to Specific Folder
movedFolder = r"D:\3. Maaz Data\movedFiles"

if not os.path.exists(movedFolder):
    os.makedirs(movedFolder)

print('img_dir = ' + img_dir)
print('labels_dir = ' + labels_dir)
print('Moved Files Directory = ' + movedFolder)


# Read Image and Label Files from the folder
labelFiles = [f for f in glob(f'{labels_dir}/**', recursive=True) if os.path.isfile(f)]
ImgFiles = [f for f in glob(f'{img_dir}/**', recursive=True) if os.path.isfile(f)]


# Compare the list of image  and  label Files
print(f" len of labelFiles {len(labelFiles)}")
print(f" len of ImgFiles {len(ImgFiles)}")



# Find matchedFiles from label to image so we can move the files to same folder
matchedFiles =[]
for label in  labelFiles:
    labelName = os.path.basename(label)
    print(label)
    name = labelName.split('.')[0]
    imgFile = [imgPath for imgPath in ImgFiles if re.search(name, imgPath)]
    if len(imgFile)>0:
        print(f"len of imgFile {len(imgFile)}")
        print(f"imgFiles {imgFile}")
        matchedFiles.append((label,imgFile[0]))


print("Copying Files from Image and Labels folder to  MovedFolder...")
# Move or Copy the file to MovedFolder
for (label,img) in matchedFiles:
    if os.path.exists(label) and os.path.exists(img):
        movedLabel=os.path.join(movedFolder,os.path.basename(label))
        movedImg=os.path.join(movedFolder,os.path.basename(img))
        shutil.copy(label, movedLabel)
        shutil.copy(img, movedImg)
        print(f"moving Image from {img} to {movedImg}")
        print(f"moving Label from {label} to {movedLabel}")

print("Moving Files Completed")
