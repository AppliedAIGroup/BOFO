#####################
# 使用leancloud上传并下载文件
# 主要功能：
# init_leancloud(leancloudID, leancloudAPP)
# uploadImageByPath(folderpath=str, filename=str) 上传文件并返回文件的ID
# downloadByID(ID=str, folderpath=str): 根据ID下载文件到filderpath
######################


import leancloud
import logging
from urllib import request

# --------------configuration --------------#

# leancloud
leancloud_APPID = 'hHcG1lVaaroON4QtEi1seRxb-gzGzoHsz'
leancloud_APPKey = 'SbR79lNTiRSM8bAm5D7JuD3E'
imageID = '59a76bfd44d90400582e628d'
folderpath = '/Users/zhizhao/PycharmProjects/BOFO/TestVersion/image'  #图片保存位置


# ------------init ------------#
def init_leancloud(leancloudID, leancloudAPP):
    leancloud.init(app_id=leancloud_APPID, app_key=leancloud_APPKey)
    logging.basicConfig(level=logging.DEBUG)


def uploadImageByPath(folderpath=str, filename=str):
    tempfilepath = folderpath + '/' + filename
    with open(tempfilepath, 'r+b') as f:
        avatar = leancloud.File(filename, f)
        avatar.save()
        object_id = avatar.id
        return object_id


# getImageID
def getUrlByID(ID=str):
    avatar = leancloud.File.create_without_data(ID)
    avatar.fetch()
    url = avatar.url
    return url


def getNameByID(ID=str):
    avatar = leancloud.File.create_without_data(ID)
    avatar.fetch()
    name = avatar.name
    return name


# download#
def downloadByID(ID=str, folderpath=str):
    url = getUrlByID(ID)
    filename = getNameByID(ID)
    print("start download img " + url)
    try:

        # fileName = gGetFileName(url)
        # print("start download img name is" + fileName)
        if url == None: print("url error")
        if url == "": print("url error")
        tempfilepath = folderpath + '/' + filename
        request.urlretrieve(url, tempfilepath)  # '/Users/zhizhao/Desktop/test/test.jpg'
        print("download img success" + url)
    except IOError:
        print("download img failed:" + url)


# --------------main loop ------------#
if __name__ == '__main__':
    init_leancloud(leancloud_APPID, leancloud_APPKey)
    downloadByID(imageID, folderpath)



