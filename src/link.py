import requests
from requests.adapters import HTTPAdapter
from sys import exit
import concurrent.futures
import threading

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    print(thread_local.session)
    return thread_local.session

def scan_link(url, session):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {response.status_code} from {url}")

def all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scan_link, sites)

def scan_links(links, verbose=False):
    print(links)
    all_sites(links)
