# FIRST PROJECT WITH PYTHON
import os, shutil

# NOTE : You can write every single extensions inside tuples
dict_extension = {
    'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
    'video_extension' : ('.mp4', '.mkv', '.flv', '.mpeg'),
    'documents_extersion' : ('.doc','.pdf','.txt'),
}

folderpath = input('enter folder path : ')

def file_finder(folder_path, file_extension):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extensions in file_extension:
    #         if file.endswith(extensions):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extensions in file_extension  if file.endswith(extensions)]

# print(file_finder(folderpath, video_extension))  
for extensions_type, extensions_tuple in dict_extension.items():
    # print('calling file finder')
    # print(file_finder(folderpath, extensions_tuple))
    folder_name = extensions_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extensions_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)
      
  