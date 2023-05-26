import os
from tqdm import tqdm
import requests
import time


infopref = "[INFO] "
dlpref = "[INFO(DOWNLOAD)]: \n"
netlifymirror = "https://rootedcdn.rootqit.dev/"
gitmirror = "https://cdn.rootqit.dev/"
currentpath = os.getcwd()
mirrors = ["https://rootedcdn.rootqit.dev/", "https://cdn.rootqit.dev/"]




def downloadfromshittyapi(dlmirror, filename):
    confirmation = input("Do you really want to download? '" + filename + "'" + " y/N" + " @: ")

    if confirmation == "y": 
        print(infopref + "Loading vars...")
        mfile = dlmirror + filename
        response = requests.get(mfile, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        download_dir = os.path.join(currentpath, "downloads")
        os.makedirs(download_dir, exist_ok=True)
        destination = os.path.join(download_dir, filename)
        print(infopref + "Downloading now...")
        print(infopref + "[]")
        print(dlpref)

        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(destination, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()
        if total_size != 0 and progress_bar.n != total_size:
            print("An error occurred while downloading the file.")
        
    else: 
        print("Ok. Not downloading. Quitting now.")
        time.sleep(3)
        os.system("cls")
        exit()

def checkmirror(xmirror):
    try:
        response = requests.head(xmirror, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def cdnmirrorcheckingthingymajong():
    for mirror in mirrors:
        if checkmirror(mirror):
            print(f"The {mirror} mirror is currently available.")
        else:
            print(f"The {mirror} mirror is currently down.")
        time.sleep(1)

cdnmirrorcheckingthingymajong()
selmirror = input("Please choose a CDN mirror. 1 For Netlify and 2 for Github Pages. @: ")

if selmirror == "1":
    chosenmirror = netlifymirror

elif selmirror == "2":
    chosenmirror = gitmirror

else:
    print("Please select a valid mirror.")
    exit()


#Downloadlist: 
dl1 = "test.txt"
dl2 = "tests.txt"


os.system("cls")
print("""
        DownloadList:
        1. test.txt
        2. tests.txt
""")

primoption = input("Input download number. @: ")
if primoption == "1":
    downloadfromshittyapi(chosenmirror, dl1)
elif primoption == "2":
    downloadfromshittyapi(chosenmirror, dl2)
