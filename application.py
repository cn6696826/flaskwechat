#encoding:utf-8
# 配置文件

#  app
from flask import Flask
# data db数据库
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
import os
# 按需加载配置
class Application(Flask):
    def __init__(self,import_name):
        # 继承自flask的方法
        super(Application,self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        # 根据环境变量引入配置文件
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py' %os.environ['ops_config'])

        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)

manager = Manager(app)


















