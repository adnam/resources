# -*- coding: utf8 -*-
"""
"""
import requests, json

class Resource:
    _uri = None
    _client = None
    _opts = {}

    def __init__(self, uri, client = None, options = {}):
        #print "Resource.__init__(%s)" % uri
        self._uri = uri
        self._client = requests.api if client is None else client
        self.set(options)
    
    def set_uri(self, uri):
        self._uri = uri
        return self

    def __repr__(self): return "<Resource %s>" % self._uri
    def __unicode__(self): return self._uri
    __str__ = __unicode__
    
    def set(self, opts):
        self._opts.update(opts)
        return self

    def request(self, method, **kwargs):
        #print "Resource.request()", method, args, kwargs
        #def req_method(*args, **kwargs):
        #    return self._client.request(method, self._uri, *args, **kwargs)
        response = self._client.request(method, self._uri, **kwargs)
        return getattr(response, "status_code", None), getattr(response, "text", None)
    def __getitem__(self, name):
        #print "Resource.__getitem__()", name
        return self.__class__("%s/%s" % (self._uri.rstrip('/'), name), self._client, options=self._opts)
    __getattr__ = __getitem__
    def get(self, **kwargs):     return self.request('get', **kwargs)
    def post(self, **kwargs):    return self.request('post', **kwargs)
    def put(self, **kwargs):     return self.request('put', **kwargs)
    def delete(self, **kwargs):  return self.request('delete', **kwargs)
    def head(self, **kwargs):    return self.request('head', **kwargs)
    def options(self, **kwargs): return self.request('options', **kwargs)
    def patch(self, **kwargs):   return self.request('patch', **kwargs)

class JsonResource(Resource):

    def request(self, method, **kwargs):
        #print "JsonResource.request()", method, args, kwargs
        if kwargs.has_key('data'):
            kwargs['data'] = json.dumps(kwargs.get('data'))
        kwargs = dict(self._opts.items() + kwargs.items())
        status_code, text = Resource.request(self, method, **kwargs)
        try:
            return status_code, json.loads(text)
        except ValueError:
            return 502, "The server did not return a valid JSON response"

