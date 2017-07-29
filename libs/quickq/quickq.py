import datetime
from importlib import import_module

from django import http
from django.conf import settings
from django.urls import reverse

import jwt
from requests_futures.sessions import FuturesSession

TOKEN_EXPIRATION = getattr(settings, 'QQ_TOKEN_EXPIRATION', 60)
TOKEN_ALGORITHMS = getattr(settings, 'QQ_TOKEN_ALGORITHMS', ['HS256'])
URL_NAME = getattr(settings, 'QQ_URL_NAME', 'taskinator')

class Task:
  def __init__ (self, *args, **kw):
    pass
    
  def __call__ (self, target):
    self.target = target
    return self.task_wrapper
    
  def execute (self, *args, **kw):
    return self.target(*args, **kw)
    
  def task_wrapper (self, *args, **kw):
    payload = {
      'args': args,
      'kw': kw,
      'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRATION),
      '__module__': self.target.__module__,
      '__name__': self.target.__name__,
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=TOKEN_ALGORITHMS[0])
    url = settings.BASE_URL + reverse(URL_NAME, args=[token])
    session = FuturesSession()
    future = session.get(url, timeout=60)
    
def taskinator (request, token):
  payload = jwt.decode(token, settings.SECRET_KEY, algorithms=TOKEN_ALGORITHMS)
  
  module = import_module(payload['__module__'])
  task = getattr(module, payload['__name__'])
  
  task.__self__.execute(*payload['args'], **payload['kw'])
  return http.HttpResponse('OK', content_type="text/plain")
  