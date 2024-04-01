import logging

# https://www.logicmonitor.com/blog/python-logging-levels-explained
# Notset = 0: This is the initial default setting of a log when it is created.
#  It is not really relevant and most developers will not even take notice of
#  this category. In many circles, it has already become nonessential. The root
#  log is usually created with level WARNING.
# Debug = 10: This level gives detailed information, useful only when a problem
#  is being diagnosed.
# Info = 20: This is used to confirm that everything is working as it should.
# Warning = 30: This level indicates that something unexpected has happened or
#  some problem is about to happen in the near future.
# Error = 40: As it implies, an error has occurred. The software was unable to
#  perform some function.
# Critical = 50: A serious error has occurred. The program itself may shut down
#  or not be able to continue running properly

# https://gist.github.com/luminoso/b58199813f6763821f6e742a297a1a63
filename = 'logdetails.log'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(filename)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


def als():
    return logger


def ok(fehlermeldung):
    return logger.debug(fehlermeldung) 