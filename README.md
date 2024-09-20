<!-- @format -->

# Task Manager app with stremlit

This is a task management web application built using Python, Streamlit, and SQLite. It allows users to register, log in, and manage their personal to-do lists by adding and viewing tasks.

## Features

- **User Registration**: Users can create an account by providing a unique username and password.
- **User Login**: Users can log in with their credentials and access their tasks.
- **Task Management**: Once logged in, users can add tasks to their personal to-do list and view all tasks they have added.
- **Persistent Data**: User information and tasks are stored in an SQLite database, ensuring that data is available after closing and reopening the app.

## Technologies Used

- **Python**: The core programming language used for the logic of the application.
- **Streamlit**: A Python library used for building the web interface.
- **SQLite**: A lightweight database used to store user accounts and tasks.

## Installation

Follow these steps to run the project locally on your machine:

### Prerequisites

- Python 3.x
- Install the required libraries using `pip`:
  pip install streamlit sqlite3

## Steps to Run

1. Clone the Repository

Clone this repository to your local machine using Git:

git clone https://github.com/AliFathi1325/To-Do_List_Streamlit.git

cd task_manager

2. Run the Application

Use the following command to start the Streamlit app:

streamlit run app.py

3. Access the App

After running the command, Streamlit will provide you with a local URL (usually http://localhost:8501) that you can open in your web browser to access the application.

## Usage

1. Open the application in your browser.
2. Sign Up to create a new account by providing a username and password.
3. Login with your credentials.
4. Once logged in, you can:
   - Add new tasks.
   - View your current tasks.
