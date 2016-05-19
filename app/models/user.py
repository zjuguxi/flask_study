class Follow(db.Modle):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForiegnKey('user.id'), primary_key = True)
    followed_id = db.Column(db.Integer, db.ForiegnKey('user.id'), primary_key = True)
    timestamp = db.Column(db.Datetime, default = datetime.utcnow)