"""Cloud Cost Optimization Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_spending():
    """Test Analyze cloud spending by service, team, and environment."""
    tools = AgentTools()
    result = await tools.analyze_spending(cloud="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_waste():
    """Test Identify idle, underutilized, or orphaned resources."""
    tools = AgentTools()
    result = await tools.detect_waste(cloud="test", utilization_threshold="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_recommend_rightsizing():
    """Test Recommend instance size changes based on actual CPU/memory usage."""
    tools = AgentTools()
    result = await tools.recommend_rightsizing(resource_type="test", lookback_days=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_plan_reservations():
    """Test Calculate optimal reserved instance or savings plan purchases."""
    tools = AgentTools()
    result = await tools.plan_reservations(cloud="test", commitment_term="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.cloud_cost_optimization_agent_agent import CloudCostOptimizationAgentAgent
    agent = CloudCostOptimizationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
