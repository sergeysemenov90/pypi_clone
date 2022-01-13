import datetime
from typing import Optional

from data.package import Package
from data.release import Release
from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request
from services import package_service


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.package: Optional[Package] = None
        self.latest_release: Optional[Release] = None
        self.latest_version = '0.0.0'
        self.is_latest = True
        self.maintainers = []

    async def load(self):
        self.package = await package_service.get_package_by_id(self.package_name)
        self.latest_release = await package_service.get_latest_release_for_package(self.package_name)

        if not self.package or not self.latest_version:
            return

        r = self.latest_release
        self.latest_version = f'{r.major_ver}.{r.minor_ver}.{r.build_ver}'
