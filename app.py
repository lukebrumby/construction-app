import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Dummy user data for authentication
USER_DATA = {
    'user1': 'password1',
    'user2': 'password2'
}

# Dummy data storage
DATA_STORAGE = {
    'timetable': pd.DataFrame(columns=['Task', 'Start Date', 'End Date']),
    'timesheet': pd.DataFrame(columns=['Date', 'Employee', 'Hours Worked']),
    'calendar': pd.DataFrame(columns=['Event', 'Date']),
    'projects': pd.DataFrame(columns=['Project Name', 'Start Date', 'End Date']),
    'invoices': pd.DataFrame(columns=['Invoice Number', 'Amount', 'Date']),
    'expenses': pd.DataFrame(columns=['Expense Name', 'Amount', 'Date']),
    'team': pd.DataFrame(columns=['Name', 'Role'])
}

# Load saved data from JSON files (if exists)
def load_data():
    try:
        with open('data.json', 'r') as file:
            global DATA_STORAGE
            DATA_STORAGE = json.load(file)
            # Convert lists to DataFrames
            for key in DATA_STORAGE.keys():
                DATA_STORAGE[key] = pd.DataFrame(DATA_STORAGE[key])
    except FileNotFoundError:
        pass

# Save data to JSON files
def save_data():
    with open('data.json', 'w') as file:
        json.dump({key: DATA_STORAGE[key].to_dict(orient='records') for key in DATA_STORAGE.keys()}, file)

# Function to display the login page
def login_page():
    st.title('Login Page')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username in USER_DATA and USER_DATA[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
            st.experimental_rerun()
        else:
            st.error('Invalid username or password')

# Function to display the main content
def main_content():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to', ['Timetable', 'Timesheet', 'Calendar', 'Projects', 'Invoices', 'Expenses', 'Team'])

    if selection == 'Timetable':
        timetable_page()
    elif selection == 'Timesheet':
        timesheet_page()
    elif selection == 'Calendar':
        calendar_page()
    elif selection == 'Projects':
        projects_page()
    elif selection == 'Invoices':
        invoices_page()
    elif selection == 'Expenses':
        expenses_page()
    elif selection == 'Team':
        team_page()

def timetable_page():
    st.title('Timetable')
    st.write('Manage project timetables.')
    with st.form(key='timetable_form'):
        task = st.text_input('Task')
        start_date = st.date_input('Start Date', datetime.now())
        end_date = st.date_input('End Date', datetime.now())
        submit_button = st.form_submit_button('Add Task')

        if submit_button:
            new_task = pd.DataFrame([[task, start_date, end_date]], columns=['Task', 'Start Date', 'End Date'])
            DATA_STORAGE['timetable'] = pd.concat([DATA_STORAGE['timetable'], new_task], ignore_index=True)
            save_data()
            st.success('Task added successfully!')
    
    st.dataframe(DATA_STORAGE['timetable'])

def timesheet_page():
    st.title('Timesheet')
    st.write('Manage employee timesheets.')
    with st.form(key='timesheet_form'):
        date = st.date_input('Date', datetime.now())
        employee = st.text_input('Employee Name')
        hours_worked = st.number_input('Hours Worked', min_value=0.0, step=0.1)
        submit_button = st.form_submit_button('Add Entry')

        if submit_button:
            new_entry = pd.DataFrame([[date, employee, hours_worked]], columns=['Date', 'Employee', 'Hours Worked'])
            DATA_STORAGE['timesheet'] = pd.concat([DATA_STORAGE['timesheet'], new_entry], ignore_index=True)
            save_data()
            st.success('Timesheet entry added successfully!')
    
    st.dataframe(DATA_STORAGE['timesheet'])

def calendar_page():
    st.title('Calendar')
    st.write('Manage project events.')
    with st.form(key='calendar_form'):
        event = st.text_input('Event')
        event_date = st.date_input('Date', datetime.now())
        submit_button = st.form_submit_button('Add Event')

        if submit_button:
            new_event = pd.DataFrame([[event, event_date]], columns=['Event', 'Date'])
            DATA_STORAGE['calendar'] = pd.concat([DATA_STORAGE['calendar'], new_event], ignore_index=True)
            save_data()
            st.success('Event added successfully!')
    
    st.dataframe(DATA_STORAGE['calendar'])

def projects_page():
    st.title('Projects')
    st.write('Manage ongoing projects.')
    with st.form(key='projects_form'):
        project_name = st.text_input('Project Name')
        start_date = st.date_input('Start Date', datetime.now())
        end_date = st.date_input('End Date', datetime.now())
        submit_button = st.form_submit_button('Add Project')

        if submit_button:
            new_project = pd.DataFrame([[project_name, start_date, end_date]], columns=['Project Name', 'Start Date', 'End Date'])
            DATA_STORAGE['projects'] = pd.concat([DATA_STORAGE['projects'], new_project], ignore_index=True)
            save_data()
            st.success('Project added successfully!')
    
    st.dataframe(DATA_STORAGE['projects'])

def invoices_page():
    st.title('Invoices')
    st.write('Manage invoices.')
    with st.form(key='invoices_form'):
        invoice_number = st.text_input('Invoice Number')
        amount = st.number_input('Amount', min_value=0.0, step=0.1)
        date = st.date_input('Date', datetime.now())
        submit_button = st.form_submit_button('Add Invoice')

        if submit_button:
            new_invoice = pd.DataFrame([[invoice_number, amount, date]], columns=['Invoice Number', 'Amount', 'Date'])
            DATA_STORAGE['invoices'] = pd.concat([DATA_STORAGE['invoices'], new_invoice], ignore_index=True)
            save_data()
            st.success('Invoice added successfully!')
    
    st.dataframe(DATA_STORAGE['invoices'])

def expenses_page():
    st.title('Expenses')
    st.write('Track and manage expenses.')
    with st.form(key='expenses_form'):
        expense_name = st.text_input('Expense Name')
        amount = st.number_input('Amount', min_value=0.0, step=0.1)
        date = st.date_input('Date', datetime.now())
        submit_button = st.form_submit_button('Add Expense')

        if submit_button:
            new_expense = pd.DataFrame([[expense_name, amount, date]], columns=['Expense Name', 'Amount', 'Date'])
            DATA_STORAGE['expenses'] = pd.concat([DATA_STORAGE['expenses'], new_expense], ignore_index=True)
            save_data()
            st.success('Expense added successfully!')
    
    st.dataframe(DATA_STORAGE['expenses'])

def team_page():
    st.title('Team')
    st.write('Manage team members.')
    with st.form(key='team_form'):
        name = st.text_input('Name')
        role = st.text_input('Role')
        submit_button = st.form_submit_button('Add Team Member')

        if submit_button:
            new_member = pd.DataFrame([[name, role]], columns=['Name', 'Role'])
            DATA_STORAGE['team'] = pd.concat([DATA_STORAGE['team'], new_member], ignore_index=True)
            save_data()
            st.success('Team member added successfully!')
    
    st.dataframe(DATA_STORAGE['team'])

# Main entry point
def main():
    load_data()
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        login_page()
    else:
        main_content()

if __name__ == '__main__':
    main()
