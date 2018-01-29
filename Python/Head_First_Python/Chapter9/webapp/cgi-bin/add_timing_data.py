import cgi
import os
import time
import sys
import yate

print(yate.start_respone('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
mothed = os.environ['REMOTE_METHOD']
cur_time = time.asctime(time.localtime())
print(host + ", " + addr + ", " + cur_time + ": " mothed + ": ", end='', file=sys.stderr)

form = cgi.FieldStorage()
for each_form_item in form.keys():
    