# PROJECT 2 - File separator using OS Module.

import os , shutil

dict_extension={
    "audio_ext": (".m4a",".flac",".mp3",".mp4",".wav",".wma",".aac"),
    "video_ext": (".mov", ".wmv", ".flv", ".mp4", ".avi", ".avchd", ".mkv",".mpeg"),
    "doc_ext"  : (".doc", ".pdf", ".txt",".jpj",".docx",".3gp",".pdf")
}

foldpath=input("enter the path :")

def file_finder(fldpath,file_extension):

    lst=[[],[]]

    for file in os.listdir(fldpath):
        for ext in file_extension:
            if file.endswith(ext):
                lst[0].append(file)
            else:
                lst[1].append("no")
    return lst

for ext_type , ext_tuple in dict_extension.items():

    foldname=ext_type.split("_")[0]
    fold_path=os.path.join(foldpath,foldname)

    if file_finder(foldpath,ext_tuple)[0]!=[]:
        print(f"Folder named '{foldname}' is formed.")
        os.mkdir(fold_path)
        for item in file_finder(foldpath,ext_tuple)[0]:
               itempath=os.path.join(foldpath,item)
               shutil.move(itempath,fold_path)

    elif os.path.exists(fold_path):
        print(f"Folder named '{foldname}' already exist.")

    else:
        print(f"There is no '{foldname} file' in the folder.")
