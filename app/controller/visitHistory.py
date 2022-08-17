from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.visitHistory import VisitHistory

visitHistoryBP = Blueprint('VisitHistory',__name__)

@visitHistoryBP.route('', methods=['GET'])
def getAssessment():
    with db.auto_commit():
        # book = Book()
        # book.title = 'aaa'
        # book.author = 'aaa'
        # book.binding = 'aaa'
        # book.publisher = 'aaa'
        # book.price = "100"
        # book.pages = 1000
        # book.pubdate = 'aaa'
        # book.isbn = 'aaa'
        # book.summary = 'aaa'
        # book.image = 'aaa'
        # # 数据库的insert操作
        # db.session.add(book)
        pass