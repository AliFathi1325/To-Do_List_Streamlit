import sqlite3
import streamlit as st

# st.markdown("# Page 2 ❄️")

# st.sidebar.markdown("# Page 12 ❄️")

def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_tables():
    conn = connect_db()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT)
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id))
    ''')

    conn.commit()
    conn.close()


def register_user(username, password):
    conn = connect_db()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

def get_user_id(username):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()
    conn.close()
    return user_id[0] if user_id else None

def signup():
    st.subheader('Sign Up')
    username = st.text_input('User name')
    password = st.text_input('Password', type='password')
    password_confirm = st.text_input('Repeat password', type='password')
    if st.button('Sign UP'):
        if password != password_confirm:
            st.error('The password and its repetition do not match')
        else:
            if register_user(username, password):
                st.success('Registration was successful, please login')
            else:
                st.error('Username already exists')

def login():
    st.subheader('Login')
    username = st.text_input('User name')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        user = login_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f'Welcome {username}')
        else:
            st.error('The username or password is incorrect')

def delete_task(task_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def task_manager():
    st.subheader(f"Management of {st.session_state.username}'s tasks")

    task = st.text_input('New task:')
    if st.button('add'):
        user_id = get_user_id(st.session_state.username)
        if user_id:
            conn = connect_db()
            c = conn.cursor()
            c.execute('INSERT INTO tasks (user_id, task) VALUES (?, ?)', (user_id, task))
            conn.commit()
            conn.close()
            st.success('task added')

    user_id = get_user_id(st.session_state.username)
    if user_id:
        conn = connect_db()
        c = conn.cursor()
        c.execute('SELECT id, task FROM tasks WHERE user_id = ?', (user_id,))
        tasks = c.fetchall()
        conn.close()

        st.write('to-do list:')
        for task in tasks:
            task_id, task_text = task
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f'- {task_text}')
            with col2:
                if st.button('delet', key=f'delete_{task_id}'):
                    delete_task(task_id)

create_tables()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ''

if st.session_state.logged_in:
    task_manager()
else:
    st.sidebar.title('User Account')
    action = st.sidebar.selectbox('Choose',['Login', 'Sign Up'])

    if action == 'Login':
        login()
    if action == 'Sign Up':
        signup()