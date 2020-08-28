from flask import Flask
from Routes.artist import search_artist_blueprint

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(search_artist_blueprint)

if __name__ == "__main__":
    app.run()
