from first_cli.create_json import create_json
import json
import pytest

@pytest.fixture
def output_file(tmp_path):
    output_file = tmp_path / "result.json"

    return output_file

@pytest.fixture
def sample_data():
    data = {
        "summary": "hello",
        "mode": "brief",
        "input_chars": 5,
    }

    return data


def test_create_json_file(output_file,sample_data):
    result = create_json(sample_data, output_file)

    assert result == output_file
    assert output_file.exists()

def test_create_json_content(output_file,sample_data):

    create_json(sample_data, output_file)

    with output_file.open(
        "r",
        encoding="utf-8"
    ) as f:
        loaded = json.load(f)

    assert loaded == sample_data

@pytest.fixture
def parent_file(tmp_path):
    output_file = tmp_path / "nested" / "result.json"
    return output_file

def test_create_json_creates_parent_directory(parent_file,sample_data):

    create_json(sample_data, parent_file)
    assert parent_file.exists()
