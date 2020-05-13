from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User(UserMixin, db.Model):
    """Model for user accounts"""

    id = db.Column(db.Integer,
                   primary_key=True)

    name = db.Column(db.String,
                     nullable=False,
                     unique=False)

    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)

    password = db.Column(db.String(200),
                         nullable=False)

    created_on = db.Column(db.DateTime)

    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
