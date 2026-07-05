"""Cloud Cost Optimization Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class CostAnalysis(BaseModel):
    """CostAnalysis for Cloud Cost Optimization Agent."""
    total_spend: float
    period: str
    breakdown: list[dict]
    trend: str
    anomalies: list[dict]


class WasteReport(BaseModel):
    """WasteReport for Cloud Cost Optimization Agent."""
    total_waste: float
    idle_resources: list[dict]
    oversized_resources: list[dict]
    orphaned_resources: list[dict]


class RightsizingRecommendation(BaseModel):
    """RightsizingRecommendation for Cloud Cost Optimization Agent."""
    resource_id: str
    current_size: str
    recommended_size: str
    monthly_savings: float
    risk: str

