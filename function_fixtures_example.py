import pytest


@pytest.fixture
def mock_api_response():
    return [{
        "id": 1,
        "name": "Alice",
        "age": 28,
        "pets": [{
            "type": "cat",
            "name": "Whiskers"
        }]
    }, {
        "id": 2,
        "name": "Bob",
        "age": 34,
        "pets": [{
            "type": "dog",
            "name": "Fido"
        }]
    }, {
        "id": 3,
        "name": "Charlie",
        "age": 22,
        "pets": [{
            "type": "bird",
            "name": "Tweety"
        }]
    }]


@pytest.fixture(params=["Alice", "Bob", "Charlie"])
def person_data(mock_api_response, request):
    return next(p for p in mock_api_response if p["name"] == request.param)


@pytest.fixture
def test_person(person_data):
    assert person_data is not None
    modify_person_data = person_data.copy()
    if person_data['name'] == "Alice":
        modify_person_data['pets'][0]['name'] = modify_person_data['pets'][0]['name'].upper()
    else:
        modify_person_data['pets'].append({
            "type": "fish",
            "name": "Nemo"
        })
    assert modify_person_data is not None
    # you should change the assertion to 1 or 2 if you want to pass the first test so that the test will pass,
    # and you can see the result from the second test - test_pet
    assert len(modify_person_data['pets']) == 2  # or 1
    return modify_person_data


def test_pet(test_person):
    pets_names = [pet['name'] for pet in test_person['pets']]
    for pet_name in pets_names:
        assert isinstance(pet_name, str) and pet_name.isalpha(), "Invalid pet name"
        # remove "NEMO" from the list to see the result of the second test - test_pet
        assert pet_name.upper() in ["WHISKERS", "FIDO", "TWEETY", "NEMO"], "Unexpected pet name"