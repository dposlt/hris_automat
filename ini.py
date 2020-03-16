## read ini file ##

from configparser import ConfigParser

parser = ConfigParser()
parser.read('settings.ini')
#print(parser.sections())



def zipFile():
    zipFile = parser.get('zipfile','path')
    return zipFile

def deploy():
    deploy = parser.get('deploy','path')
    return deploy

def target():
    target = parser.get('target','path')
    return target



