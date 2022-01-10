from typing import List
from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request
from services.package_service import package_count, release_count, packages
from services.user_service import user_count


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = package_count()
        self.release_count: int = release_count()
        self.user_count: int = user_count()
        self.packages: List = packages(limit=5)