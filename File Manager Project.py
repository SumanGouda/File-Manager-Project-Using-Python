import os
import shutil

source_file = "D:\PROJECTS\LOGO\snackBOT"

for file in os.listdir(source_file):
    # Makes a list of all the file in the folder.
    
    file_path = os.path.join(source_file, file)
    #Makes a path to the file.
    
    if os.path.isdir(file_path):
        continue    
        #It skips any folder inside the main folder as we want to deal with files or arrenge files according to there type.
        
    _, ext = os.path.splitext(file)
    ext = ext[1:]
    #It extracts the extension name name remove the dot, like ---> .jpg --> jpg
    
    new_folder = os.path.join(source_file, ext)
    #Add the file to the respective category type file. Like a .png file to png folder which was already inside the main folder.
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        #Creates a file with the extension name(Excluding dot) if is not exist there before.
        
    shutil.move(file_path, os.path.join(new_folder, file))
    #Moves the file. (src, dst)