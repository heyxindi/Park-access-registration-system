from flask import Flask
from app.controller import visitor, visitHistory, admin

# 定义注册蓝图方法
def register_blueprints(app):
    app.register_blueprint(visitor.visitorBP,url_prefix='/visitor')
    app.register_blueprint(visitHistory.visitHistoryBP,url_prefix='/visitHistory')
    app.register_blueprint(admin.adminBP,url_prefix='/admin')

    
    

# 注册插件(数据库关联)
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    # create_all要放到app上下文环境中使用
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.config.setting') # 基本配置(setting.py) 
    app.config.from_object('app.config.secure') # 重要参数配置(secure.py)
    # 注册蓝图与app对象相关联
    register_blueprints(app)
    # 注册插件(数据库)与app对象相关联
    register_plugin(app)
    # 一定要记得返回app
    return app