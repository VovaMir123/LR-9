from flask import Flask

a = Flask(__name__)

@a.route('/')
def site():
    return "Это мой второй сайт!!!"

if __name__ == "__main__":
    a.run(host="0.0.0.0")
