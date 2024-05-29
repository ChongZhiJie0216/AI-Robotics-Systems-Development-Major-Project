import torch

if torch.cuda.is_available():
    print("Pytouch Version:",torch.__version__)
    print("Cuda Status:",torch.cuda.is_available())
    print("CUDA version:", torch.version.cuda)
    num_cuda_devices = torch.cuda.device_count()
    print("Number of CUDA devices available:", num_cuda_devices)
else:
    print("CUDA is not available.")
