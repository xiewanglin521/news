from apps import db
from datetime import datetime
#基础表
class BaseModel(object):
    create_time = db.Column(db.DateTime,default = datetime.now)
    update_time = db.Column(db.DateTime,default = datetime.now)
#分类表

class Cate(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(30))

#产品表

class Goods(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(5,2))
    descrip = db.Column(db.String(225))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(100))
    number = db.Column(db.Integer)
    cid = db.Column(db.Integer,db.ForeignKey('cate.id'))
    cate = db.relationship(Cate)

#购物车表
class Cart(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(5,2))
    descrip = db.Column(db.String(225))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(100))
    number = db.Column(db.Integer)
    gid = db.Column(db.Integer,db.ForeignKey('goods.id'))
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))

# 管理员表
class User(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    password_hash = db.Column(db.String(30))


#评论表
class Comment(BaseModel,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(30))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    good_id = db.Column(db.Integer,db.ForeignKey('goods.id'))
    user= db.relationship(User)