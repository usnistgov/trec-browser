import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api as api_blueprint

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'trec.db')
db = SQLAlchemy(app)


def create_app():

    with app.app_context():

        db.Model.metadata.reflect(db.engine)
       
        db.create_all()
        app.register_blueprint(api_blueprint, url_prefix='/trec/api/v1')

    return app


if __name__ == '__main__':

    app = create_app()  
    app.run(host='0.0.0.0', port=5000, debug=True)
    