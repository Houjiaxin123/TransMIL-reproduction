# TransMIL: [NeurIPS 2021]

## Data Preprocess

we follow the CLAM's WSI processing solution (https://github.com/mahmoodlab/CLAM)

- CLAM预处理，前景背景分割，ResNet50提取patch特征，每张图像保存为一个.pt文件。
- 利用生成的csv列表，训练集随机划分5折（训练集和验证集），测试集固定不变，保存划分结果至dataset_csv/camelyon16。

## Installation

- Windows 10
- NVIDIA GPU (Tested on a single Nvidia GeForce GTX 1080 Ti)
- Python (3.8.18), h5py (3.10.0), opencv-python (4.2.0.34), PyTorch (2.2.1), torchvision (0.17.1+cu118), pytorch-lightning (1.2.3).

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

## Modification
修改：
models/model_interface.py
- 1.class ModelInterface中def __init__，调用trochmetrics计算指标，添加参数task = 'multiclass'或task = 'binary'.
- 2.def test_epoch_end,修改为auc = self.AUROC(max_probs, target.squeeze())
- 3.环境中不需要omegaconf 2.2.3。

## Results
数据直接用CLAM预处理，无其他操作，camelyon16结果。    

| fold | test_BinaryAccuracy | test_BinaryCohenKappa | test_BinaryF1Score | test_BinaryRecall | test_BinaryPrecision | auc | 
| :-----:| :----: | :----: | :----: | :----: | :----: | :----: |
| 0 | 0.822 | 0.587 | 0.701 | 0.551 | 0.964 | 0.769 |
| 1 | 0.845 | 0.663 | 0.783 | 0.735 | 0.837 | 0.824 |
| 2 | 0.806 | 0.566 | 0.706 | 0.612 | 0.833 | 0.769 |
| 3 | 0.798 | 0.555 | 0.705 | 0.633 | 0.795 | 0.766 |
| 4 | 0.853 | 0.673 | 0.782 | 0.694 | 0.895 | 0.822 |
| ave | 0.825 | 0.609 | 0.735 | 0.645 | 0.865 | 0.790 |

