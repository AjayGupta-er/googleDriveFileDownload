'''This script will download a file from google drive.'''

import sys
import gdown
import requests

class DownloadGD:
    def __init__(self, url):
        self.url = url

    def useGdown(self, outFile):
        try:
            out = gdown.download(self.url, outFile, quiet=False)
            if out:
                return(out)
        except Exception as e:
            print("Exception Occurred: ",e)

    def useRequests(self, outFile):
        try:
            response = requests.get(self.url)
            request_code = response.status_code
            if request_code == 200:
                fetchedData = response.content
                with open(outFile, "wb") as raw_file:
                    raw_file.write(fetchedData)
                return(outFile)
        except Exception as e:
            print("Exception Occurred: ",e)


if __name__ == '__main__':
    url = sys.argv[1]
    outFile = sys.argv[2]
    downloadGoogle = DownloadGD(url)
    downloadGoogle.useGdown(outFile)
#    downloadGoogle.useRequests(outFile)
