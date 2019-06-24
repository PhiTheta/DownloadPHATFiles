#By Kiran Tikare 2019/06/19
# Python 3.7 (Anaconda)
#Contains methods for downloading photometry files from PHAT website

from bs4 import BeautifulSoup
import requests
import os
import logging
import re


def downloadPHATPhotFiles(brickNo, page_link, download_folder_path):
    '''int,string,string -> log file'''
    brickFolderName = 'brick' + str(brickNo)
    os.chdir(download_folder_path)
    os.mkdir(brickFolderName, mode=0o777)  # 0o777 is a octal number
    os.chdir(download_folder_path + brickFolderName)

    # here, we fetch the content from the url, using the requests library
    page_response = requests.get(page_link, timeout=5)

    # we use the html parser to parse the url content and store it in a variable.
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # gather all the links related to V2 Photometry files which have extension *_v2_phot.fits.gz
    links = [a['href'] for a in page_content.find_all('a', href=re.compile('http.*\.gz'))]

    # print(links)
    # -N option enables time-stamping, which re-downloads the file only if its newer on the server than the downloaded version.
    for dwnlink in links:
        grabThis = "wget -N "
        downloadLink = grabThis + dwnlink

        try:
            resultLog = os.system(downloadLink)
            if 0 == resultLog:
                logging.info("file download complete", resultLog)
            else:
                logging.error("files were not downloaded; result code: %d" % resultLog)
        except:
            logging.error("files were not downloaded")
        else:
            logging.info("file download complete")

