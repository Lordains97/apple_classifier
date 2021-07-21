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
The dataset folder contains both training data and the validation data that was used during the training of the neural network.

1. valid-datavalid_apple-20210721T050130Z-001.zip -- validation dataset
2. dataset-20210721T050154Z-001                   -- training images dataset

Please note that this dataset already has augmented images of the original apple images inorder to balance out the dataset and as for the non-apple images, random images were manually picked from the fruits 360 dataset from the following link below.
"https://www.kaggle.com/moltean/fruits"

#Apple_classifier_model
This jupyter notebook contains the code for creating the model and saving the model under the folder 'apple_classification_model'. The jupyter notebook explains the code via commented lines. The notebook also has means of testing the image directly.

#apple_classifier_test
This python file is used for testing the saved model. there are two things that are needed to be done properly.

1. the location of the folder 'apple_classification_model' must be mentioned correctly in the code (the code contains my local system location)
2. The location to the test folder that contains the testing images should be mentioned properly

On running the python code, the images present in the test file automatically gets predicted and the prediction for each image present in the testing folder is printed along with the name of the file.
