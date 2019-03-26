from flask import Blueprint,make_response,render_template,session,request,jsonify,redirect,url_for,g,json

from apps import db
from models import *
from comm import isLogin
index_blue = Blueprint('index',__name__)

#初始化数据
@index_blue.route('/addcate')
def addCate():
    cate = Cate(name = '水果')
    cate1 = Cate(name = '生鲜')
    cate2 = Cate(name = '海鲜')
    db.session.add_all([cate,cate1,cate2])
    return 'ok'

#初始化数据
@index_blue.route('/addgoods')
def addgoods():
    goods = Goods(name = '苹果1',price = 1.5,descrip="都符合国家能否快速",content ='改革方式打开',image_url='static/upload/1.jpg',number = 10,cid = 1)
    goods1 = Goods(name = '葡萄1',price = 2.5,descrip="都fdsgfgg 否快速",content ='改革方式打开',image_url='static/upload/2.jpg',number = 10,cid = 2)
    goods2 = Goods(name = '香蕉1',price = 3.5,descrip="都符dsgfhgfdsds能否快速",content ='改革方式打开',image_url='static/upload/3.jpg',number = 10,cid = 3)
    goods3 = Goods(name = '苹果2',price = 1.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/1.jpg',number = 10,cid = 1)
    goods4 = Goods(name = '葡萄2',price = 2.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/2.jpg',number = 10,cid = 2)
    goods5 = Goods(name = '香蕉6',price = 3.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/3.jpg',number = 10,cid = 3)
    goods6 = Goods(name = '苹果3',price = 1.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/1.jpg',number = 10,cid = 1)
    goods7 = Goods(name = '葡萄3',price = 2.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/2.jpg',number = 10,cid = 2)
    goods8 = Goods(name = '香蕉4',price = 3.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/3.jpg',number = 10,cid = 3)
    goods9 = Goods(name = '苹果5',price = 1.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/1.jpg',number = 10,cid = 1)
    goods10 = Goods(name = '葡萄4',price =2.5,descrip="都符合国dfgbff快速",content ='改革方式打开',image_url='static/upload/2.jpg',number = 10,cid = 2)

    db.session.add_all([goods,goods1,goods2,goods3,goods4,goods5,goods6,goods7,goods8,goods9,goods10])
    return 'ok'



@index_blue.route('/')
def index():
    categoies = Cate.query.all()
    click_news_list = Goods.query.offset(0).limit(5)
    data = {'categoies':categoies,'click_news_list':click_news_list}
    
    return render_template('/index.html',data=data)




@index_blue.route('/goodslist',methods=['post','get'])
def goodlist(): 
    cid = request.args.get('id')
    current_page=request.args.get('p',1)
    page_count = 1
    goods=Goods.query.filter(Goods.cid==cid).paginate(int(current_page),page_count,False)
    data= {'goods':goods.items,'current_page':goods.page,'total_page':goods.pages,'cid':cid}
    return render_template('/goodslist.html',data= data) 
    




@index_blue.route('/content',methods=['post','get'])
def content():
    id = request.args.get('id',0)
    goods = Goods.query.filter(Goods.id ==id)
    cart=Comment.query.filter(Comment.good_id==id).all()

    data = {'goods':goods,'cart':cart}
    return render_template('/content.html',data=data)
#添加购物车
@index_blue.route('/addcart')
# @isLogin
def addcart():
    mes = {}
    # user =g.user
    user = session.get('username')
    user_id = User.query.filter(User.name==user).first()
    id =request.args.get('id')
    good = Goods.query.get(id)
    try:
        user1 = Cart.query.filter(Cart.uid ==user.id).first()
    except:
        user1 = None
    if user:
        if user1:
            try:
                cart=Cart.query.filter(Cart.name ==goods.name).first()
            except:
                cart = None
            if cart:
                cart.number +=1
                db.session(cart)
                mes['code']=200
                mes ['mes'] = "添加成功"
            else:
                addcart = Cart(name=good.name,price =good.price,number=1,gid=good.id,uid = user1.id)
                db.session.add(addcart)
                mes['code'] = 200
                mes['mes'] = '添加成功'
        else:
            addcart= Cart(name=good.name,price=good.price,number=1,gid =good.id,uid=user_id.id)
            db.session.add(addcart)
            mes['code'] = 200
            mes['mes'] = '添加成功'
    else:
        mes['code'] = 10010
        mes['mes'] = '请先登录'
    return jsonify(mes)

# 登录
@index_blue.route("/login",methods = ['post','get'])
def login():
    mes= {}
    if request.method == "POST":
        # 从登陆页面获取用户名和密码  
        username = session.get('username')
        name = request.form.get('username')
        password = request.form.get('password')
    #     # 如果不存在
        if not all([name,password]):
            mes['code'] = 10011
            mes['message'] = '参数不完整'
        else:
            admin = User.query.filter(User.name==name).first()
            if not admin:
                mes['code'] = 10012
                mes['message'] = '用户不存在'
            else:
                # 
                # flag = check_password_hash(admin.password_hash,password)
                if admin:
                    session['username'] = name
                    mes['code'] = '200'
                    mes['message'] ='成功'
                else:
                    mes['code'] = 10013
                    mes['message'] = '密码错误'
                    
        return jsonify(mes)
    return render_template('login.html')


@index_blue.route('/Cartlist')
def Cartlist():
    cart = Cart.query.all()
    sum = 0
    for i in cart:
        sum+=i.price * i.number
    return render_template('cart.html',cart=cart,sum=sum)
#发表评论
@index_blue.route('/comm',methods=['post'])
def comm():
    mes={}
    userid = session.get('userid')
    good_id = request.form.get('good_id')
    content = request.form.get('content')
    if not all([good_id,content]):
        mes['code'] = 10010
        mes['message'] ='参数错误' 
    else:

        comment = Comment(content = content,user_id =userid,good_id=good_id)
        db.session.add(comment)
        db.session.commit()
        mes['code'] = 200
        mes['message'] ='评论成功'       


    return jsonify(mes)
