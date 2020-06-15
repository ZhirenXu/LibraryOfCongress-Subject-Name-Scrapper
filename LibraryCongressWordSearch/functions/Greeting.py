import sys

## print program info
def showInfo():
    print("****************************************************")
    print("*  LibraryOfCongress Subject/Name Scrapper v1.0.0  *")
    print("*              Author: Zhiren Xu                   *")
    print("*      Use and Modify Code from @ruthtillman       *")
    print("*            published data: 6/15/20               *")
    print("****************************************************")
    print("Check this repo to see Ruth's work: https://github.com/ruthtillman/subjectreconscripts")
    
## print exit message
# @param    fileOut
#           name of output file
def sysExit(fileOut):
    print("\nThe program is finished. The output file is: ", fileOut, " \n. It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
