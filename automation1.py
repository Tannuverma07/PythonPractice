import os

folder_path = "C:\\Users\\Subhi\\OneDrive\\Desktop\\TestFolder"
es = os.listdir(folder_path)

for index, file in enumerate(es):
    new_name = f"suga{index+1}.txt"
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Files renamed succesfully!")