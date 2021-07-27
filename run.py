# python imports

# project imports
from app import app, db

# run app
if __name__ == '__main__':
    db.create_all()
    app.run()
