
## checking existing folder ##

import ini, os


def checkFolder(folderName):
    if os.path.isdir(folderName):

        return True
    else:

        os.mkdir(folderName)


checkFolder(ini.zipFile())
        



