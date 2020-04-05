'''This script will test the google drive downloader'''

import os
import unittest
from gDriveDownloader import DownloadGD

URL = 'https://drive.google.com/uc?id=19S-lycZy0Yz8WHbk8CwAjkaIBUKwmXHU'
OUTFILE = 'abc.csv'
FILESIZE = 114702936

class TestDownload(unittest.TestCase):

    def setUp(self):
        if os.path.exists(OUTFILE):
            os.system('rm '+OUTFILE)

    def test_useGdown(self):
        download = DownloadGD(URL)
        output = download.useGdown(OUTFILE)
        self.assertEqual(
            output,
            OUTFILE,
            'Downloaded file is: {out}'.format(out=output)
        )

    def test_useRequests(self):
        download = DownloadGD(URL)
        output = download.useRequests(OUTFILE)
        self.assertEqual(
            output,
            OUTFILE,
            'Downloaded file is: {out}'.format(out=output)
        )

    def test_invalidURL(self):
        invalidURL = "www://drive.google.com/uc?id=19S-lycZy0Yz8WHbk8CwAjkaIBUKwmXHU"
        download = DownloadGD(invalidURL)
        output = download.useGdown(OUTFILE)
        self.assertIsNone(output)

    def test_fileSizeRequests(self):
        download = DownloadGD(URL)
        output = download.useRequests(OUTFILE)
        if os.path.exists(OUTFILE):
            fSize = os.path.getsize(OUTFILE)
        self.assertEqual(
            fSize,
            FILESIZE,
            "Size of the file which downloaded using useRequests method is: {fSize}".format(fSize=fSize)
        )

    def test_fileSizeGdown(self):
        download = DownloadGD(URL)
        output = download.useGdown(OUTFILE)
        if os.path.exists(OUTFILE):
            fSize = os.path.getsize(OUTFILE)
        self.assertEqual(
            fSize,
            FILESIZE,
            "Size of the file which downloaded using useGdown method is: {fSize}".format(fSize=fSize)
        )

    def tearDown(self):
        if os.path.exists(OUTFILE):
            os.system('rm '+OUTFILE)

if __name__ == '__main__': 
    unittest.main()
