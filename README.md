# Potato Disease Classification

Farmers who grow potatoes suffer from serious financial standpoint losses each year which cause several diseases that affect potato plants. The diseases Early Blight and Late Blight are the most frequent.

Early blight is caused by fungus and late blight is caused by specific micro-organisms and if farmers detect this disease early and apply appropriate treatment then it can save a lot of waste and prevent economical loss. The treatments for early blight and late blight are a little different so it’s important that you accurately identify what kind of disease is there in that potato plant.

Our Goal is to classify the the type of disease in the potato plant Thus, we have three classes
- Healthy
- Early Blight
- Late Blight

### Install required packages
The required packages are listed in `requirements.txt` file. You can install the required packages using the following command:<br/><br/>
`pip install -r requirements.txt`

### Models and Flask Server

Two models are saved in the `models` directory. Version 2 is more accuracte than version 1. Both the models have the same architecture except for a `RandomContrast` layer which is present in version 2 and not in version 1.

A server is also developed using Flask that has an endpoint. You can send a POST request with an image to that endpoint which sends a response in the following format:
```
{
    "prediction_v1": "<potato-class>",
    "prediction_v2": "<potato-class>"
}
```

An example:
```
{
    "prediction_v1": "Potato___Late_blight",
    "prediction_v2": "Potato___Late_blight"
}
```

## Dataset

All the images are present in the `PlantVillage` folder. The images were downloaded from [Potato Disease Classification Dataset](https://www.kaggle.com/code/amankrpandey1/potato-disease-classification/input) from Kaggle.
