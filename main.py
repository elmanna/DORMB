from pathlib import Path
from settings.settings import setupConfigurations
from django.core.management import execute_from_command_line


BASE_DIR = Path(__file__).resolve().parent

def main():
    #run script or any other subprocess code here
    pass

def setup():
    
    setupConfigurations()
    execute_from_command_line() # """ uncomment this line to 
    # to use the django command line (i.e manipulate DB & so on...) from within terminal"""
    main()

if __name__ == "__main__":
    setup()