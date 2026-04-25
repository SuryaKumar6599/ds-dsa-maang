import torch

#No information leakage from the timestamp in the autoregressive piplines
def causal_masking(seq_len):
    #true means mask this position
    mask = torch.triu(torch.ones(seq_len,seq_len),diagonal = 1).bool()
    #True means block this position
    #False means allow attention
    return mask

# Example usage:
seq_len = 5
mask = causal_masking(seq_len)
print(mask)