from hello import hello_app
from db import register_health_route
register_health_route(hello_app)
if __name__ == '__main__':
    hello_app.run(host='0.0.0.0', port=5000)