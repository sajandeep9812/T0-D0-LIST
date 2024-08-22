# T0-D0-LIST

Tkinter To-Do List Application <br>
Overview
This is a Python-based To-Do List application built using the Tkinter library. The application provides a simple graphical user interface (GUI) to manage tasks, allowing users to add, edit, delete, and mark tasks as complete or incomplete. Tasks are stored in a JSON file, ensuring that they persist between sessions. Additionally, the application allows users to save their task list as a PDF file.

<br>

<b>Features: </b> <br>
- <b>Add Task: </b> Add new tasks to the list using a text entry field.  <br>
- <b>Delete Task: </b>  Remove selected tasks from the list.  <br>
- <b>Mark Complete/Incomplete:  </b> Toggle tasks as complete or incomplete by clicking on them.  <br>
- <b>Edit Task:  </b> Modify the selected task's text.  <br>
- <b>Multiple Selection: </b>  Select multiple tasks simultaneously for deletion or completion.  <br>
- <b>Save Tasks to JSON: </b>  Tasks are automatically saved to a JSON file for persistence across sessions.  <br>
- <b>Export Tasks as PDF: </b>  Save the current task list as a PDF file.  <br>

<b> Requirements: </b> <br>
- Python 3.x
- Tkinter (comes pre-installed with Python) <br>
- ReportLab (for PDF generation) <br>

**You can install the ReportLab library using pip:** <br>
- pip install reportlab

**File Structure:** <br>
- <b>home.py:</b> The main Python script that runs the application. <br>
- <b>tasks.json:</b> A JSON file where tasks are saved. This file is automatically created and updated as you use the application.<br>
- <b>assets/:</b> Directory containing images and other assets used in the GUI.<br>

