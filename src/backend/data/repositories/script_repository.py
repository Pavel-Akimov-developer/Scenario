from models.script import Script, ScriptCreate
import uuid
from datetime import datetime


class ScriptRepository:
    def __init__(self, conn):
        self.conn = conn

    def create_script(self, script: ScriptCreate) -> Script:
        script_id = str(uuid.uuid4())
        self.conn.execute(
            "INSERT INTO scripts (id, title, content) VALUES (?, ?, ?)",
            (script_id, script.title, script.content),
        )
        self.conn.commit()
        return self.get_script(script_id)

    def get_script(self, script_id: str) -> Script:
        cursor = self.conn.execute("SELECT * FROM scripts WHERE id = ?", (script_id,))
        result = cursor.fetchone()
        return Script(**dict(result)) if result else None
