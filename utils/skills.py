from .json_files import getBaseURL
import requests

def get_skills_count(): return len(requests.get(f"{getBaseURL()}/api/skills/count/").json())

def get_skills(c=None):
  if c: return requests.get(f"{getBaseURL()}/api/skills/?c={c}").json()['skills']
