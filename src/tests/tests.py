import unittest
from click.testing import CliRunner
from pvw.args_parser import *
import os
import sys
import logging

VENV_DEFAULT_PATH = os.path.join(os.path.expanduser("~"), "venvs")
log = logging.getLogger("pvwTesting")
PREFIX = "pvw_test_case"


class TestPvwCli(unittest.TestCase):
    def test_ls(self):
        runner = CliRunner()
        result1 = runner.invoke(ls)
        result2 = runner.invoke(ls, ["--show-size"])
        assert result1.exit_code == 0
        assert result2.exit_code == 0
        assert len(result1.output) > 0
        assert "Size" in result2.output

    def test_default_env(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            default_name = PREFIX + "_env_default"
            create_result = runner.invoke(create, [default_name])
            assert create_result.exit_code == 0
            assert os.path.exists(os.path.join(VENV_DEFAULT_PATH, default_name))

            cp_name = default_name + "_cp"
            cp_result = runner.invoke(cp, [default_name, cp_name])
            assert cp_result.exit_code == 0
            assert os.path.exists(os.path.join(VENV_DEFAULT_PATH, cp_name))

            mv_name = default_name + "_mv"
            mv_result = runner.invoke(mv, [cp_name, mv_name], input="y")
            assert mv_result.exit_code == 0
            assert os.path.exists(os.path.join(VENV_DEFAULT_PATH, mv_name))
            assert not os.path.exists(os.path.join(VENV_DEFAULT_PATH, cp_name))

            rm_result = runner.invoke(rm, f'"{PREFIX}.*"', input="y")
            ls_result = runner.invoke(ls)
            assert rm_result.exit_code == 0
            assert default_name not in ls_result.output

    def test_current_env(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            current_name = PREFIX + "_env_current"
            current_path = os.path.join(os.getcwd(), current_name)
            create_result = runner.invoke(create, [current_path])
            assert create_result.exit_code == 0
            assert os.path.exists(current_path)

            cp_name = current_name + "_cp"
            cp_path = os.path.join(os.getcwd(), cp_name)
            cp_result = runner.invoke(cp, [current_name, cp_path])
            assert cp_result.exit_code == 0
            assert os.path.exists(cp_path)

            mv_name = current_name + "_mv"
            mv_path = os.path.join(os.getcwd(), mv_name)
            mv_result = runner.invoke(mv, [cp_name, mv_path], input="y")
            assert mv_result.exit_code == 0
            assert os.path.exists(mv_path)
            assert not os.path.exists(cp_path)

            rm_result = runner.invoke(rm, f'"{PREFIX}.*"', input="y")
            ls_result = runner.invoke(ls)
            assert rm_result.exit_code == 0
            assert current_name not in ls_result.output

    def test_init(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            name = PREFIX + "_env_init"
            path = os.path.join(os.getcwd(), name)
            env_path = os.path.join(path, name)
            init_result = runner.invoke(init, [name], input="y\n\n")
            assert init_result.exit_code == 0
            assert os.path.exists(path)
            assert os.path.exists(env_path)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("pvwTesting").setLevel(logging.DEBUG)
    unittest.main(verbosity=2)
