import os
import shutil

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
	
               "Audio": [".aac", ".aa", ".aac", ".dvf",
                         ".m4a", ".m4b", ".m4p", ".mp3",
                         ".msv", "ogg", "oga", ".raw", 
                         ".vox", ".wav", ".wma"], 
              } 
# Function to create folders for each file format
def generate_folders():
    
    if not os.path.exists('data'):
        os.mkdir('data')
        if not os.path.exists('data/Web'):
            os.mkdir('data/Web')
        if not os.path.exists('data/Pictures'):
            os.mkdir('data/Pictures')
        if not os.path.exists('data/Videos'):
            os.mkdir('data/Videos')
        if not os.path.exists('data/Documents'):
            os.mkdir('data/Documents')
        if not os.path.exists('data/Compressed'):
            os.mkdir('data/Compressed')
        if not os.path.exists('data/Audio'):
            os.mkdir('data/Audio')
    
 # Function to organize files into their respective folders   
def file_organizer():
    for file in os.listdir():
        if os.path.isfile(file):
            for folder_name, file_format in fileFormat.items():
                for format in file_format:
                    if f'.{file.split('.')[-1]}' == format:
                        shutil.move(f'{os.getcwd()}/{file}', f'data/{folder_name}/{file}')
                        
                        

def main():
    generate_folders()
    file_organizer()
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
