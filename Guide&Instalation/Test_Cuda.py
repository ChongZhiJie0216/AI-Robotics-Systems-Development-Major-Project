import torch
print("Pytouch Version:",torch.__version__)
print("Cuda Status:",torch.cuda.is_available())
print("Cuda Device:",torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CUDA not available")
