'''
第二章 共享你的代码块:函数模块
'''

'''
通过作为Python模块共享代码，可以向整个Python社区开放你的代码
Python提供了一组技术，可以很容易地实现共享，这包括模块和一些发布工具：
    * 模块允许你合理组织代码来实现最优共享
    * 发布工具允许你向全世界共享你的模块

共享前准备：
    1、将函数转换为模块：
        模块就是一个包含Python代码的文本文件，对模块的主要需求就是要求文件名以.py结尾。
'''
        # 将第一章中的函数 print_lol()保存到nester.py中

        # 查看Python模块放在计算机的位置
        import sys
        print(sys.path)

'''
        Python包索引(Python Package Index, PyPI)为Internet上的第三方Python模块提供了一个集中的存储库。

    2、代码注释：使用三重引号建立多行注释

准备发布：
    为了共享新创建的这个模块，需要准备一个发布。在Python中，所谓“发布”（distribution）只是一个文件集合，这些文件联合在一起允许你构建、打包和发布你的模块。
    一旦发布存在，就可以把模块安装到你的Python本地副本上，还可以把模块上传到PyPI与全世界共享
    1、首先为模块创建一个文件夹
'''
        # 创建文件夹，命名为nester，将nester.py模块文件复制到这个文件夹中。
'''
    2、在新文件夹中创建一个名为“setup.py”的文件
'''
        # 这个文件包含有关发布的元数据。编辑这个文件，增加下面代码：
        from distutils.core import setup  # 从Python发布工具导入“setup”函数

        setup{
            name = 'nester',
            version = '1.0.0',
            py_modules = ['nester'],
            author = 'Leo Qi',
            author_email = 'qilei101@gmail.com',
            url = 'https://www.leo-qi.github.io',
            description = 'A simple printer of nested lists',
        }
'''
构建发布：
    3、构建一个发布文件
'''
        # 发布工具包含有构建一个发布所需的所有功能。在nester文件夹中打开一个终端窗口键入命令：
        python3 setup.py sdist
'''
    4、将发布安装到你的Python本地副本中
'''
        # 仍然在终端窗口中，键入以下命令：
        sudo python3 setup.py install #windows去掉sudo
'''
发布速览：
    利用Python的发布工具，模块已经转换为一个发布，并且安装在你的Python本地副本上。
    开始时只有一个函数，这个函数输入到一个nester.py的文件中，这个就创建了一个模块。然后创建一个名为nester的文件夹存放这个模块。通过在这个文件夹中增加一个名为setup.py的文件，从而能构建和安装你的发布，这会生成一组额外的文件，并在nester文件夹中出现两个新的文件夹
    
    安装前：           安装后：
    nester            nester
      |                 |
       —— nester         —— MANIFEST    #这个文件中包含发布中的文件列表
      |                 |
       —— setup.py       —— build
                        |     |
                        |      —— lib
                        |          |
                        |           —— nester.py
                         —— dist
                        |     |
                        |      —— nester-1.0.0.tar.gz   #这是发布包
                         —— nester.py
                        |
                         —— nester.pyc  #“编译”版本的代码
                        |
                         —— setup.py

导入模块并使用 
'''
    # 使用模块时，需要导入到程序中，告诉Python将nester.py模块包含在程序中。
    import nester
'''
    Python的模块实现命名空间: 不能直接通过 print_lol()调用这个函数
'''
    cast = ['Palin','Clesse', 'Idle', 'Jones', 'Gilliam', 'Chapman']
    nester.print_lol(cast)
'''
    使用普通的import语句时，如import nester，这会提示Python解释器允许你使用命名空间限定访问nester的函数。还可以更为特定：
'''
    # 如果当前命名空间中已经定义了同名函数，特定import语句会覆盖掉自定义函数
    from nester import print_lol
'''
注册 PyPI网站

向PyPI上传代码
'''
"""
"""
'''
总结:
    pyc 文件说明 P76
    BIF 说明 P80
    内置函数（BIF）：P81
'''