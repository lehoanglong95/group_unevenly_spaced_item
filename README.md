# Predict the Correct Grouping of Unevenly Spaced
![Before Grouping](https://iili.io/JW21rAJ.png)
![After Grouping](https://iili.io/JW21e6P.png)

## Background

In the design-to-code process, one of the initial steps involves "fixing" the design to ensure adherence to certain best practices, enabling accurate and correct code generation.

A crucial aspect of this process is grouping elements together to facilitate correct conversion into responsive flex layouts. This step is essential because modern webpages are expected to be responsive and visually appealing across various screen sizes.

## Problem

The task at hand is to predict the correct grouping of elements given an array of items and spaces in either the x or y direction.

The input consists of an array representing items and spaces along with their respective sizes, structured as follows:

```bash
input: [[a,4], [0,2], [b,5], [0,3], [c,5], [d,4]]
```

Here, the first element of each sub-array represents the item ID (e.g., a, b, c, d, or 0 for a space), and the second element denotes the size (height if in the y-direction, width if in the x-direction).

The expected output is an array of grouped elements, like so:
```bash
output: [[a,b], c, d]
```

## Installation

To run the project locally, execute the following commands:

```bash
docker build -t group_unevenly_spaced_item .
docker run -p 3000:3000 -it group_unevenly_spaced_item
```

## Overview of Solutions

- Calculate the distance from each element in the input with left alignment.
- Calculate the different distances of each pair in the input, named `diff_distance`.
- Calculate the different sizes of each pair in the input, named `diff_size`.
- Generate each pair to determine whether they belong to the same group in the output. The output has values 0 (not in the same group) and 1 (in the same group), known as `is_same_group`. For example:
   - Input: [[a, b], c]
   - Output: [[a, b, 1], [a, c, 0], [b, c, 0]]
- Divide data into two categories: horizontal and vertical.
- Plot scatter `diff_distance`, `diff_size`, and `is_same_group` for each category to use two features to determine if two elements are in the same group.
- Split data into train and test sets. Use a decision tree classifier to train the model and test it on the test set.
- Horizontal model performance on the test set:
   - Accuracy: 0.97
   - Recall: 0.96
   - F1 Score: 0.95
- Vertical model performance on test set:
   - Accuracy: 0.97
   - Recall: 0.94
   - F1 Score: 0.96
- Use pretrained models for predicting input in API.
- All plots and model training are found in `data_analyst/data_analysis.ipynb`.
- Pretrained models are found in:
   - `data_analyst/horizontal_decision_tree_model.pkl`
   - `data_analyst/vertical_decision_tree_model.pkl`


## Code Structure

- `/data`: JSON data of assignment.
- `/data_analyst`: Analysis of data and model training.
- `/src`: Source code for backend.
- `/utils`: Functions for preprocessing data.

The backend code is structured following CLEAN architecture:
- `/api`: Handlers for API.
- `/domain`: Main business logic of the backend code. Each business logic is handled by a use case, and all elements communicate via an interface.
- `/infrastructure`: Implement interfaces from domain.

## Further Improvements

### ML/AI

1. Find additional features from raw data (feature engineering) to enhance the model's classification.
2. Try other classifiers. Experiment with 5 to 10 models and choose the best, or use an ensemble of models with weighted predictions.
3. Experiment with K-means as an alternative approach.
4. Consider building separate models for each website (e.g., Airbnb, Retool, Uber, Wego) due to differing data distributions. While this could improve performance, scalability might be a concern when adding more websites.

### Backend

1. Save user requests to a database and allow users to provide feedback on the AI predictions for potential retraining of the model.
2. Implement caching for faster responses instead of repetitive model predictions.
3. Use a singleton pattern to load the model instead of reinitializing it for each new request.
4. Implement versioning for the model to facilitate API versioning.

# 🐉 About Me

## Hi, I'm Long - A Data Analyst! 💻

## Author

- [@Long H Le](https://github.com/lehoanglong95)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://long-hoang-le.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/long-le-713b41111/)