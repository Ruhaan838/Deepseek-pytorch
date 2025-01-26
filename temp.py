from model import DeepSeekConfig, Attention

import torch

config = DeepSeekConfig()
model = Attention(config)
a = torch.rand(1, 6, config.d_model)
print(model(a).shape)