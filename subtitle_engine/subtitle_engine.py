import os
from providers.open_subtitle_provider import OpenSubtitleProvider
from settings import VIDEO_EXTENSIONS

provider = OpenSubtitleProvider()


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


def download_subtitles_for_files_in_directory(path, logger):
    for file_path in get_files(path):
        try:
            subtitle_path = get_subtitle_path(file_path)
            if not os.path.isfile(subtitle_path):
                s_id = provider.search(file_path, 'es')
                logger.info("Downloading {}".format(subtitle_path))
                provider.download(s_id, subtitle_path)
            else:
                logger.info("No need to download subtitle for {}".format(file_path))
        except Exception as e:
            logger.info('ERROR: {}'.format(str(e)))
