from flask import Blueprint
from flask_restful import Api

from service.minecraft_service import *

minecraft_service_bp = Blueprint('minecraft_service_bp', __name__, url_prefix="/service/minecraft")
minecraft_service_api = Api()
minecraft_service_api.init_app(minecraft_service_bp)


minecraft_service_api.add_resource(TestReturn, "/test_return")
minecraft_service_api.add_resource(TestReturn2, "/test_return2")