from app import create_app
from app.config import Config

app = create_app(Config)


def main():
    app.run(host=Config.SERVER_HOST, port=Config.SERVER_PORT)


if __name__ == "__main__":
    main()
