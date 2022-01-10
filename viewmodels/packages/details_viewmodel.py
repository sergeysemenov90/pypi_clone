import datetime
from data.release import Release
from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request
from services import package_service


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.package = package_service.get_service_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_package(package_name)
        self.latest_version = '0.0.0'
        self.is_latest = True
        self.maintainers = []

        if not self.package or not self.latest_version:
            return 
        
        self.latest_version = self.latest_release.version
        self.maintainers = self.package.maintainers