import pytest
import data
import sender_stand_request

# Obtener el token de un nuevo usuario
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Pruebas positivas (código 201)
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Pruebas negativas (código 400)
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Pruebas individuales
def test_create_kit_1_character_name_success():
    positive_assert(data.kit_body_1)

def test_create_kit_511_characters_name_success():
    positive_assert(data.kit_body_2)

def test_create_kit_empty_name_error():
    negative_assert_code_400(data.kit_body_3)

def test_create_kit_512_characters_name_error():
    negative_assert_code_400(data.kit_body_4)

def test_create_kit_special_characters_name_success():
    positive_assert(data.kit_body_5)

def test_create_kit_spaces_in_name_success():
    positive_assert(data.kit_body_6)

def test_create_kit_numbers_in_name_success():
    positive_assert(data.kit_body_7)

def test_create_kit_no_name_parameter_error():
    negative_assert_code_400(data.kit_body_8)

def test_create_kit_number_type_name_error():
    negative_assert_code_400(data.kit_body_9)