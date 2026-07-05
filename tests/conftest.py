"""Test configuration for Cloud Cost Optimization Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cloud-cost-optimization-agent", "category": "DevOps & Platform Engineering"}
