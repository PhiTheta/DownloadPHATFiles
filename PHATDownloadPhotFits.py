#By Kiran Tikare 2019/06/20
# Python 3.7 (Anaconda)
#Downloads photometry files from PHAT website

import logging
from PHATDownloadFunc import downloadPHATPhotFiles
#setup the logging
logging.basicConfig(filename='executionLog.log',level=logging.DEBUG)
#Path to home directory
download_folder_path = '/home/okc/Kiran-Thesis/'
#loop through the brick numbers and create folder for each brick and download photometry files into them
for x in range(1, 23):
    if (x <= 9):
        brickNo = '0'+str(x)
    else:
        brickNo = str(x)

    page_link = 'https://archive.stsci.edu/pub/hlsp/phat/brick'+brickNo+'/'

    # Direct Link just incase you want to download only specific brick files
    # page_link = 'https://archive.stsci.edu/pub/hlsp/phat/brick23/'

    downloadPHATPhotFiles(brickNo, page_link, download_folder_path)

