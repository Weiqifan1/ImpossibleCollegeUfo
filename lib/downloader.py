
# download the file and change it to a panda dataset


import requests
import os.path
import sys

def downloader(URL, file_name):
    """Download file from URL and save to file_name if not already present. If present, do nothing."""

    if not os.path.isfile(file_name):

        try:
            print("Downloading file...")
            response = requests.get(URL)
            as_string = response.text

            with open(file_name, 'w', encoding='utf8', newline='') as the_file:
                the_file.write(as_string)
        except Exception as e:
            print("Error downloading file; ", e)
            sys.exit(1)
        print("File downloaded.")


# old downloader
'''
import os
import sys
from urllib import request as req


def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)


def download_file():
    try:
        global file_name
        _, url, file_name = sys.argv
    except:
        try:
            _, url = sys.argv
            file_name = os.path.basename(url)
        except:

            try:

                # open file
                cfg_file = file_name
                with open(cfg_file) as fp:
                    for line in fp:

                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)
            except Exception as e:
                print(__doc__)
                sys.exit(1)

    download(url, file_name)
    return file_name
'''