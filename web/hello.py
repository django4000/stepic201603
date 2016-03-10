def wsgi_application(env,response)
        response('200 OK', [])
	return [env.wsgi.input]
