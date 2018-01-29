import yate

print(yate.start_respone('text/html'))

print(yate.do_form('add_timing_data.py', ['TimeValue'], text='Send'))