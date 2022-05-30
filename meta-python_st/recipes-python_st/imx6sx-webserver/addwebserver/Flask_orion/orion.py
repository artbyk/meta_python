from app import create_app
from app.models import User
from app import cli

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, ssl_context=('cert.pem', 'key.pem'))

# cli.register(app)

