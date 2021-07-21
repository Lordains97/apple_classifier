# apple_classifier
Classification of apple with the dataset given from LuxPM company. This is written as the qualifying test for Lux

#library version required for running
1. numpy - 1.19.5
2. Pillow -  7.1.2
3. Opencv2 - 4.1.2
4. matplotlib - 3.2.2
5. tensorflow - 2.5.0
6. keras - 2.5.0

#Dataset
The dataset folder contains both training data and the validation data that was used during the training of the neural network. Please note that this dataset already has augmented images of the original apple images inorder to balance out the dataset and as for the non-apple images, random images were manually picked from the fruits 360 dataset from the following link below.
"https://www.kaggle.com/moltean/fruits"

#Apple_classifier_model
This jupyter notebook contains the code for creating the model and saving the model as a 'apple_classifier_model.h5' file.

#Model
This folder contains the saved model as well as the python code for testing out the model. Please make that the path to the test folder is mentioned properly for the code to run.
