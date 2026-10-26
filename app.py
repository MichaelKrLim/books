from flask import Flask

from lib.connection import close_db
from lib.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)
app.teardown_appcontext(close_db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
