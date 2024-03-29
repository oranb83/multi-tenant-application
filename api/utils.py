from threading import local

_thread_locals = local()


def get_current_request():
    return getattr(_thread_locals, 'request', None)

def set_current_request(request):
    setattr(_thread_locals, 'request', request)
