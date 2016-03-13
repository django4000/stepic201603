CONFIG = {
    # 'mode': 'wsgi',
    #'working_dir': '/home/box/web/',
    # 'python': '/usr/bin/python',
    'args': (
        '--chdir=/home/box/web',
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        'hello',
    ),
} 
