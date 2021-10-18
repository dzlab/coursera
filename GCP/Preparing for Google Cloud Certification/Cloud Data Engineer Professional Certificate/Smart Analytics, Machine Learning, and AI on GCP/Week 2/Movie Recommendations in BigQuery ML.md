# Lab: Movie Recommendations in BigQuery ML

## Overview
BigQuery is Google's fully managed, NoOps, low cost analytics database. With BigQuery you can query terabytes and terabytes of data without having any infrastructure to manage or needing a database administrator. BigQuery uses SQL and can take advantage of the pay-as-you-go model. BigQuery allows you to focus on analyzing data to find meaningful insights.

[BigQuery Machine Learning](https://cloud.google.com/bigquery/docs/bigqueryml-analyst-start) (BigQuery ML) is a feature in BigQuery where data analysts can create, train, evaluate, and predict with machine learning models with minimal coding.

Collaborative filtering provides a way to generate product recommendations for users, or user targeting for products. The starting point is a table with three columns: a user id, an item id, and the rating that the user gave the product. This table can be sparse -- users don’t have to rate all products. Then, based on just the ratings, the technique finds similar users and similar products and determines the rating that a user would give an unseen product. Then, you can recommend the products with the highest predicted ratings to users, or target products at users with the highest predicted ratings.

To illustrate recommender systems in action, you will use the MovieLens dataset. This is a dataset of movie reviews released by GroupLens, a research lab in the Department of Computer Science and Engineering at the University of Minnesota, through funding by the US National Science Foundation.

### Objectives
In this lab, you learn to perform the following tasks:

- Create a BigQuery dataset to store and load MovieLens data
- Explore the MovieLens dataset
- Use a trained model to make recommendations in BigQuery
- Make product predictions for both single users and batch users

## Task 1: Get MovieLens data
In this task you will use the command line to create a BigQuery dataset to store the MovieLens data. The MovieLens data will then be loaded from a Cloud Storage bucket into the dataset.

### Start the Cloud Shell Editor
To create a BigQuery dataset and load the MovieLens data the Cloud Shell is used.

1. In the GCP Console, click Activate Cloud Shell (Cloud Shell).

2. If prompted, click Continue.

### Create and Load BigQuery Dataset
1. Run the following command to create a BigQuery dataset named movies:
```
bq --location=EU mk --dataset movies
```

2. Run the following commands separately in the Cloud Shell:
```
 bq load --source_format=CSV \
 --location=EU \
 --autodetect movies.movielens_ratings \
 gs://dataeng-movielens/ratings.csv
 ```
 ```
 bq load --source_format=CSV \
 --location=EU   \
 --autodetect movies.movielens_movies_raw \
 gs://dataeng-movielens/movies.csv
```

## Task 2: Explore the data
In this task you will explore and verify the MovieLens dataset using Query editor.

1. In BigQuery's Query editor execute the following query:
```sql
SELECT
  COUNT(DISTINCT userId) numUsers,
  COUNT(DISTINCT movieId) numMovies,
  COUNT(*) totalRatings
FROM
  movies.movielens_ratings
```
You should confirm that the dataset consists of over 138 thousand users, nearly 27 thousand movies, and a little more than 20 million ratings.

2. Examine the first few movies using the query:
```sql
SELECT
  *
FROM
  movies.movielens_movies_raw
WHERE
  movieId < 5
```

![image](https://user-images.githubusercontent.com/1645304/137668706-cf6bda22-9bd7-41e9-96b8-544496649497.png)


3. You can see that the genres column is a formatted string. Parse the genres into an array and rewrite the results into a table named `movielens_movies`.
```sql
CREATE OR REPLACE TABLE
  movies.movielens_movies AS
SELECT
  * REPLACE(SPLIT(genres, "|") AS genres)
FROM
  movies.movielens_movies_raw
```

Feel free to perform additional queries until you are comfortable with the dataset.

## Task 3: Evaluate a trained model created using collaborative filtering
In this task you will view the metrics for a trained model which was generated using matrix factorization.

Matrix factorization is a collaborative filtering technique that relies on two vectors called the user factors and the item factors. The user factors is a low-dimensional representation of a user_id and the item factors similarly represents an item_id.

To perform a matrix factorization of our data, you use the typical BigQuery ML syntax except that the model_type is matrix_factorization and you have to identify which columns play what roles in the collaborative filtering setup.

In order to apply matrix factorization to the movie ratings data, the BigQuery ML query needs to be executed to create the model. However, creation of this model type can take up to 40 minutes and requires a Google Cloud project with reservation-oriented resources -- which is unlike those offered by the Qwiklabs environment.

A model has been created in the Cloud Training project's **cloud-training-prod-bucket** BigQuery dataset for use in the rest of the lab.

**NOTE:** The query below is for reference only. Please **DO NOT EXECUTE** this query in your project.

> CREATE OR REPLACE MODEL movies.movie_recommender

> OPTIONS (model_type='matrix_factorization', user_col='userId', item_col='movieId', rating_col='rating', l2_reg=0.2, num_factors=16) AS

> SELECT userId, movieId, rating

> FROM movies.movielens_ratings

Note, the num_factors and l2_reg options have been selected after much experimentation to speed up training of the model.

1. To view metrics for the trained model, run the following query:
```sql
SELECT * FROM ML.EVALUATE(MODEL `cloud-training-prod-bucket.movies.movie_recommender`)
```

## Task 4: Make Recommendations
In this task you will use the trained model to provide recommendations.

1. Let’s find the best comedy movies to recommend to the user whose userId is 903. Enter the query below:
```sql
SELECT
  *
FROM
  ML.PREDICT(MODEL `cloud-training-prod-bucket.movies.movie_recommender`,
    (
    SELECT
      movieId,
      title,
      903 AS userId
    FROM
      `movies.movielens_movies`,
      UNNEST(genres) g
    WHERE
      g = 'Comedy' ))
ORDER BY
  predicted_rating DESC
LIMIT
  5  
```

![image](https://user-images.githubusercontent.com/1645304/137668949-292becf0-3a12-481c-8fcb-fdcd8559744d.png)

2. This result includes movies the user has already seen and rated in the past. Let’s remove them:
```sql
SELECT
  *
FROM
  ML.PREDICT(MODEL `cloud-training-prod-bucket.movies.movie_recommender`,
    (
    WITH
      seen AS (
      SELECT
        ARRAY_AGG(movieId) AS movies
      FROM
        movies.movielens_ratings
      WHERE
        userId = 903 )
    SELECT
      movieId,
      title,
      903 AS userId
    FROM
      movies.movielens_movies,
      UNNEST(genres) g,
      seen
    WHERE
      g = 'Comedy'
      AND movieId NOT IN UNNEST(seen.movies) ))
ORDER BY
  predicted_rating DESC
LIMIT
  5
```

For this user, this happens to yield the same set of movies -- the top predicted ratings didn’t include any of the movies the user has already seen.

## Task 5:Apply customer targeting
In this task you will look at how to identify the top-rated movies for a specific user. Sometimes, you have a product and have to find the customers who are likely to appreciate it.

1. You wish to get more reviews for movieId=96481 which has only one rating and you wish to send coupons to the 100 users who are likely to rate it the highest. Identify those users using:
```sql
SELECT
  *
FROM
  ML.PREDICT(MODEL `cloud-training-prod-bucket.movies.movie_recommender`,
    (
    WITH
      allUsers AS (
      SELECT
        DISTINCT userId
      FROM
        movies.movielens_ratings )
    SELECT
      96481 AS movieId,
      (
      SELECT
        title
      FROM
        movies.movielens_movies
      WHERE
        movieId=96481) title,
      userId
    FROM
      allUsers ))
ORDER BY
  predicted_rating DESC
LIMIT
  100
```

The result gives us 100 users to target, the top 5 of whom are:

![image](https://user-images.githubusercontent.com/1645304/137669023-babc1bdb-c000-4e90-8f44-9bab9be0283e.png)

## Task 6: Perform Batch predictions for all users and movies
In this task you will perform a query to obtain batch predictions for users and movies.

What if you wish to carry out predictions for every user and movie combination? Instead of having to pull distinct users and movies as in the previous query, a convenience function is provided to carry out batch predictions for all movieId and userId encountered during training.

1. Enter the following query to obtain batch predictions:
```sql
SELECT
  *
FROM
  ML.RECOMMEND(MODEL `cloud-training-prod-bucket.movies.movie_recommender`)
LIMIT 
  100000
```

Without the LIMIT command the results would be too large to return given the default settings. But the output provides you a sense of the type of predictions that can be made with this model.

As seen in a section above, it is possible to filter out movies the user has already seen and rated in the past. The reason already seen movies aren’t filtered out by default is that there are situations (think of restaurant recommendations, for example) where it is perfectly expected that you would need to recommend restaurants the user has liked in the past.

