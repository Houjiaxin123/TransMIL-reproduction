# TransMIL: [NeurIPS 2021]

<details>
<summary>
    <b>TransMIL: Transformer based Correlated Multiple Instance Learning for Whole Slide Image Classification</b>. <a href="https://proceedings.neurips.cc/paper/2021/file/10c272d06794d3e5785d5e7c5356e9ff-Paper.pdf" target="blank">[NeurIPS2021]</a>
</summary>

## Data Preprocess

we follow the CLAM's WSI processing solution (https://github.com/mahmoodlab/CLAM)
CLAM预处理，前景背景分割，ResNet50提取patch特征，每张图像保存为一个.pt文件。

## Installation

- Windows 10
- NVIDIA GPU (Tested on a single Nvidia GeForce GTX 1080 Ti)
- Python (3.8.18), h5py (3.10.0), opencv-python (4.2.0.34), PyTorch (2.2.1), torchvision (0.17.1+cu118), pytorch-lightning (1.2.3).

### Train

### Test

## Reference

- If you found our work useful in your research, please consider citing our works(s) at:

```tex

@article{shao2021transmil,
  title={Transmil: Transformer based correlated multiple instance learning for whole slide image classification},
  author={Shao, Zhuchen and Bian, Hao and Chen, Yang and Wang, Yifeng and Zhang, Jian and Ji, Xiangyang and others},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  pages={2136--2147},
  year={2021}
}


```

© This code is made available under the GPLv3 License and is available for non-commercial academic purposes.
