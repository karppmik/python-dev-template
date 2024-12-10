"""Test package version"""

from {{cookiecutter.package_name}} import __version__

def test_version() -> None:
    "Check that version matches expected"
    assert __version__ == "{{ cookiecutter.version }}"