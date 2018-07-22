from subtitle_provider import SubtitleProvider
from utils.pythonopensubtitles.opensubtitles import OpenSubtitles
from utils.pythonopensubtitles.utils import File

ost = OpenSubtitles()
ost.login('fede.rulli@hotmail.com', 'rehlinger')


class OpenSubtitleProvider(SubtitleProvider):

    def search(self, file_path, language):
        file_obj = File(file_path)
        data = ost.search_subtitles(
            [{'sublanguageid': 'es',
              'moviehash': file_obj.get_hash(),
              'moviebytesize': file_obj.size}])
        return next(x for x in data if x['ISO639'] == language)['IDSubtitleFile']

    def download(self, subtitle_id, output_path):
        ost.download_subtitles([subtitle_id], None, output_path)
