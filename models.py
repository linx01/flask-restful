from run import db

class BookInfo(db.Model):

    __tablename__ = 'book_info'

    id = db.Column(db.Integer, primary_key=True)    # id 自增
    name = db.Column(db.String(255), nullable=False, unique=True)  # 书名
    author = db.Column(db.String(255), nullable=False)  # 作者
    country = db.Column(db.String(255), nullable=False)  # 国籍

    def __init__(self, name, author, country):
        self.name = name
        self.author = author
        self.country = country

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class PersionInfo(db.Model):

    __tablename__ = 'persion_info'

    id = db.Column(db.Integer, primary_key=True)    # id 自增
    name = db.Column(db.String(255), nullable=False)  # 人名
    book_name = db.Column(db.String(255), db.ForeignKey('book_info.name'))  # 书名

    def __init__(self, name,  book_name):
        self.name = name
        self.book_name = book_name

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


db.create_all()