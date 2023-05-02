from pathlib import Path

import pytest

from jsonschema import Draft202012Validator
from referencing import Resource
from referencing.jsonschema import DRAFT202012, SchemaRegistry
from referencing.exceptions import NoSuchResource

import yaml

SCHEMAS = Path("./models")


def retrieve_yaml(uri: str) -> Resource:
    """
    Load a YAML document as a Resource.

    From https://python-jsonschema.readthedocs.io/en/latest/referencing/#resolving-references-to-schemas-written-in-yaml
    """
    if not uri.startswith("./"):
        raise NoSuchResource(ref=uri)
    path = SCHEMAS / Path(uri.removeprefix("./"))
    contents = yaml.safe_load(path.read_text())
    return Resource.from_contents(contents, default_specification=DRAFT202012)


@pytest.fixture
def registry() -> SchemaRegistry:
    """
    Return a registry object that points to the schemas folder to allow $ref.
    resolution.
    """
    return SchemaRegistry(retrieve=retrieve_yaml)


@pytest.fixture
def load_schema():
    """
    Return a function that can load a schema given a path.
    """
    return retrieve_yaml


@pytest.fixture
def get_schema_validator(registry):
    """
    Return a function that gets a validator for a given schema.
    """

    def get_validator(schema):
        return Draft202012Validator(schema, registry=registry)

    return get_validator


@pytest.fixture
def schema_event_types(load_schema):
    return load_schema("./data-types/event-type.yaml")


@pytest.fixture
def schema_vehicle_states(load_schema):
    return load_schema("./data-types/vehicle-state.yaml")
