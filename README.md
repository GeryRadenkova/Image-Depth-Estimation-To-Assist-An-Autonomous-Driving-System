# Image-Depth-Estimation-To-Assist-An-Autonomous-Driving-System

<p>This repository contains the code used for developing and testing the algorithms for depth estimation and object recognition in the context of autonomous driving. This code was used for conducting the experiments and validating the results presented in the thesis.</p>

The code is organized into several Python and Python Notebook files, each performing specific tasks:

- **video_spliter.py**: Splitting the video into images.
- **train_kitti_road_resnet.ipynb**: Contains the logic for training the ResNet model on the KITTI dataset.
- **train_kitti_road_unet.ipynb**: Contains the logic for training the U-Net model on the KITTI dataset.
- **train_resnet_custom_dataset.ipynb**: Contains the logic for training the ResNet model on the newly created dataset.
- **train_unet_custom_dataset.ipynb**: Contains the logic for training the U-Net model on the newly created dataset.
- **MaskRCNN.ipynb**: Includes functionalities for object recognition using the Mask R-CNN model.
- **predict_kitti_resnet_real_images.ipynb**: Contains the results of applying the ResNet model trained on the KITTI dataset.
- **predict_kitti_unet_real_images.ipynb**: Contains the results of applying the U-Net model trained on the KITTI dataset.
- **predict_resnet_real_images.ipynb**: Contains the results of applying the ResNet model trained on the newly created dataset.
- **predict_unet_real_images.ipynb**: Contains the results of applying the U-Net model trained on the newly created dataset.


Each of the trained models is saved in a file with the **.keras** extension, such as **model_kitti_resnet_1716910504.keras**, which provides the opportunity for future use of the model. 
This .kears files can be found in [models](https://drive.google.com/drive/folders/1nRc4k3qgn_itWADnP9jY3zcWyxqDGNsR?usp=drive_link)

To run the code for Mask R-CNN you need this [files](https://drive.google.com/drive/folders/19TxNh0yoyVVxbyYWubaMQJmgvGxrnZs-?usp=drive_link).

The code included in this appendix provides the foundation for the development and testing of algorithms for autonomous driving. Additional improvements and extensions can be made in the future to increase the efficiency and accuracy of the models. This project has the potential to serve as a basis for future research and applications in the field.
