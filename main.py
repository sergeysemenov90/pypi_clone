import os.path
import fastapi
import uvicorn
import fastapi_chameleon

from db import db_session
from views import home, packages, account
from starlette.staticfiles import StaticFiles


app = fastapi.FastAPI()


def main():
    configure()
    setup_db()
    uvicorn.run(app, port=8001)


def configure():
    configure_routes()
    configure_templates()


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi_sqlite')
    db_session.global_init(db_file)

def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(packages.router)
    app.include_router(account.router)


def configure_templates():
    fastapi_chameleon.global_init('templates')


if __name__ == '__main__':
    main()
else:
    configure()