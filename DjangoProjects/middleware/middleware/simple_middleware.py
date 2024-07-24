def simple_middleware(get_response):
    def middleware(request):

        #forward going area
        print("This is before view")
        reponse = get_response(request)
        print("This is after view")

        return reponse
    return middleware
