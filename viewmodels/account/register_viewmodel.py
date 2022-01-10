from typing import Optional
from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    async def load(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.email = form.get('email')
        self.password = form.get('password')

        if not self.name:
            self.error = 'Your name is required'

        elif not self.email:
            self.error = 'Your email is required'

        if not self.password or len(self.password) < 5:
            self.error = 'Your password is required and must be at least 5 characters'
