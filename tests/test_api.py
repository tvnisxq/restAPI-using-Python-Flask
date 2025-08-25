import json

import pytest

from src import main


@pytest.fixture
def client():
    main.app.config["TESTING"] = True
    with main.app.test_client() as client:
        yield client


def test_root(client):
    r = client.get("/")
    assert r.status_code == 200
    data = r.get_json()
    assert data.get("message") == "Hello, World!"


def test_armstrong_endpoint_true(client):
    r = client.get("/armstrong/153")
    assert r.status_code == 200
    data = r.get_json()
    assert data["Armstrong"] is True


def test_armstrong_negative_input(client):
    r = client.get("/armstrong/-5")
    assert r.status_code == 400


def test_palindrome_endpoint_true(client):
    r = client.get("/palindrome/121")
    assert r.status_code == 200
    data = r.get_json()
    assert data["Palindrome"] is True


def test_palindrome_negative_input(client):
    r = client.get("/palindrome/-1")
    assert r.status_code == 400


def test_sum_get(client):
    r = client.get("/sum?a=2&b=3")
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 5


def test_sum_post(client):
    r = client.post("/sum", json={"a": 10, "b": 7})
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 17


def test_avg_get(client):
    r = client.get("/avg?a=2&b=3")
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 2.5


def test_avg_post(client):
    r = client.post("/avg", json={"a": 10, "b": 6})
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 8.0
