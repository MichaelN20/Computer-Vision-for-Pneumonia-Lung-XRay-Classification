# **Computer Vision for Pneumonia Lung X-Ray Classification**

### **Dataset Information:**

This dataset consists of chest X-ray images of children collected at the Guangzhou Women and Children's Medical Center, Guangzhou, China. The dataset includes a total of 5,863 X-ray images in JPEG format, categorized into two classes: Pneumonia and Normal. These images have been used to develop an artificial intelligence system for chest X-ray analysis.

### **Objective:**

The goal of this project is to develop a computer model capable of classifying whether someone is suffering from Pneumonia or not, based on the results of patients' lung X-rays. The approach applied in creating this model is the concept of Computer Vision, with the implementation of an Artificial Neural Network architecture to understand the complex relationship between chest X-ray images and the presence of Pneumonia. The basic principle of this project involves training the model to recognize patterns and features in X-ray images that indicate the presence of Pneumonia. Thus, the project is essential in applying artificial intelligence technology in the field of medical diagnostics.

### **Problem:**

Create a computer model that can classify whether someone is suffering from Pneumonia or not based on the results of patients' lung X-rays.

### **Tools:**
- **Data Handling:** `os` (Operating System), `glob` (File path pattern matching), `numpy` (Numerical operations), `pandas` (Data manipulation)
- **Image Processing:** `PIL` (Python Imaging Library), `ImageDataGenerator` (Data augmentation for images), `ResNet50` (Pre-trained Convolutional Neural Network)
- **Machine Learning Models:** `Sequential`, `Conv2D`, `MaxPooling2D`, `Flatten`, `GlobalAveragePooling2D`, `Dense`, `Dropout` (for building and training neural networks)
- **Optimizers:** `optimizers` (Optimization algorithms for model training)
- **Model Saving/Loading:** `save_model`, `load_model` (for saving and loading machine learning models)
- **Data Visualization:** `matplotlib.pyplot`, `seaborn` (for creating plots and visualizations)
- **Data Preprocessing:** `ImageDataGenerator` (for augmenting image data), `StandardScaler`, `LabelEncoder`, `OneHotEncoder`, `OrdinalEncoder` (for preparing data)
- **Metrics and Evaluation:** `confusion_matrix`, `classification_report` (for assessing model performance)
- **Callbacks:** `EarlyStopping`, `ReduceLROnPlateau`, `ModelCheckpoint` (for controlling model training)
- **Other Libraries:** `tensorflow`, `keras` (Deep learning libraries)