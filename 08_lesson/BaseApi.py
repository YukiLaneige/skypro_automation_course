import requests


def get_my_login():
    return "YOUR_LOGIN_HERE"


def get_my_password():
    return "YOUR_PASSWORD_HERE"


def get_my_company():
    return "YOUR_COMPANY_NAME"


class YougileApi:

    def __init__(self):
        self.base_url = "https://yougile.com"
        self.token = self._get_auth_token()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def _get_auth_token(self):
        auth = {
            "login": get_my_login(),
            "password": get_my_password(),
            "name": get_my_company()
        }

        target_company_id = None

        keys_data = {
            "login": get_my_login(),
            "password": get_my_password(),
            "companyId": target_company_id
        }

        keys_res = requests.post(f"{self.base_url}/api-v2/auth/keys/get",
                                 json=keys_data)
        keys_json = keys_res.json()

        api_key = keys_json[0].get("key")

        return api_key

    def create_project(self, title, use_token=True):
        current_headers = self.headers if use_token else {
            "Content-Type": "application/json"}
        project_data = {"title": title}
        return requests.post(f"{self.base_url}/api-v2/projects",
                             json=project_data, headers=current_headers)

    def update_project(self, project_id, new_title, use_token=True):
        current_headers = self.headers if use_token else {
            "Content-Type": "application/json"}
        update_data = {"title": new_title}
        return requests.put(f"{self.base_url}/api-v2/projects/{project_id}",
                            json=update_data, headers=current_headers)

    def get_project(self, project_id, use_token=True):
        current_headers = self.headers if use_token else {
            "Content-Type": "application/json"}
        return requests.get(f"{self.base_url}/api-v2/projects/{project_id}",
                            headers=current_headers)
