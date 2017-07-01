import falcon
import json


class JSONMiddleware(object):
    def process_request(self, req, resp):
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        req.context['data'] = json.loads(body.decode('utf-8'))

    def process_resource(self, req, resp, resource, params):
        pass

    def process_response(self, req, resp, resource, req_succeeded):
        if req_succeeded and 'data' in resp.context:
            resp.status = falcon.HTTP_200
            data = resp.context['data'].copy()
            data['status'] = 'ok'
            resp.body = json.dumps(data)
