# googleDriveFileDownload
Given public URL, this utility will download the file to the local disk.


Prerequisite : 
1. python version 3.5 or more.
2. Python libraries:
  i) gdown : - https://pypi.org/project/gdown/
 ii) requests: - https://pypi.org/project/requests/
iii) unittest: - https://pypi.org/project/unittest/

Usage:
1. Use below command to clone this repo.
    git clone https://github.com/AjayGupta-er/googleDriveFileDownload.git
2. Use below command line to invoke the script:
    python3.5 gDriveDownloader.py <URL> <fileName>
  
Here, <URL> is the public link of google drive file.
    Ex: 'https://drive.google.com/uc?id=19S-lycZy0Yz8WHbk8CwAjkaIBUKwmXHU'
    <fileName> is the file name you want to save the file as.
          
Also, you can import gDriveDownloader and create object of class DownloadGD.
Usage:
from gDriveDownloader import DownloadGD
    download = DownloadGD(<URL>)
    download.useGdown(<fileName>) OR download.useRequests(<fileName>)
  
  
  Please note:
  Class method 'useGdown' can be used to download larger size of files.
  
  Validation:
  
  To validate the gDriveDownloader, there is another unittest based tests: "testDownload.py"
  
  Usage:
  python3.5 testDownload.py
  
  This file has total 5 tests which validates the downloader.
  
 Also, there are few scenarios which could be validated manually for more rigorous tests:
 1. Test the downloader with different types of files, such as (tar files, image files, etc)
 2. Test the downloader with larger file size, such as (1GB, 10GB, etc)
 
