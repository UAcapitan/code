
import hashlib
# from models import db

def encrypte_password(password):
    return hashlib.md5(password.encode("utf_8")).hexdigest()

# def add_to_db(obj):
    # db.session.add(obj)
    # db.session.commit()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}