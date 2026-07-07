Lab 10.3 - Deployment via Streamlit
Introduction
Note: This notebook should work on your local machine.

The purpose of this lab is to take you through the process of deploying a machine learning web app on a publicly hosted platform (streamlit.io and optionally render.com). A trained model will be created using the Scikit-learn pipeline (combining loading, preprocessing and training steps), then separate files of Python code and text will need to be completed to make deployment possible. Firstly the app will be deployed to your local machine (so that you can view it in your browser). Once that it is successful, the files will be uploaded to a new repository you create in GitHub and then Streamlit or Render will read from this to host the application via a publicly accessible URL.

The app will take in a text string from a user and output a prediction of whether that string is expressing positive or negative sentiment. The model is created using methods from Module 8 (Natural Language Processing). Since the training data used to create the model is small (300 records), the prediction may only be accurate around 70% of the time. In future you may wish to improve this app's performance or develop your own app in a similar manner.

The following files are needed to create the app (they should be in the same folder as this notebook):
requirements.txt
app.py
model.joblib
utils.py
.streamlit/ (folder containing config.toml)

Firstly we will see how a predictive model can be created as a pipe which combines the preprocessing, feature engineering and model training steps. This model is then saved as a joblib pickle file which can be reloaded at any time to avoid retraining.

This trained model can be loaded within your production environment along with required packages and real-time predictions can be made by calling its predict() method.

Streamlit enables apps to be deployed rapidly with minimal knowledge of HTML or CSS. Some of the key concepts are described at https://docs.streamlit.io/get-started/fundamentals/main-concepts. Sample apps can be seen at https://streamlit.io/gallery.

Local hosting
Using Anaconda prompt (Windows) or a Terminal window (Mac) run "streamlit run app.py". This deploys the app locally on http://localhost:8501/ (or similar) which you can then view on the browser. The file app.py may require debugging before it runs successfully.

Bonus Exercise: Redesign the webpage by adding other components. You can use the cheat sheet at https://docs.streamlit.io/library/cheatsheet as a reference.

Deployment via streamlit.io
So far you have deployed your model on your local machine. Now we seek to deploy it publicly.

streamlit.io is intended to deploy Streamlit apps seamlessly without worrying about infrastructure.

There is one additional file needed for external deployment of your model:

requirements.txt includes the versions of packages that are to be used with the app.
To update the requirements.txt file use the __version__ attribute to see the version of packages being used. This ensures that your model is reproducible on other computing environments.

Log into your GitHub account (create one if you have not already done so) and create a new repository containing the following files.
requirements.txt
app.py
model.joblib
utils.py
.streamlit/ (folder containing config.toml)
This config.toml allows one to set themes such as the type of background to display.

Next sign up for a free account at https://streamlit.io/ and once signed in, go to https://share.streamlit.io/ and click the blue "New app" button. Under "Repository" specify the GitHub repository where your app is located (in the form username/reponame). The default URL is based on the app's location in GitHub, but that may be changed. Under "main file path" enter app.py replacing streamlit-app.py. Finally click the "Deploy!" button. If successful the app will deployed to the specified url (it may take several minutes). An example can be seen at https://iod-sentiment-app.streamlit.app/.

If there are issues, click on the "Manage app" button at the bottom right to view the app's logs. Files such as requirements.txt can be edited directly within GitHub.

Further details are at https://docs.streamlit.io/streamlit-community-cloud/manage-your-app.

If you managed to see your app successfully, congratulations! You now know how to deploy an app on the cloud. To make it visible to others, go to your app's settings and under "Sharing" -> "Who can view this app" select "This app is public and searchable".
