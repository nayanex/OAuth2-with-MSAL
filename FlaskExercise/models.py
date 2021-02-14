from flask_login import UserMixin
from FlaskExercise import login


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login.user_loader
def load_user(user_id):
    # Normally, Flask would have you check your DB for the user ID
    # We're just allowing any authenticated user in for now
    return User(0)
    # User.query.get(int(user_id))
