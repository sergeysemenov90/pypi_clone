from typing import List
from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request
from services.package_service import package_count, release_count, last_packages
from services.user_service import user_count


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = 0
        self.release_count: int = 0
        self.user_count: int = 0
        self.packages: List = []

    async def load(self):
        self.package_count: int = package_count()
        self.release_count: int = release_count()
        self.user_count: int = await user_count()
        self.packages: List = last_packages(limit=5)
