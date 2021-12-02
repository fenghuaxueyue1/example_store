from app import create_app
from app.config import Config


app = create_app(Config)


@app.route("/")
def index():
    return "INDEX"


def main():
    app.run()


if __name__ == "__main__":
    main()
