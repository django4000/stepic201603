from cgi import parse_qs
def hello (env,start_response):
   #pars=parse_qs(env.get('QUERY_STRING'))
   pars=env.get('QUERY_STRING').split("&")
   start_response('200 OK', [('Content-Type','text/html')])
   return [pars]
