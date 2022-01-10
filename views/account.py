import fastapi
from starlette import requests
from starlette.requests import Request
from starlette import status

from infrastructure import cookie_auth
from services import user_service
from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from fastapi_chameleon import template


router = fastapi.APIRouter()


@router.get('/account')
@template
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register')
@template
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return vm.to_dict()

    # TODO: create the account
    account = user_service.create_account(vm.name, vm.email, vm.password)
    # TODO: Login user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response


@router.get('/account/login')
@template
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template
async def login(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()
    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = 'The account does not exist or the password is wrong'
        return vm.to_dict()
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, user.id)
    return response


@router.get('/account/logout')
@template
def logout(request: Request):
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response