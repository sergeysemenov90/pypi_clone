from pathlib import Path

import fastapi
import uvicorn
import fastapi_chameleon

from data import db_session
from views import home, packages, account
from starlette.staticfiles import StaticFiles


app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, port=8001)


def configure():
    configure_routes()
    configure_templates()
    configure_db()


def configure_db():
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


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
