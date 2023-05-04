import random

import pytest

from jsonschema import ValidationError


@pytest.fixture
def schema_policy_rule(load_schema):
    return load_schema("./policy-rule.yaml")


@pytest.fixture
def policy_rule_states_validator(get_schema_validator, schema_policy_rule):
    """
    Get a jsonschema.Validator for the policy.rule.states property
    """
    policy_rule_states = schema_policy_rule.contents["$defs"]["states"]
    return get_schema_validator(policy_rule_states)


def test_policy_rule_states_propertyNames_valid(schema_vehicle_states, policy_rule_states_validator):
    # check that every vehicle state option is valid
    for vehicle_state in schema_vehicle_states.contents["enum"]:
        # make an instance like { "available": [] }
        instance = {vehicle_state: []}
        # expect no validation errors
        policy_rule_states_validator.validate(instance)


def test_policy_rule_states_propertyNames_invalid(policy_rule_states_validator):
    # make a bad instance: invalid state
    instance = {"not_a_vehicle_state": []}
    # expect ValidationError
    with pytest.raises(ValidationError):
        policy_rule_states_validator.validate(instance)


def test_policy_rule_states_values_valid(schema_event_types, policy_rule_states_validator):
    # make a valid instance with a subset of types
    event_types = random.sample(schema_event_types.contents["enum"], k=5)
    instance = {"available": event_types}
    # expect no ValidationError
    policy_rule_states_validator.validate(instance)


def test_policy_rule_states_values_invalid(policy_rule_states_validator):
    # make a bad instance: valid state, invalid event types
    instance = {"available": ["not_an_event", "nope_not_this_one"]}
    # expect ValidationError
    with pytest.raises(ValidationError):
        policy_rule_states_validator.validate(instance)
