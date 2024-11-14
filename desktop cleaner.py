import os
import shutil

## select desired directory, will make it easier to get user input later
os.chdir('/Users/manuelp/desktop')
print(os.path.dirname)

## small function to create folder and check if said folder exist 
def createFolder(name):
    folder_path = os.path.join('/Users/manuelp/desktop', name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
   
    
## set main directory to desktop


##list of extentions of files
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"]
text_extensions = [".txt", ".md", ".rtf", ".doc", ".docx", ".odt", ".pdf", ".tex", ".wps", ".pptx"]

createFolder("images")
createFolder("docs")
createFolder("others")

p
for file in os.listdir():
    name, ext = os.path.splitext(file)  # Split the filename and its extension
    if os.path.isfile(file):  # Only process files, not directories
        if ext in image_extensions: ## check for extension and add the files to the folder 
            shutil.move(file, '/Users/manuelp/desktop/images')
        elif ext in text_extensions:
            shutil.move(file, '/Users/manuelp/desktop/docs')
        else:
            shutil.move(file, '/Users/manuelp/desktop/others')

print("Files organized successfully!")
        
        
            
            


