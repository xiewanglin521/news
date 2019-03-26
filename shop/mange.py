from flask import Flask
from info.shop.index import index_blue
from flask_script import Manager
from models import *
#迁移
from flask_migrate import Migrate,MigrateCommand
from apps import app

manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
#注册前台蓝图
app.register_blueprint(index_blue)

if __name__ == "__main__":
    # manage.run()
    app.run()

