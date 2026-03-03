"""
Tests for the integration adapters (garak, pyrit, deepteam).
"""

import pytest

from src.integrations.detector import detect_all
from src.integrations.garak_adapter import GarakAdapter
from src.integrations.pyrit_adapter import PyRITAdapter
from src.integrations.deepteam_adapter import DeepTeamAdapter


class TestDetector:
    def test_detect_all_returns_all_libraries(self):
        result = detect_all()
        assert "garak" in result
        assert "pyrit" in result
        assert "deepteam" in result

    def test_detect_all_structure(self):
        result = detect_all()
        for lib_name, info in result.items():
            assert "installed" in info
            assert isinstance(info["installed"], bool)
            assert "method_count" in info
            assert isinstance(info["method_count"], int)
            assert "pip_install" in info
            assert isinstance(info["pip_install"], str)


class TestGarakAdapter:
    def test_is_available(self):
        result = GarakAdapter.is_available()
        assert isinstance(result, bool)

    def test_get_info(self):
        info = GarakAdapter.get_info()
        assert "installed" in info
        # When not installed, only has "installed" key
        if info["installed"]:
            assert "version" in info

    def test_list_probes(self):
        probes = GarakAdapter.list_probes()
        assert isinstance(probes, list)


class TestPyRITAdapter:
    def test_is_available(self):
        result = PyRITAdapter.is_available()
        assert isinstance(result, bool)

    def test_get_info(self):
        info = PyRITAdapter.get_info()
        assert "installed" in info

    def test_list_converters(self):
        converters = PyRITAdapter.list_converters()
        assert isinstance(converters, list)
        assert len(converters) > 0
        for c in converters:
            assert "id" in c
            assert "name" in c
            assert "description" in c

    def test_known_converters_count(self):
        converters = PyRITAdapter.list_converters()
        assert len(converters) >= 8


class TestDeepTeamAdapter:
    def test_is_available(self):
        result = DeepTeamAdapter.is_available()
        assert isinstance(result, bool)

    def test_get_info(self):
        info = DeepTeamAdapter.get_info()
        assert "installed" in info

    def test_list_methods(self):
        methods = DeepTeamAdapter.list_methods()
        assert isinstance(methods, list)
        assert len(methods) > 0
        for m in methods:
            assert "id" in m
            assert "name" in m
            assert "type" in m

    def test_known_methods_count(self):
        methods = DeepTeamAdapter.list_methods()
        assert len(methods) >= 16

    def test_method_types(self):
        methods = DeepTeamAdapter.list_methods()
        types = {m["type"] for m in methods}
        assert "vulnerability" in types
        # Attack types can be "single" or "multi"

    def test_list_vulnerabilities(self):
        vulns = DeepTeamAdapter.list_vulnerabilities()
        assert isinstance(vulns, list)
        assert len(vulns) >= 10

    def test_list_attacks(self):
        attacks = DeepTeamAdapter.list_attacks()
        assert isinstance(attacks, list)
        assert len(attacks) >= 6
