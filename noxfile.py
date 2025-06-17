"""Nox configuration for automated testing, linting, and type checking."""

import nox

# Default sessions to run when nox is called without arguments
nox.options.sessions = ["lint", "typecheck", "test"]

# Python versions to test against
PYTHON_VERSIONS = ["3.10"]


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    """Run the test suite."""
    session.install("-e", ".[dev]")
    session.run(
        "pytest",
        "--cov=voice_transcriber",
        "--cov-report=term-missing",
        "--cov-report=xml",
        "tests/",
        *session.posargs,
    )


@nox.session(python=PYTHON_VERSIONS)
def lint(session):
    """Run the linters."""
    session.install("-e", ".[dev]")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")


@nox.session(python=PYTHON_VERSIONS)
def typecheck(session):
    """Run the type checker."""
    session.install("-e", ".[dev]")
    session.run("mypy", "src/voice_transcriber", "tests/")


@nox.session(python=PYTHON_VERSIONS)
def format(session):
    """Format the code."""
    session.install("-e", ".[dev]")
    session.run("ruff", "format", ".")


@nox.session(python=PYTHON_VERSIONS)
def fix(session):
    """Fix linting issues automatically."""
    session.install("-e", ".[dev]")
    session.run("ruff", "check", "--fix", ".")
    session.run("ruff", "format", ".") 