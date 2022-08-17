import os
from flask import Blueprint,render_template, request, redirect, url_for
from app.models.base import db
from app.models.admin import Admin
from app.models.visitor import Visitor
from app.models.visitHistory import VisitHistory
from sqlalchemy import or_,and_,all_,any_

adminBP = Blueprint('Admin',__name__)

# set save path
save_path = os.path.join(os.path.dirname(__file__),'export_file')

@adminBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 获取姓名密码
        staffID = request.form.get('staffID')
        _password = request.form.get('password')
        loginResult = Admin.query.filter(and_(Admin.id == staffID,Admin._password == _password)).first()
        if loginResult:
            global username
            username = loginResult.name    
            return redirect(url_for('Admin.adminPage'))
        else:
            return render_template('login.html', error_msg = '员工ID或密码错误，请重新输入。')

@adminBP.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        usename = None
        return redirect(url_for('Admin.login'))

@adminBP.route('/searchHistory', methods=['GET', 'POST'])
def searchHistory():
    if request.method == 'GET':
        return render_template('searchHistory.html')
    else:
        id = request.form.get('id')
        visitor = Visitor.query.filter(Visitor.id == id).first()
        if visitor:
            records = VisitHistory.query.filter(VisitHistory.seq == visitor.seq).all()
            if records:    
                recordInfo = []          
                for eachRecord in records:
                    eachRecordInfo = []
                    eachRecordInfo.append(eachRecord.recordID)
                    eachRecordInfo.append(visitor.id)
                    eachRecordInfo.append(visitor.name)
                    eachRecordInfo.append(visitor.teleNum)                  
                    eachRecordInfo.append(eachRecord.arrivalTime)
                    if eachRecord.depatureTime:
                        eachRecordInfo.append(eachRecord.depatureTime)
                    else:
                        eachRecordInfo.append("未出园") 
                    recordInfo.append(eachRecordInfo) 
                return render_template('searchHistory.html', recordInfo=recordInfo)
            else:
                return render_template('searchHistory.html', msg="该用户不存在。")
        else:
            return render_template('searchHistory.html', msg="该用户不存在。")

@adminBP.route('/searchVisitor', methods=['GET', 'POST'])
def searchVisitor():
    if request.method == 'GET':
        return render_template('searchVisitor.html')
    else:
        id = request.form.get('id')
        visitor = Visitor.query.filter(Visitor.id == id).first()
        if visitor:
            visitorInfo = []
            visitorInfo.append(visitor.seq)
            visitorInfo.append(visitor.id)
            visitorInfo.append(visitor.name)
            visitorInfo.append(visitor.gender)
            visitorInfo.append(visitor.teleNum)
            visitorInfo.append(visitor.homeAddress)
            visitorInfo.append(visitor._password)
            return render_template('searchVisitor.html', visitorInfo=visitorInfo)
        else:
            return render_template('searchVisitor.html', msg="该用户不存在。")
        
@adminBP.route('/adminPage', methods=['GET'])
def adminPage():
    if request.method == 'GET':
        return render_template('index.html', username = username)

@adminBP.route('/visitorInfo', methods=['GET', 'POST'])
def visitorInfo():
    if request.method == 'GET':
        visitors = Visitor.query.all()
        totalNum = Visitor.query.count()
        visitorInfo = []
        for eachVisitor in visitors:
            eachVisitorInfo = []
            eachVisitorInfo.append(eachVisitor.id)
            eachVisitorInfo.append(eachVisitor.name)
            eachVisitorInfo.append(eachVisitor.gender)
            eachVisitorInfo.append(eachVisitor.teleNum)
            eachVisitorInfo.append(eachVisitor.homeAddress)
            eachVisitorInfo.append(eachVisitor._password)
            eachVisitorInfo.append(eachVisitor.seq)
            visitorInfo.append(eachVisitorInfo)
        return render_template('visitorInfo.html', visitorInfo = visitorInfo, totalNum = totalNum)
    else:
        # 新增用户
        id = request.form.get('id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        teleNum = request.form.get('teleNum')
        password = request.form.get('password')
        homeAddress = request.form.get('homeAddress')
        with db.auto_commit():
            visitor = Visitor()
            visitor.id = id
            visitor.name = name
            visitor._password = password
            visitor.gender = gender
            visitor.teleNum = teleNum
            visitor.homeAddress = homeAddress
            db.session.add(visitor)

        #更新用户列表            
        visitors = Visitor.query.all()
        totalNum = Visitor.query.count()
        visitorInfo = []
        for eachVisitor in visitors:
            eachVisitorInfo = []
            eachVisitorInfo.append(eachVisitor.id)
            eachVisitorInfo.append(eachVisitor.name)
            eachVisitorInfo.append(eachVisitor.gender)
            eachVisitorInfo.append(eachVisitor.teleNum)
            eachVisitorInfo.append(eachVisitor.homeAddress)
            eachVisitorInfo.append(eachVisitor.seq)
            visitorInfo.append(eachVisitorInfo)
        return render_template('visitorInfo.html', visitorInfo = visitorInfo, totalNum = totalNum)

@adminBP.route('/visitorHistory', methods=['GET'])
def visitorHistory():
    if request.method == 'GET':
        historyRecords = VisitHistory.query.all()
        totalNum = VisitHistory.query.count()
        historyInfo = []
        for eachHistoryRecord in historyRecords:
            eachHistoryRecordInfo = []
            visitorInfo = Visitor.query.get(eachHistoryRecord.seq)
            eachHistoryRecordInfo.append(visitorInfo.id)
            eachHistoryRecordInfo.append(visitorInfo.name)
            eachHistoryRecordInfo.append(visitorInfo.teleNum)
            eachHistoryRecordInfo.append(eachHistoryRecord.arrivalTime)
            if eachHistoryRecord.depatureTime:
                eachHistoryRecordInfo.append(eachHistoryRecord.depatureTime)
            else:
                eachHistoryRecordInfo.append("未出园")
            eachHistoryRecordInfo.append(eachHistoryRecord.recordID)  
            historyInfo.append(eachHistoryRecordInfo)
        return render_template('visitorHistory.html', historyInfo = historyInfo, totalNum = totalNum)

@adminBP.route('/deleteRecord/<recordID>/', methods=['GET'])
def deleteRecord(recordID):
    if request.method == 'GET':
        with db.auto_commit():
            VisitHistory.query.filter(VisitHistory.recordID == recordID).delete()
        return redirect(url_for('Admin.visitorHistory'))

@adminBP.route('/deleteUserInfo/<userID>/', methods=['GET'])
def deleteUserInfo(userID):
    if request.method == 'GET':
        with db.auto_commit():
            Visitor.query.filter(Visitor.seq == userID).delete()
        return redirect(url_for('Admin.visitorInfo'))

@adminBP.route('/deleteRecordForSearchPage/<recordID>/', methods=['GET'])
def deleteRecordForSearchPage(recordID):
    if request.method == 'GET':
        with db.auto_commit():
            VisitHistory.query.filter(VisitHistory.recordID == recordID).delete()
        return render_template('searchHistory.html', msg="已成功删除。")

@adminBP.route('/deleteUserInfoForSearchPage/<userID>/', methods=['GET'])
def deleteUserInfoForSearchPage(userID):
    if request.method == 'GET':
        with db.auto_commit():
            Visitor.query.filter(Visitor.seq == userID).delete()
        return render_template('searchVisitor.html', msg="已成功删除。")