from string import Template #从标准库的“string”模块导入“Template”类。它支持简单的字符串替换模板

def start_respone(resp="text/html"):
    '''
    用来创建一个CGI“Content-type:”行，参数缺省值是“text/html"
    '''
    return 'Content-type: ' + resp + '\n\n'

def include_header(the_title):
    '''
    the_title:标题
    打开模板文件（html），读入文件，换入提供的标题
    '''
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    # header.substitute：用在HTML页面最前面的标题中。
    # 页面本身存储在一个单独的文件“templates/header.html"中，可以根据需要替换标题
    return header.substitute(title=the_title)

def include_footer(the_links):
    '''
    打开模板文件（HTML)，读入文件，换入“the_links”中提供的HTML链接字典
    '''
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    # 将链接字典转换为一个字符串，然后在换入模板
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key \
        + '</a>&nbsp;&nbsp;&nbsp;&nbsp'
    footer = Template(foot_text)
    # 与“include_header”函数类似，这个函数使用一个字符串作为参数，来创建一个HTML页面的尾部。
    # 页面本身存储在一个单独的文件“templates/footer.html”中，参数用于动态地创建一组HTML链接标记。
    # 参宿应当是一个字典
    return footer.substitute(links=link_string)

def start_form(the_url, form_type="POST"):
    '''
    返回表单最前面的HTML，允许调用者指定URL、所使用的的方法
    '''
    return '<form action="' + the_url + '" method="' + form_type + '">'

def end_form(submit_msg="Submit"):
    '''
    返回表单末尾的HTML标记，同时还允许调用者制定表单submit按钮的文本
    '''
    return '<p></p><input type=submit value="' + submit_msg + '"></form>'

def radio_button(rb_name, rb_value):
    '''
    给定一个单选钮名和值，创建一个单选钮
    '''
    return '<input type="radio" name="' + rb_name + '" value="' + rb_value + '">' \
    + rb_value + '<br />'

def u_list(items):
    '''
    给定一个列表，转换为HTML无序列表。
    '''
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return u_string

def header(header_text, header_level=2):
    '''
    返回一个HTML标题标记
    '''
    return '<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>'

def para(para_text):
    return '<p>' + para_text + '</p>'
