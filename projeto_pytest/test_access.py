import pytest


@pytest.fixture(params=[
    {"role": "admin", "access": True},
    {"role": "editor", "access": True},
    {"role": "guest", "access": False}
])
def user_data(request):
    return request.param


def test_access_control(user_data):
    if user_data["role"] == "guest":
        assert user_data["access"] is False
    else:
        assert user_data["access"] is True