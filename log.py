## logging system ##

import logging,checkFolder
import ini

    
def info(infolog):
    logpath = checkFolder.checkFolder(ini.logs())
    logging.basicConfig(filename=ini.logs()+'logs.out', level=logging.INFO)
    logging.info(infolog)



info('started')




