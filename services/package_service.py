import datetime
from typing import List, Optional
from data.package import Package
from data.release import Release


def package_count() -> int:
    return 172_280

def release_count() -> int:
    return 320_826
        
def packages(limit) -> List:
    return [
        {'id': 'fastapi', 'summary' : 'fast and beautiful pythpn framework'},
        {'id': 'uvicorn', 'summary' : 'your favorite ASGI server'},
        {'id': 'httpx', 'summary' : 'window to async world'},
        ][:limit]

def get_service_by_id(package_name: str) -> Package:
    package = Package(
        package_name, 'his is the summary', 'ull details here',
        'https://fastapi.tiangolo.com/', 'MIT', 'sebastian ramirez'
    )
    return package

def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release('1.2.0', datetime.datetime.now())