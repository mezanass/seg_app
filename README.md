# seg_app

The goal of this project is to train and deploy an image segmentation model, the model is an encoder-decoder that was trained on a dataset of 80 images of the ISEM 2019 class, the images were first segmented manually using [VGG Image Annotator](http://www.robots.ox.ac.uk/~vgg/software/via/) tool that produces a csv [file](https://github.com/mezanass/seg_app/blob/master/training/via_region_data.csv) that contains the coordinates of the various segmentation polygons, using this file a mask was created for every image, since the dataset is kinda small, during the training a data pipeline was setup to apply various transformations to the training images and masks in order to help the model generalize better. a dockerized web app was created to explore various deployment options (tensorflowjs, flask web service, ...).

![Screenshot](screenshot.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The main dependencies you need to install

```
pip install tensorflow
pip install keras
pip install Flask
pip install pymongo
```

### Deployment

Clone the repo

```
git clone https://github.com/mezanass/seg_app.git
cd seg_app/deployment/flask/
```

run without Docker

```
./setup
```

run with Docker

```
./dockerize.sh
```

## Built With

* [Tensorflow](https://www.tensorflow.org/) - Training the model
* [Keras](https://keras.io/) - Training the model
* [Flask](http://flask.pocoo.org/) - The web framework used
* [MongoDB](https://www.mongodb.com/) - The noSQL database used


## Authors

* **Anass Mezroui** - [LinkedIn](https://www.linkedin.com/in/anassmezroui/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Huge thanks to the author of this [notebook](https://colab.research.google.com/github/tensorflow/models/blob/master/samples/outreach/blogs/segmentation_blogpost/image_segmentation.ipynb#scrollTo=l5SZJKPRdXNX) that was a great help
