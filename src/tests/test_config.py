from ..config import Config
import os

def test_config_values():
    config = Config()
    assert config.description_engine == 'gpt-4o-2024-05-13'
    assert config.summary_engine == 'gpt-4o-2024-05-13'
    assert config.max_tokens == 4096
