# Image-Depth-Estimation-To-Assist-An-Autonomous-Driving-System

Това репо съдържа кодът, използван за разработване и тестване на алгоритмите за извличане на дълбочина и разпознаване на обекти в контекста на автономното шофиране. Този код е използван за изпълнението на експериментите и валидирането на резултатите, представени в дипломната работа.

Кодът е организиран в няколко Python и Python Notebook файлове, всеки от които изпълнява специфични задачи:

- **video_spliter.py**: Отговаря за разделянето на видеото на изображения.
- **train_kitti_road_resnet.ipynb**: Съдържа логиката за обучение на ResNet модела върху KITTI dataset.
- **train_kitti_road_unet.ipynb**: Съдържа логиката за обучение на U-Net модела върху KITTI dataset.
- **train_resnet_custom_dataset.ipynb**: Съдържа логиката за обучение на ResNet модела върху новосъздадения dataset.
- **train_unet_custom_dataset.ipynb**: Съдържа логиката за обучение на U-Net модела върху новосъздадения dataset.
- **MaskRCNN.ipynb**: Включва функционалностите за разпознаване на обекти с Mask R-CNN модел.
- **predict_kitti_resnet_real_images.ipynb**: Съдържа резултатите от прилагане на модела ResNet обучен върху KITTI dataset.
- **predict_kitti_unet_real_images.ipynb**: Съдържа резултатите от прилагане на модела U-Net обучен върху KITTI dataset.
- **predict_resnet_real_images.ipynb**: Съдържа резултатите от прилагане на модела ResNet обучен върху новосъздадения dataset.
- **predict_unet_real_images.ipynb**: Съдържа резултатите от прилагане на модела U-Net обучен върху новосъздадения dataset.


Всеки от обучените модели е запазен в файл с разширение  **.keras**, например **model_kitti_resnet_1716910504.keras**, което предоставя възможност за бъдещо използване на модела. 
Тези .kears могат да бъдат намерени в [модели](https://drive.google.com/drive/folders/1nRc4k3qgn_itWADnP9jY3zcWyxqDGNsR?usp=drive_link).

За да изпълните кода за Mask R-CNN ще са ви необходими тези [файлове](https://drive.google.com/drive/folders/19TxNh0yoyVVxbyYWubaMQJmgvGxrnZs-?usp=drive_link).

Кодът, включен в това репо, предоставя основата за разработването и тестването на алгоритми за автономно шофиране. В бъдеще могат да бъдат направени допълнителни подобрения и разширения, за да се увеличи ефективността и точността на моделите. Този проект има потенциала
да бъде основа за бъдещи изследвания и приложения в областта.
