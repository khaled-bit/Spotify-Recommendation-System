# Spotify-Recommendation-System
- We will have 3 tasks to finish our Spotify Recommendation System Project with deploying it <br>
- Tasks:
    - Task1: Feature Engineering
    - Task2: Building ML Model
    - Task3: Deploying ML Model
<hr>
<center> <h1> Task 1: Feature Engineering</h1> </center>

<hr>

## Task Details 
- Deadline Date: 9/14/2022 <br>
- Deadline Time: 9:00 AM EG, 12:30 AM IST

- Dataset Link:
    - https://drive.google.com/file/d/1QB1suGX6SiyJpDZ9afpnfoRYJTwPyQMQ/view?usp=sharing

- You are required to add at minimum two modifications to the feature engineering of this dataset
    - Feel free to check your notebook regarding this task and add any modification which was not done in this example notebook
    - Feel free to contact your team leader if you want to ask about anything

- Recommendations
    - You may use `boxcox technique` to handle the skewness of the numerical data (but remember it only accepts positive data)
    - You may use `PCA technique` in different manner rather than dimensionality reduction
    - You may use different way than `correlation technique` to get the best features from the dataset
    - You may use `one hot encoding technique` regarding categorical features (yes, no) rather than (1, 0)
    - You may use one/many of the `object` columns and convert them into category `int` using `label encoding technique`

- Helping Materials
    - Feature Engineering Article
        - https://www.analyticsvidhya.com/blog/2021/03/step-by-step-process-of-feature-engineering-for-machine-learning-algorithms-in-data-science/
    - PCA Article
        - https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html
    - Handle Skewed Data Article
        - https://medium.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Ftop-3-methods-for-handling-skewed-data-1334e0debf45

<center> <strong> Feel free to make any other recommendation that is not mentioned here, that will improve your data features. </strong> </center> <br>

<center> Wish you the best of luck. </center>
<hr>

Down here is an example notebook in which you have to modify your changes upon it:<br>
<a href="Task1_FeatureEngineering.ipynb"> Task1: Feature Engineering Notebook</a>
<hr>
<a href="Task1_ModelAnswer.ipynb"> Task 1 Model Answer Notebook</a>
<hr>

<center> <h1> Task 2: Spotify Collaborative Filtering Model Building</h1> </center>

<hr>

## Task Details 
- Deadline Date: 9/16/2022 <br>
- Deadline Time: 11:59 PM EG, 03:30 AM IST

- Dataset:
    - There are two datasets and we will try to train our model on both and then check the accuracy and compare
        - This is supposed to be made to gain visualization about the importance of PCA
        - The datsets are `model_normal_dataset.csv` and `model_pca_dataset.csv` 
    - Link
        - https://drive.google.com/drive/folders/104scYexDFCHGSWE8pw3sXTmieWwZZUpH?usp=sharing

We are going to build Recommendation System using `Collaborative Filtering` 

- Helping Materials
    - Introduction to different recommendation systems
        - <a href="https://www.youtube.com/watch?v=SEkIy7V8Lks"> How Does Spotify Recommend Music?  </a>
        - <a href="https://www.datacamp.com/tutorial/recommender-systems-python"> Beginner Tutorial: Recommender Systems in Python </a>
        - <a href="https://www.cambridgespark.com/info/practical-introduction-to-recommender-systems"> Practical Introduction to Recommender Systems</a>
        
    - Mathematics beyond Collaborative Filtering
        - <a href="https://www.youtube.com/watch?v=giIXNoiqO_U&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=96"> Andrew Course Lec 16, <strong> Watch from Video 16.1 to 16.6</strong></a><br>
        - <a href="https://www.youtube.com/watch?v=WlJLGTMGC_A&list=PL6-3IRz2XF5UnONA8-ENhR0NE04mIllqB&index=14"> Hesham Assem Video 1, <strong> Special Arabic Content</strong></a>
        - <a href="https://www.youtube.com/watch?v=wxQdtPT5-2Q&list=PL6-3IRz2XF5UnONA8-ENhR0NE04mIllqB&index=15"> Hesham Assem Video 2, <strong> Special Arabic Content</strong></a>
        - <a href="https://www.youtube.com/watch?v=8_VEwRMkvRg&list=PL6-3IRz2XF5UnONA8-ENhR0NE04mIllqB&index=16"> Hesham Assem Video 3, <strong> Special Arabic Content</strong></a>
        - <a href="https://www.youtube.com/watch?v=4L4TT3-nic4"> Moataz Saad Video 1, <strong> Special Arabic Content</strong></a><br>

    - Collaborative Filtering Recommendation System
        - <a href="https://us.hidester.com/proxy.php?u=eJwBcwCM%2F3M6MTA2OiInFvvbiGSaE2J0oipuRxoF6UoMOo1uOiE7jjUqFMPj4bgntMII4bTRqHMHsINbz337b65C1Lg4PDui873dxaZmE0%2BwOEDiBaFYEtgtNHAkIYOzPWVKR9AwOZ9Al4w1SudwBRBQ4wNhUrjMIjsL8DFs&b=7"> Various Implementations of Collaborative Filtering </a>
        - <a href="https://www.slideshare.net/erikbern/collaborative-filtering-at-spotify-16182818"> Collaborative Filtering at Spotify </a>
        - <a href="https://hackernoon.com/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe"> Spotify’s Discover Weekly: How machine learning finds your new music </a>
        
    - Spotify Playlist Recommendation System GitHub Repo 
        - <a href="https://github.com/wsmiles000/CS109a-Spotify-Recommendation#conclusions-&-summary"> GitHub Repo </a>    

<center> <strong> Feel free to study any other materials which is not mentioned up here, that will make you understand the content well </strong> </center> 

<center> <strong> Please start studying immediately as STUDY WILL TAKE TIME </strong> </center> <br>

<center> Wish you best of luck </center>
<hr>
<center> <h1> Task 3: Build Basic Website </h1> </center>
<hr>

## Task Details 
- Deadline Date: 9/22/2022 <br>
- Deadline Time: 11:59 PM EG, 03:30 AM IST (9/23/2022)

- You are supposed to build a website using <a href = "https://streamlit.io/" > Streamlit </a>
- The website should contain of minimum one page with:
    - Welcome Title and description of what our website does 
    - Input box where I input the name of the song
    - Output Table where I can control how many rows it should display
    - The output table should contain the track's 
        - Name
        - Album
        - Track Uri
    - Footer which wrote in it, your credit as name, etc.
    - Just do the task with no ML Model explained, just make the user interface and functionalities
    - A BONUS for designing the best user interface
    - Helping Materials:
        - Streamlit Crash Course
            - https://www.youtube.com/watch?v=_9WiB2PDO7k&t=2105s
        - Building A Course Recommender App with Streamlit
            - https://www.youtube.com/watch?v=w564MnjtB7I
        - Streamlit Documentation
            - https://streamlit.io/
<center> Wish you best of luck </center>
<hr>
