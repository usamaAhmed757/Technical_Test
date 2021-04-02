

from settings import db






class Contact(db.Model):
    __tablename__ = u'contact'
    id = db.Column(db.Integer,primary_key=True)
    user_name= db.Column(db.String(50),unique=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))

    def __init__(self,user_name,first_name,last_name):
        self.user_name=user_name
        self.first_name=first_name
        self.last_name=last_name


    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()
class Emails(db.Model):
    __tablename__ = u'emails'
    id = db.Column(db.Integer,primary_key=True)
    email_id = db.Column(db.String(50), unique=True)
    contact_id=db.Column(db.Integer, db.ForeignKey('contact.id',ondelete="CASCADE"))
    contact=db.relationship('Contact', backref=db.backref('stocktrack', lazy='dynamic'))



