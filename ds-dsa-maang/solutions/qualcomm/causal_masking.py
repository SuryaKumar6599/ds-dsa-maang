import torch
import torch.nn as nn
import torch.nn.functional as F

def get_causal_mask(seq_len: int) -> torch.Tensor:
    # Creates upper triangular matrix with 1s above diagonal
    # True values mask out (ignore) positions where j > i
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
    return mask

# Usage in Transformer
class DecoderBlock(nn.Module):
    def __init__(self, d_model: int, nhead: int):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(d_model, nhead)
        
    def forward(self, x: torch.Tensor):
        seq_len = x.size(0)
        mask = get_causal_mask(seq_len)
        # attn_mask=True means ignore that position
        out, _ = self.self_attn(x, x, x, attn_mask=mask)
        return out