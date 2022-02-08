### CONCEPT FOR TEMPLATE DIRECTORY ####
## Specific to new Django release


from pathlib import Path
print(__file__) # Name of the current file
print(Path(__file__).resolve()) # Complete path of the file
print(Path(__file__).resolve().parent) #1 directory up
print(Path(__file__).resolve().parent.parent) # another directory up
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR / 'templates')

## Templates folder created at project level and then app level folders
# in views.py, render(request,'testapp/Welcome.html') as, till templates, path already defined in settings
