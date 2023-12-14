# **Computer Vision for Pneumonia Lung X-Ray Classification**

### **Dataset Information:**

This dataset consists of chest X-ray images of children collected at the Guangzhou Women and Children's Medical Center, Guangzhou, China. The dataset includes a total of 5,863 X-ray images in JPEG format, categorized into two classes: Pneumonia and Normal. These images have been used to develop an artificial intelligence system for chest X-ray analysis.

### **Objective:**

The goal of this project is to develop a computer model capable of classifying whether someone is suffering from Pneumonia or not, based on the results of patients' lung X-rays. The approach applied in creating this model is the concept of Computer Vision, with the implementation of an Artificial Neural Network architecture to understand the complex relationship between chest X-ray images and the presence of Pneumonia. The basic principle of this project involves training the model to recognize patterns and features in X-ray images that indicate the presence of Pneumonia. Thus, the project is essential in applying artificial intelligence technology in the field of medical diagnostics.

### **Problem:**

Create a computer model that can classify whether someone is suffering from Pneumonia or not based on the results of patients' lung X-rays.

### **Tools:**
- **Data Retrieval:** `os` (Operating System Interface), `glob` (Pattern matching on file paths), `numpy` (Numerical operations), `pandas` (Data manipulation library), `tensorflow` (Machine learning library), `matplotlib` (Plotting library), `seaborn` (Statistical data visualization)
- **Image Processing:** `PIL` (Python Imaging Library), `ImageDataGenerator` (Data augmentation for image data), `ResNet50` (Pre-trained Convolutional Neural Network model)
- **Model Building:** `Sequential` (Linear stack of layers for building neural networks), `Conv2D` (Convolutional layer), `MaxPooling2D` (Max pooling layer), `Flatten` (Flattens the input), `GlobalAveragePooling2D` (Global average pooling operation), `Dense` (Fully connected layer), `Dropout` (Dropout layer)
- **Optimizers:** `optimizers` (Optimization algorithms for training models)
- **Model Training:** `EarlyStopping` (Stop training when a monitored metric has stopped improving), `ReduceLROnPlateau` (Reduce learning rate when a metric has stopped improving), `ModelCheckpoint` (Save the model after every epoch)
- **Model Saving/Loading:** `save_model` (Save the model to disk), `load_model` (Load a saved model from disk)
- **Data Augmentation:** `ImageDataGenerator` (Generate augmented data for training)
- **Evaluation Metrics:** `confusion_matrix` (Compute confusion matrix), `classification_report` (Build a text report showing the main classification metrics)
- **Other Libraries:** `keras` (Deep learning library), `scikit-learn` (Machine learning library)