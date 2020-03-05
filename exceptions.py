class ApiError(Exception):
    def __init__(self, msg, code, submsg=None, subcode=None, params=None):
        self.message = msg
        self.submsg = submsg
        self.code = code
        self.subcode = subcode
        self.params = params

    def __str__(self):
        return '{}({})'.format(self.message, self.code) \
               + (', {}({})'.format(self.submsg,self.subcode) if self.submsg else '') \
               + (', params: {}'.format(self.params) if self.params else '')