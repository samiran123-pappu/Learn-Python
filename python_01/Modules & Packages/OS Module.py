import os
import json
#  1. Get current working directory
cwd = os.getcwd()
print("Current Directory:", cwd)

#  2. Create a new folder named 'new_folder'
if not os.path.exists("new_folder"):  # check first to avoid errors
    os.mkdir("new_folder")
    print("Folder 'new_folder' created!")
else:
    print("Folder 'new_folder' already exists!")

#  3. List all files and folders in current directory
files = os.listdir(".")
print("Files and Folders:", files)
with open("data1.json", "w") as f:
    json.dump(files, f)
#  4. Create a sample file to rename
with open("old.txt", "w") as f:
    f.write("This is a sample file.")
print("File 'old.txt' created!")

# #  5. Rename 'old.txt' to 'new.txt'
if os.path.exists("old.txt"):
    os.rename("old.txt", "new.txt")
    print("File renamed from 'old.txt' to 'new.txt'")
else:
    print("'old.txt' does not exist!")

# #  6. Remove the renamed file
if os.path.exists("new.txt"):
    os.remove("new.txt")
    print("File 'new.txt' removed!")
else:
    print("'new.txt' does not exist!")

# #  7. List again to confirm changes
files_after = os.listdir(".")
print("After deletion:", files_after)
#  8. Remove the folder we created
if os.path.exists("new_folder"):
    os.rmdir("new_folder")
    print("Folder 'new_folder' removed!")
else:
    print("'new_folder' does not exist!")



