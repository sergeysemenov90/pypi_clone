from typing import Optional

from starlette.requests import Request

from services import user_service
from viewmodels.shared.viewmodel_base import ViewModelBase
from data.user import User


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user: Optional[User] = None

    async def load(self):
        self.user = await user_service.get_user_by_id(self.user_id)
