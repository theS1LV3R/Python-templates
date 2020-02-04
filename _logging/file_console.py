"""Template for logging to a file and console"""

import logging


# ------- EDIT THIS -------
LOG_FILENAME = 'example.log'  # default example.log
LOG_LEVEL_CONSOLE = logging.DEBUG  # default logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG  # default logging.DEBUG
# default '%(asctime)s %(levelname)s %(message)s'
LOG_FORMAT_CONSOLE = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
LOG_FORMAT_FILE = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# ------- END EDIT  -------


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(level=LOG_LEVEL_CONSOLE)
FH = logging.FileHandler(LOG_FILENAME)
FH.setLevel(LOG_LEVEL_FILE)
FH.setFormatter(LOG_FORMAT_FILE)
CH = logging.StreamHandler()
CH.setLevel(LOG_LEVEL_CONSOLE)
CH.setFormatter(LOG_FORMAT_CONSOLE)
LOGGER.addHandler(FH)
LOGGER.addHandler(CH)

LOGGER.debug("A quirky message only developers care about")
LOGGER.info("Curious users might want to know this")
LOGGER.warning("Something is wrong and any user should be informed")
LOGGER.error("Serious stuff, this is red for a reason")
LOGGER.critical("OH NO everything is on fire")
