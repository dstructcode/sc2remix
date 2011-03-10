import zipfile

from mpyq import MPQArchive

class SC2Remix(object):
    def __init__(self, replay):
        self.replay = replay
#        self.file = self._open(replay)
        self._get_mpq()
        self.archive = None

    def _get_mpq(self):
        try:
            self.mpq = MPQArchive(self.replay)
        except IOError:
            return None

    def _open(self, replay):
        try:
            self.file = open(replay, 'rb')
        except:
            print "Error opening replay."

    def zip(self, path=''):
        self.archive = zipfile.ZipFile(self.mpq.file.name+'.zip','w')
        files = self.mpq.extract()
        for f in self.mpq.files:
            self.archive.writestr(f, files[f])
        self.archive.close()
