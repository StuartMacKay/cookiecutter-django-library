import os
import subprocess

import pytest

CONTEXT = {
    "create_project": "y",
    "test_runner": "pytest",
}

# None of the calls to subprocess.run() pass capture_output=True. There
# is no need if the test is passing and it's easily added if the test
# is failing. Alternatively when running pytest from the command line
# you can pass in --keep-baked-projects to stop any clean up after the
# tests have run. You can then find the generated project in /tmp and
# run the command directly to see why it's failing.


@pytest.fixture(scope="session")
def project(cookies_session):
    """Generate the project and return the path to the root directory

    The session scoped cookies fixture is not documented. It was added in
    https://github.com/hackebrot/pytest-cookies/pull/46/
    """
    result = cookies_session.bake(extra_context=CONTEXT)
    return str(result.project)


def test_run_migrations(project):
    """Verify the migrations run so we know Django is configured correctly"""
    python = os.path.join(project, "venv", "bin", "python")
    db = os.path.join(project, "db.sqlite3")
    assert not os.path.exists(db)
    subprocess.run([python, "manage.py", "migrate"], cwd=project, check=True)
    assert os.path.exists(db)


def test_run_tests(project):
    """Verify the tests run successfully, including black, flake8 and isort checks"""
    runner = os.path.join(project, "venv", "bin", "pytest")
    subprocess.run([runner], cwd=project, check=True)


def test_make_build(project):
    """Verify the Makefile can create the distribution so we know it's syntactically correct"""
    dist_dir = os.path.join(project, "dist")
    wheel = os.path.join(dist_dir, "django_app-0.1-py2.py3-none-any.whl")
    sdist = os.path.join(dist_dir, "django-app-0.1.tar.gz")
    assert not os.path.exists(dist_dir)
    subprocess.run(["make", "build"], cwd=project, check=True)
    assert os.path.exists(dist_dir)
    assert os.path.exists(wheel)
    assert os.path.exists(sdist)
