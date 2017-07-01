import falcon

from armada_backend.middleware import JSONMiddleware
from armada_backend.logic.version import Version
from armada_backend.logic.info import Info
from armada_backend.logic.env import Env
from armada_backend.logic.create import Create

api = falcon.API(middleware=[JSONMiddleware()])

api.add_route('/version', Version())
api.add_route('/info', Info())
api.add_route('/env/{container_id}/{key}', Env())
api.add_route('/create', Create())

