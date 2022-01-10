from starlette.requests import Request
from viewmodels.shared.viewmodel_base import ViewModelBase
from data.user import User


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('Michael', 'michaelqw@mail.ru', 'hcahcvasbhckjav')