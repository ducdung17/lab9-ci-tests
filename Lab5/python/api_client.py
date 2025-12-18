from dataclasses import dataclass
from typing import Any, Dict
import requests


@dataclass(frozen=True)
class JsonPlaceholderClient:
    base_url: str
    session: requests.Session

    def get_user(self, user_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/users/{user_id}", timeout=15)

    def create_user(self, payload: Dict[str, Any]) -> requests.Response:
        return self.session.post(f"{self.base_url}/users", json=payload, timeout=15)

    def update_user(self, user_id: int, payload: Dict[str, Any]) -> requests.Response:
        return self.session.put(f"{self.base_url}/users/{user_id}", json=payload, timeout=15)
