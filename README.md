# Mobility Data Specification OpenAPI

The [Mobility Data Specification (MDS)](https://github.com/openmobilityfoundation/mobility-data-specification), a project of the Open Mobility Foundation (OMF), is a data standard to enable right-of-way regulation and two-way communication between mobility companies and local governments.

This is the OpenAPI description for MDS data feeds, managed by the [Open Mobility Foundation](https://github.com/openmobilityfoundation).

Online documentation is available on [Stoplight](https://openmobilityfnd.stoplight.io/docs/mds-openapi).

MDS versions are organized by branches starting with a branch for `v2.0`.

## Python project

A small Python project defined in [`pyproject.toml`](./pyproject.toml) supports the schema development process.

```bash
# install the project and its dependencies
pip install -e .
```

### Schema validation

Tests written in [`pytest`](https://pytest.org) check various components of the schemas. These tests can be run locally, and
also run in GitHub Actions on commits to this repository.

```bash
# run the tests with pytest from the root of the repo
pytest
```

### Notebooks

[Jupyter Notebooks](https://jupyter.org/) to help with one-time data cleanups and issue checking.

```bash
# install the 'notebooks' extras
pip install -e .[notebooks]
```

## License

The MDS OpenAPI, like MDS itself, is licensed under [Creative Commons Attribution 4.0 International Public License](../LICENSE)
