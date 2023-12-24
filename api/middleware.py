from api.utils import set_current_request


class RouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_current_request(request)
        return self.get_response(request)
