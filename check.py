import torch

if torch.cuda.is_available():
    print(f"CUDA is available! Using {torch.cuda.device_count()} GPU(s).")
else:
    print("CUDA is not available.")