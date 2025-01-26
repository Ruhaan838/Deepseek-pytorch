from dataclasses import dataclass

@dataclass
class DeepSeekConfig:
    d_model:int = 512
    num_head:int = 8
    d_q:int = 2
    d_kv:int = 4