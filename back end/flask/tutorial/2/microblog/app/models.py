from app import db
from hashlib import md5

class User(db.Model):

    id        = db.Column(db.Integer, primary_key=True)
    nickname  = db.Column(db.String(64), index=True, unique=True)
    email     = db.Column(db.String(120), index=True, unique=True)
    posts     = db.relationship('Post', backref='autor', lazy='dynamic')
    about_me  = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() == None:
                break
            version += 1
        return new_nickname
    
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
        
    def get_id(self):
        return unicode(self.id)
        
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar' + md5(self.email).hexdigest() + '?/d=mm&s=' + str(size)
    
    def __str__(self):
        return '<User %r>' % self.nickname
        
    __repr__ = __str__
    
class Post(db.Model):
    
    id        = db.Column(db.Integer, primary_key=True)
    body      = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return '<Post %r>' % self.body
        
    __repr__ = __str__