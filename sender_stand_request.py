import requests
import data
import configuration

def post_new_user(body):
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer" + auth_token
    return requests.post(
        url=configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )