import torch

if torch.cuda.is_available():
    device = 'cuda'
    print(f'Num GPUs Available: {torch.cuda.device_count()}')
else:
    device = 'cpu'

COMPUTE_DEVICE = torch.device(device)
COMPUTE_DEVICE_CPU = torch.device('cpu')
# COMPUTE_DEVICE = COMPUTE_DEVICE_CPU
