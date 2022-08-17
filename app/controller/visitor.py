from flask import Blueprint,render_template, request, redirect, url_for
from app.models.base import db
from app.models.visitor import Visitor
from app.models.visitHistory import VisitHistory
from sqlalchemy import or_,and_,all_,any_
import qrcode as qr
visitorBP = Blueprint('Visitor',__name__)

@visitorBP.route('/visitoradmin', methods=['GET','POST'])
def visitoradmin():
	if request.method == 'GET':
		return render_template('visit.html')
	else:
		_id= request.form.get('_id')
		name=request.form.get('name')
		pw=request.form.get('pw')
		pw1=request.form.get('pw1')
		address=request.form.get('address')
		gender=request.form.get('gender')
		pnumber=request.form.get('pnumber')
		loginResult = Visitor.query.filter(Visitor.id == _id).first()
		if loginResult:
			return render_template('visit.html', error_msg = '身份证已经被注册，请联系管理人员。')
		if pw!=pw1:
			return render_template('visit.html', error_msg = '验证密码有误。')
		else:
			with db.auto_commit():
				visitor = Visitor()
				visitor.id = _id
				visitor.name = name
				visitor._password = pw
				visitor.gender = gender
				visitor.teleNum = pnumber
				visitor.homeAddress = address
				db.session.add(visitor)
			return render_template('visit.html', msg = '注册成功，按此处返回登录。')

@visitorBP.route('/visitorlogin', methods=['GET','POST'])
def visitorlogin():
	if request.method == 'GET':
		return render_template('visitorlogin.html')
	else:
		global staffID
		staffID = request.form.get('staffID')
		_password = request.form.get('password')
		loginResult = Visitor.query.filter(and_(Visitor.id == staffID,Visitor._password == _password)).first()
		
		if loginResult:
			return redirect(url_for('Visitor.visitorinfo'))
		else:
			return render_template('visitorlogin.html', error_msg = '员工ID或密码错误，请重新输入。')

@visitorBP.route('/visitorinfo', methods=['GET','POST'])
def visitorinfo():
	if request.method == 'GET':
		visitor = Visitor.query.filter(Visitor.id == staffID).first()
		name=visitor.name
		seq=visitor.seq
		id = visitor.id
		record=VisitHistory.query.filter(VisitHistory.seq == seq).first()
		qr.make("姓名：" + name +'\n'+'身份证号：'+ id ).get_image().show()
		# if record:
		# 	at=record.arrivalTime
		# 	if at:			
		# 		qr.make("姓名："+name+'\n'+'身份证号：'+ id + '\n' + '入园时间：'+str(at)).get_image().show()
		# 		return render_template('information.html',name=name, at=at)
		# 	else:
		# 		qr.make("姓名："+name+'\n'+'身份证号：'+ id).get_image().show()
		# 		return render_template('information.html',name=name)
		# else:
		# 	qr.make("姓名："+name+'\n'+'身份证号：'+ id).get_image().show()
		# 	return render_template('information.html',name=name)

