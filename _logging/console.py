"""Template for logging to console"""

import logging


# ------- EDIT THIS -------
LOG_LEVEL = logging.DEBUG  # default debug
# default '%(asctime)s %(levelname)s %(message)s'
LOG_FORMAT = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# ------- END EDIT  -------


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(level=LOG_LEVEL)
CH = logging.StreamHandler()
CH.setLevel(LOG_LEVEL)
CH.setFormatter(LOG_FORMAT)
LOGGER.addHandler(CH)

LOGGER.debug("A quirky message only developers care about")
LOGGER.info("Curious users might want to know this")
LOGGER.warning("Something is wrong and any user should be informed")
LOGGER.error("Serious stuff, this is red for a reason")
LOGGER.critical("OH NO everything is on fire")
