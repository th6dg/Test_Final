This is my code for classification with MNIST data

+ dataset(mnist) is available in link: https://drive.google.com/drive/u/0/folders/1Pq7fxoOvFWDMlpFBXvIDz7_RasNcOAog - Please download data and put into project
+ file train_eval.py for training loop and evaluate accuracy
+ file predict.py for predicting image in test_dataset
+ folder 'utils' contain some neccessary function like loss function, optimizer, load_data function, class dataset, plot_dataset_function...

How to predict your dataset?
+ easily, first you can put your test_set in folder 'data'
+ second, please change the index in the line 20 (__getitem__ function)
+ third, you can change your model if you want

How to train your custom data?
+ first, you can put your dataset in folder 'data'
+ second, change Path to (val,train)dataset at line 12, 15, 16 in file train_eval.py
+ Third, change Path to test_dataset at line 9 in file predict.py

HOW YOU ENJOY IT!
