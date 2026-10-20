import pytest
from BaseApi import YougileApi

api = YougileApi()


def test_create_project_positive():
    response = api.create_project(title="Как же")

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    response = api.create_project(title="Мне", use_token=False)

    assert response.status_code == 401


def test_update_project_positive():
    create_res = api.create_project(title="Впадлу")
    project_id = create_res.json()["id"]

    response = api.update_project(project_id=project_id, new_title="Делать")

    assert response.status_code == 200


def test_update_project_negative():
    invalid_id = "00000000-0000-0000-0000-000000000000"

    response = api.update_project(project_id=invalid_id, new_title="Эту")

    assert response.status_code == 404


def test_get_project_positive():
    create_res = api.create_project(title="Домашку")
    project_id = create_res.json()["id"]

    response = api.get_project(project_id=project_id)

    assert response.status_code == 200
    assert response.json()["title"] == "Домашку"


def test_get_project_negative():
    invalid_id = "domashka-very-skuchno-programming-ochen-hard"

    response = api.get_project(project_id=invalid_id)

    assert response.status_code in [400, 404]
