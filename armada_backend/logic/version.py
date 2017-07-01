import os
import falcon


class Version(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = os.environ.get("ARMADA_VERSION", "none")
