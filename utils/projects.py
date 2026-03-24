from .json_files import getBaseURL
import requests

def get_projects_count(): return len(requests.get(f"{getBaseURL()}/api/projects/count/").json())

def get_projects(c=None):
  if c: return requests.get(f"{getBaseURL()}/api/projects/?c={c}").json()['projects']
