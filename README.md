# BoostMIS


## 📄 About

This repository contains **code for our paper published in CVPR 2022**:

> **"BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation"**


<div align=center><img height="500" src="imgs/framework.png"></div>

[Article link](https://arxiv.org/abs/2203.02533) _(Published on arxiv: Mar 4, 2022 )_

In this paper, we propose a novel semi-supervised learning (SSL) framework named BoostMIS that combines adaptive pseudo labeling and informative active annotation to unleash the potential of medical image SSL models.

## 🎓 What’s In This Repo



The proposed dataset and framework implementations of our paper are as follows:

## Environment

- Python==3.9
- Pytorch==1.9.1
- Keras==2.2.2

## Dataset Statistic
[**Dataset link**](https://arxiv.org/abs/2203.02533)

## Dataset 
Based on Tensorflow object detection API, we pick Faster R-CNN with Resnet101 architecture pre-trained on COCO dataset to detect region of interest (ROI).



## Run the code
bash train.sh
## 🤝 Referencing and Citing 

If you find our work useful in your research and would like to cite our Radiology paper, please use the following citation:

```
@inproceedings{zhang2022boostmis,
      title={BoostMIS: Boosting Medical Image Semi-supervised Learning with Adaptive Pseudo Labeling and Informative Active Annotation}, 
      author={Zhang, Wenqiao and Zhu, Lei and Hallinan, James and Zhang, Shengyu and Makmur, Andrew  and Cai, Qingpeng and Ooi, Beng Chin},
      booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
      year={2022}
}
```
