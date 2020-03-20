## logging system ##

import logging,checkFolder, time
import ini



def info(infolog):
    logpath = checkFolder.checkFolder(ini.logs())
    logging.basicConfig(filename=ini.logs()+'logs.out', level=logging.INFO)
    logging.info('{logtime} {log}'.format(logtime = time.strftime('%Y/%m/%d %H:%M'), log = infolog))





