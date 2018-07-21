import os
import logging
import sys
from providers.open_subtitle_provider import OpenSubtitleProvider

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__file__)

provider = OpenSubtitleProvider()

VIDEO_EXTENSIONS = {'webm', 'mkv', 'flv', 'vob', 'ogv', 'avi', 'mp4'}


def get_subtitle_path(file_path):
    return '{}.srt'.format(file_path[:-4])


def is_video_file(path):
    return path[-3:].lower() in VIDEO_EXTENSIONS


def get_files(path):
    files = []
    for file in os.listdir(path):
        file_or_dir_path = os.path.join(path, file)
        if os.path.isdir(file_or_dir_path):
            files += get_files(file_or_dir_path)
        elif os.path.isfile(file_or_dir_path):
            if is_video_file(file_or_dir_path):
                files.append(file_or_dir_path)
    return files


def download_subtitles_for_files_in_directory(path):
    for file_path in get_files(path):
        try:
            subtitle_path = get_subtitle_path(file_path)
            if not os.path.isfile(subtitle_path):
                s_id = provider.search(file_path, 'es')
                logger.info("Downloading {}".format(subtitle_path))
                provider.download(s_id, subtitle_path)
            else:
                logger.info("No need to download subtitle for {}".format(file_path))
        except:
            logger.info("couldn't find subtitle for {}".format(path))

if __name__ == '__main__':
    download_subtitles_for_files_in_directory(sys.argv[1])
