
# Task Requirements

## Data Collection

- Obtain the data independently.
  - **Note**: Do not use Kaggle or any other external sources.
- Ensure the dataset contains at least 10,000 rows.

---

## Part 1: Clustering

### Objective

Perform clustering on data based on sequences. These sequences can vary in length. The goal is to identify patterns within the sequences.

#### Examples

- **Travel Routes**: If you consider data of travel routes for different people sampled every minute, you'll find some people have shorter routes while others have longer ones. The objective is to cluster similar travel patterns.
- **HTTP Requests**: Analyzing HTTP requests between different services in an application can result in sequences. For instance, some requests might reach the web server and then be sent to the database. Others might be routed to different services. Clustering these sequences, which can vary in length, can reveal primary transaction patterns in the sampled application.
- **Recipe Instructions**: Here, a sequence is defined by the actions or steps needed to prepare a dish. Many recipes might have similar sequences of instructions. Clustering these sequences can uncover patterns in the preparation methods for different types of food.

### Tasks

1. Use at least 3 different clustering methods and compare their results.
2. Design various test scenarios to evaluate the clustering results.
3. Display the outcomes of these tests using graphical representations.

---

## Part 2: Time Series Prediction

### Objective

Predict the next sequence in the dataset using time series forecasting techniques.

### Tasks

1. Implement time series prediction to estimate the subsequent sequence in your data.
2. Ensure the dataset used here is different from the one used in Part 1.

## Note

For all the models you implement, ensure you choose different hyperparameters. Provide explanations for your choices.

--- 

