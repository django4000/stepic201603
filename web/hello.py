from cgi import parse_qs
def wsgi_application(env,start_response)
   pars=parse_qs(env.get('QUERY_STRING'))
   start_response('200 OK', [('Content-Type':'text/html')])
   return [pars]
