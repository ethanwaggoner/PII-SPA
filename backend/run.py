from flask_migrate import Migrate

from app.models.database import db
from app import create_app

app = create_app()
Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
