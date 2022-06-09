# encoding=utf8

import os

workers_num = 2
port = os.getenv('PORT', '8443')
bind = '0.0.0.0:{}'.format(port)  # 绑定地址
workers = workers_num
threads = 2
print('Child process number: {} with port: {}'.format(workers, port))

graceful_timeout = 6
backlog = 2048

proc_name = 'Django'
preload_app = True
capture_output = True

# loglevel = 'debug'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'  # noqa
# f_path = os.getenv('FLASK_APPLOGS_DIR', '.')
# accesslog = os.getenv('ACCESSLOG', default='log/access.log')
# errorlog = os.getenv('ERRORLOG', default='log/error.log')
