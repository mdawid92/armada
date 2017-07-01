import falcon
import json
from armada_backend import docker_client


class Env(object):
    def on_get(self, req, resp, container_id, key):
        try:
            docker_api = docker_client.api()
            docker_inspect = docker_api.inspect_container(container_id)
            value = None
            for env_var in docker_inspect['Config']['Env']:
                env_key, env_value = (env_var.strip('"').split('=', 1) + [''])[:2]
                if env_key == key:
                    value = env_value
                    break

            if value is None:
                pass
            resp.context['data'] = {'value': str(value)}
        except Exception as e:
            pass
