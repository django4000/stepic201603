
def hello (env,start_response):

   pars=env.get('QUERY_STRING').split("&")
   start_response('200 OK', [('Content-Type','text/plain')])
   return iter("\n".join(pars))
