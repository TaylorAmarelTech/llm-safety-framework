"""
Pydantic models for the spinning pipeline.
"""

from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

from pydantic import BaseModel, Field


class SpinType(str, Enum):
    SPINTAX = "spintax"
    REGEX = "regex"
    CHAR_PADDING = "char_padding"
    LLM_REPHRASE = "llm_rephrase"
    ATTACK_AUGMENT = "attack_augment"
    CUSTOM = "custom"
    ENCODE = "encode"
    OBFUSCATE = "obfuscate"
    JAILBREAK_WRAP = "jailbreak_wrap"


class SpinConfig(BaseModel):
    """Configuration for a spinning operation."""
    spin_type: SpinType
    save_to_pipeline: bool = True
    # Spintax
    template: Optional[str] = None
    count: int = 10
    # Regex
    patterns: List[Dict[str, str]] = Field(default_factory=list)
    # Char padding
    padding_chars: str = " "
    padding_count: int = 0
    trailing_chars: str = ""
    insert_zero_width: bool = False
    # LLM rephrase
    model_id: Optional[str] = None
    rephrase_instructions: str = "Rephrase this prompt while preserving the original intent and meaning."
    count_per_prompt: int = 3
    temperature: float = 0.9
    # Attack augment
    strategies: List[str] = Field(default_factory=list)
    # Custom
    prefix: str = ""
    suffix: str = ""
    find_replace: List[Dict[str, str]] = Field(default_factory=list)


class SpinJob(BaseModel):
    """A completed spin job with results."""
    id: str
    type: SpinType
    created_at: datetime = Field(default_factory=datetime.now)
    config: Dict[str, Any] = Field(default_factory=dict)
    prompts: List[str] = Field(default_factory=list)
    details: Optional[List[Dict[str, Any]]] = None

    @property
    def count(self) -> int:
        return len(self.prompts)


class SpinResult(BaseModel):
    """Result of a spinning operation."""
    job_id: str
    count: int
    prompts: List[str]
    saved: bool
    details: Optional[List[Dict[str, Any]]] = None


class PipelineSource(BaseModel):
    """A source contributing prompts to the pipeline."""
    type: str  # "set", "imported", "spun"
    id: str
    count: int


class PipelinePrompt(BaseModel):
    """A single prompt in the pipeline."""
    text: str
    source: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ActivePipeline(BaseModel):
    """The active pipeline ready for testing."""
    built_at: datetime = Field(default_factory=datetime.now)
    sources: List[PipelineSource] = Field(default_factory=list)
    total: int = 0
    prompts: List[PipelinePrompt] = Field(default_factory=list)
