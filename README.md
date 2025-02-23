# Virtual Mouse Control With Gesture Recognition and Voice Assistant

This is Final Year Project for VIT

# Getting Started

  ### Pre-requisites
  
  Python: (3.9.21)<br>
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  
  ### Procedure
  ```bash
  git clone this repo
  ```
  For detailed information about cloning visit [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
  
  Step 1: 
  ```bash
  conda create --name gesture python=3.9.21
  ```
  
  Step 2:
  ```bash
  conda activate gesture
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  conda install pywin32
  ```

  Step 5:
  1. Create an .env file inside the src directory with the following line
    ```bash
    GEMINI_API_KEY = <YOUR_GEMINI_API_KEY>
    ```
  2. To Create Gemini API Key visit [Google AI Studio](https://aistudio.google.com/apikey)
  
  Step 6:
  ``` 
  cd to the GitHub Repo till src folder
  ```
  Command may look like: `cd C:\Users\.....\Glide-Connect\src`
  
  Step 7:
  
  For running Voice Assistant:
  ```bash 
  python Voice_Assistant.py
  ```
  
  For running only Gesture Recognition:
  ```bash 
  python Gesture_Controller.py
  ```