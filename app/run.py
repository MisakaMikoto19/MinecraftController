from flask import Flask

from router.routes import minecraft_service_bp  # Adjusted import path

def create_app():
    app = Flask(__name__)

    # 注册 main Blueprint
    app.register_blueprint(minecraft_service_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run("0.0.0.0", 50003, True)