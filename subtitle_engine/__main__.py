import logging
import sys
from settings import DIRECTORIES
from subtitle_engine import download_subtitles_for_files_in_directory


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logger = logging.getLogger(__file__)
    for directory in DIRECTORIES:
        logger.info("Searching subtitles for videos in {}".format(directory))
        download_subtitles_for_files_in_directory(directory, logger)
