class UrsService(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def connect(self):
        if self.key == 'foo':
            raise ValueError('yo dog!')
        return True

    def get_redirect(self, url):
        return 'http://' + url
