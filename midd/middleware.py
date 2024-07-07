def my_middleware(get_response):
    print('middleware is the one time run')

    def myfunction(request):
      print('this is before view')

      response= get_response(request)
      print('this is after view')
      return response
    return myfunction