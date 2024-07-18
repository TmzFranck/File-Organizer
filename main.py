import os
import shutil
import time

fileFormat = {
	           "Web": [".html5", ".html", ".htm", ".xhtml"], 
	
               "Pictures": [".jpeg", ".jpg", ".tiff", ".gif",
                           ".bmp", ".png", ".bpg", "svg",".heif", ".psd"], 
	
               "Videos": [".avi", ".mkv",".flv", ".wmv",
                         ".mov", ".mp4", ".webm", ".vob", 
                         ".mng",".qt", ".mpg", ".mpeg", ".3gp"], 
	
              "Documents": [".oxps", ".epub", ".pages", ".docx",
                           ".txt", ".pdf", ".doc", ".fdf",
                           ".ods",".odt", ".pwi", ".xsn",
                           ".xps", ".dotx", ".docm", ".dox",
                           ".rvg", ".rtf", ".rtfd", ".wpd", 
                           ".xls", ".xlsx", ".ppt","pptx"], 
	
               "Compressed": [".a", ".ar", ".cpio", ".iso", 
                              ".tar", ".gz", ".rz", ".7z",
                              ".dmg", ".rar", ".xar", ".zip"], 
	
               "Audios": [".aac", ".aa", ".aac", ".dvf",
                         ".m4a", ".m4b", ".m4p", ".mp3",
                         ".msv", "ogg", "oga", ".raw", 
                         ".vox", ".wav", ".wma"], 
              } 
# Function to create folders for each file format
def generate_folders():
    
    if not os.path.exists('data'):
        os.mkdir('data')
        os.mkdir('data/Web')
        os.mkdir('data/Pictures')
        os.mkdir('data/Videos')
        os.mkdir('data/Documents')
        os.mkdir('data/Compressed')
        os.mkdir('data/Audios')
        print("Folders created successfully")
    else:
        print("Folders already exist")
        folder_name = input('give a new name to the folder: ')
        os.mkdir(folder_name)
        os.mkdir(f'{folder_name}/Web')
        os.mkdir(f'{folder_name}/Pictures')
        os.mkdir(f'{folder_name}/Videos')
        os.mkdir(f'{folder_name}/Documents')
        os.mkdir(f'{folder_name}/Compressed')
        os.mkdir(f'{folder_name}/Audios')
        print("Folders created successfully")
        
    
 # Function to organize files into their respective folders   
def file_organizer():
    for file in os.listdir():
        if os.path.isfile(file):
            for folder_name, file_format in fileFormat.items():
                for format in file_format:
                    if f'.{file.split('.')[-1]}' == format:
                        shutil.move(f'{os.getcwd()}/{file}', f'data/{folder_name}/{file}')
                        print(f"Moved {file} to {folder_name} folder")
                        time.sleep(0.5)
                        
                        

def main():
    print("Organizing files...")
    generate_folders()
    file_organizer()
    print("All files have been organized successfully")
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
