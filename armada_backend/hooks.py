
from armada_backend import docker_client
from armada_backend.utils import get_logger

HOOK_PATH = '/opt/microservice/src/hooks.py'


def run_hook(container_id, hook_name, timeout):
    get_logger().info('before hook')
    api = docker_client.api(timeout)
    command = ' '.join(['python', HOOK_PATH, hook_name])
    exec_id = api.exec_create(container_id, command)
    try:
        result = api.exec_start(exec_id['Id'])
        get_logger().info(result)
    except Exception as e:
        get_logger().exception(e)
    get_logger().info('after hook')
