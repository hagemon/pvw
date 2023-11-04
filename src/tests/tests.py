import unittest
from click.testing import CliRunner
from pvw.args_parser import *
import os
import sys
import logging


ISOLATED_PATH = os.path.join(os.path.expanduser("~"), "isolated")
if not os.path.exists(ISOLATED_PATH):
    os.makedirs(ISOLATED_PATH)
log = logging.getLogger("pvwTesting")


class TestPvwCli(unittest.TestCase):
    def test_ls(self):
        runner = CliRunner()
        result1 = runner.invoke(ls)
        result2 = runner.invoke(ls, ["--show-size"])
        assert result1.exit_code == 0
        assert result2.exit_code == 0
        assert len(result1.output) > 0
        assert "Size" in result2.output

    def test_create_in_default_path(self):
        runner = CliRunner()
        with runner.isolated_filesystem(ISOLATED_PATH):
            result = runner.invoke(create, ["test_case_env_default"])
            ls_result = runner.invoke(ls)
            assert result.exit_code == 0
            assert "test_case_env_default" in ls_result.output

    # def test_ops_in_current_path(self):
    #     runner = CliRunner()
    #     with runner.isolated_filesystem():
    #         result1 = runner.invoke(create, ["./test_case_env_current"])
    #         result2 = runner.invoke(
    #             cp, ["test_case_env_current", "./test_case_env_current_cp"]
    #         )
    #         result3 = runner.invoke(
    #             mv, ["test_case_env_current_cp", "./test_case_env_current_mv"]
    #         )
    #         result4 = runner.invoke(
    #             rm, ["test_case_env_current", "./test_case_env_current_mv"]
    #         )
    #         assert result1.exit_code == 0
    #         assert result2.exit_code == 0
    #         assert result3.exit_code == 0
    #         assert result4.exit_code == 0

    # def test_ops_in_specific_path(self):
    #     runner = CliRunner()
    #     with runner.isolated_filesystem():
    #         tmp_dir_name = "pvw_test_tmp_dir"
    #         path = os.path.join('./', tmp_dir_name)
    #         runner = CliRunner()
    #         result1 = runner.invoke(
    #             create, [os.path.join(path, "test_case_env_specific")]
    #         )
    #         result2 = runner.invoke(
    #             cp,
    #             ["test_case_env_specific", os.path.join(path, "test_case_env_specific_cp")],
    #         )
    #         result3 = runner.invoke(
    #             mv,
    #             [
    #                 "test_case_env_specific_cp",
    #                 os.path.join(path, "test_case_env_specific_mv"),
    #             ],
    #         )
    #         result4 = runner.invoke(
    #             rm,
    #             ["test_case_env_specific", "test_case_env_specific_mv"],
    #         )
    #         assert result1.exit_code == 0
    #         assert result2.exit_code == 0
    #         assert result3.exit_code == 0
    #         assert result4.exit_code == 0


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("pvwTesting").setLevel(logging.DEBUG)
    unittest.main(verbosity=2)
