from typing import List, Optional
from models.script import Script, ScriptCreate
from data.repositories.script_repository import ScriptRepository
import uuid
from datetime import datetime


class ScriptService:
    def __init__(self, repo: ScriptRepository):
        self.repo = repo

    def create_script(self, script: ScriptCreate) -> Script:
        return self.repo.create_script(script)

    def get_script(self, script_id: str) -> Script:
        return self.repo.get_script(script_id)

    def get_all_scripts(self) -> List[Script]:
        return self.repo.get_all_scripts()
