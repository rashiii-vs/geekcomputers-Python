import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ping_subnet import ping_subnet


@pytest.fixture
def run_scan(tmp_path, monkeypatch):
    """Run the subnet scan with a mocked ping function."""

    def execute(subnet, folder_name):
        run_directory = tmp_path / folder_name
        run_directory.mkdir()

        calls = []

        def fake_ping(command, **kwargs):
            calls.append(command)
            return 0 if command.endswith(subnet + ".2") else 1

        monkeypatch.chdir(run_directory)

        ping_subnet(subnet, ping_function=fake_ping)

        log_file = run_directory / ("ping_" + subnet + ".log")
        actual_lines = log_file.read_text().splitlines()

        return calls, actual_lines

    return execute


def expected_output(subnet):
    """Calculate the expected output independently."""

    return (
        [subnet + ".2 is alive"]
        + [
            subnet + "." + str(host) + " did not respond"
            for host in range(3, 255)
        ]
    )


def test_smallest_prefix_input(run_scan):
    # Source line 24: range(2, 255) checks hosts 2 through 254.
    subnet = "0.0.0"

    calls, actual = run_scan(subnet, "smallest")
    expected = expected_output(subnet)

    assert len(calls) == 253
    assert actual == expected
    assert calls[0].endswith("0.0.0.2")
    assert calls[-1].endswith("0.0.0.254")


def test_ordinary_prefix_input(run_scan):
    subnet = "192.168.1"

    calls, actual = run_scan(subnet, "ordinary")
    expected = expected_output(subnet)

    assert len(calls) == 253
    assert actual == expected
    assert calls[0].endswith("192.168.1.2")
    assert calls[-1].endswith("192.168.1.254")


def test_repeated_runs_are_isolated(run_scan):
    first_calls, first_result = run_scan("192.168.1", "first")
    second_calls, second_result = run_scan("192.168.1", "second")

    run_scan("10.0.0", "other-subnet")

    third_calls, third_result = run_scan("192.168.1", "third")

    assert first_result == second_result
    assert first_result == third_result
    assert first_calls == second_calls == third_calls
    assert first_result == expected_output("192.168.1")


def test_ping_dependency_receives_required_options(tmp_path, monkeypatch):
    calls = []

    def fake_ping(command, **kwargs):
        calls.append((command, kwargs))
        return 1

    monkeypatch.chdir(tmp_path)

    ping_subnet("192.168.1", ping_function=fake_ping)

    assert len(calls) == 253

    command, options = calls[0]

    assert command.endswith("192.168.1.2")
    assert options["shell"] is True
    assert options["stderr"] == subprocess.STDOUT
    assert "stdout" in options
