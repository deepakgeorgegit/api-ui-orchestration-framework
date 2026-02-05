import requests


class AuthAPI:

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(
            "https://reqres.in/api/login",
            json=payload)

        return response


    def get_session_cookie(self,response):
        return response.cookies