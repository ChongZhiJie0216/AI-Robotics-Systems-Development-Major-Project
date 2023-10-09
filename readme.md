# Anaconda Env Install

```bash
conda create --name ultralytics-env python=3.8 -y
conda activate ultralytics-env
conda install -c conda-forge opencv
conda install -c "conda-forge/label/broken" opencv -y
conda install -c "conda-forge/label/cf201901" opencv -y
conda install -c "conda-forge/label/cf202003" opencv -y
conda install -c "conda-forge/label/gcc7" opencv -y
conda install -c michael_wild opencv-contrib -y
conda install -c conda-forge ultralytics -y
conda install -c anaconda numpy -y
conda install spyder-kernels=2.4
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=ultralytics-env
```
