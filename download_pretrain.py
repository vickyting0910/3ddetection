import os
from google_drive_downloader import GoogleDriveDownloader as gdd

def main(file1, file2):
    if not os.path.isdir("./tools/objdet_models/"+file1+"/pretrained/"):
        os.mkdir("./tools/objdet_models/"+file1+"/pretrained/")

    if not os.path.isdir("./tools/objdet_models/"+file2.replace('fpn-','')+"/pretrained/"):
        os.mkdir("./tools/objdet_models/"+file2.replace('fpn-','')+"/pretrained/")

    

    gdd.download_file_from_google_drive(file_id='1Pqx7sShlqKSGmvshTYbNDcUEYyZwfn3A',
        dest_path="./tools/objdet_models/"+file1+"/pretrained_" + file1 + ".zip",
                                    unzip=True)
    
    gdd.download_file_from_google_drive(file_id='1RcEfUIF1pzDZco8PJkZ10OL-wLL2usEj',
        dest_path="./tools/objdet_models/"+file2.replace('fpn-','')+"/pretrained_" + file2 + ".zip",
                                    unzip=True)
if __name__ == "__main__":
    file1 = "darknet"
    file2 = "fpn-resnet"
    main(file1, file2)

