# StonkSpy
![Bildschirmfoto_26-12-2024_181658_localhost](https://github.com/user-attachments/assets/2e60d135-e684-465f-9eb9-4c6da7a59d72)
![Bildschirmfoto_26-12-2024_181725_localhost](https://github.com/user-attachments/assets/1e2df10c-e488-45f9-b5f6-052ea561eff3)
![Bildschirmfoto_26-12-2024_181737_localhost](https://github.com/user-attachments/assets/21d12626-7f75-448b-b672-58a6583a805f)


## using
* React Vite
* Shadcn
* Python Flask
* Google Cloud VertexAI


## dev setup

### backend

You need a Google Cloud account, setup a project and activate the VertexAI service for this project.

Then you need to create a service account which has the Vertex AI User role.

Create a private key for the service account and download it as a .json file. This is used for the backend to authenticate to the Google Cloud.

* create `.env` file in root to store Google Cloud information for VertexAI
  * with Project ID `PROJECT_ID`, like `PROJECT_ID = "my-google-cloud-project-name"`
  * with Location `LOCATION`, like `LOCATION = "us-central1"`
  * with Google Application Credentials `GOOGLE_APPLICATION_CREDENTIALS`, like `GOOGLE_APPLICATION_CREDENTIALS = "path-to-google-service-account-private-key.json"`
* run `pip install -r requirements.txt`

### frontend
* `cd` to the frontend folder and run `npm install`
