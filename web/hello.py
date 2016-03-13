
def hello (env,start_response):

   pars=env.get('QUERY_STRING').split("&")
   start_response('200 OK', [('Content-Type','text/html')])
   return iter("\n".join(pars))
