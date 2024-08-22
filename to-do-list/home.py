import json
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Listbox, Scrollbar, END, simpledialog, MULTIPLE, EXTENDED
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas
from tkinter import filedialog

# Change path details if required
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/sajandeepsingh/Desktop/to-do-list/assets")
TASKS_FILE = OUTPUT_PATH / "tasks.json"  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(END, task)
        entry.delete(0, END)
        save_tasks()

def delete_task():
    selected_task_indices = task_listbox.curselection()
    for index in reversed(selected_task_indices):
        task_listbox.delete(index)
    save_tasks()

def mark_task_complete():
    selected_task_indices = task_listbox.curselection()
    for index in selected_task_indices:
        current_task = task_listbox.get(index)
        if current_task.startswith("✔️ "):
            # Uncheck the task
            task_listbox.delete(index)
            task_listbox.insert(index, current_task[2:])  # Remove "✔️ " from the task
        else:
            # Check the task
            task_listbox.delete(index)
            task_listbox.insert(index, f"✔️ {current_task}")
    save_tasks()

def edit_task():
    selected_task_indices = task_listbox.curselection()
    for index in selected_task_indices:
        current_task = task_listbox.get(index)
        new_task = simpledialog.askstring("Edit Task", "Modify the selected task:", initialvalue=current_task)
        if new_task:
            task_listbox.delete(index)
            task_listbox.insert(index, new_task)
    save_tasks()

def save_tasks():
    tasks = task_listbox.get(0, END)
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            for task in tasks:
                task_listbox.insert(END, task)

def save_tasks_as_pdf():
    pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        pdf = pdf_canvas.Canvas(pdf_file, pagesize=letter)
        pdf.drawString(100, 750, "Task List")
        y_position = 720

        for task in task_listbox.get(0, END):
            pdf.drawString(100, y_position, task)
            y_position -= 20
            if y_position < 50:  
                pdf.showPage()
                y_position = 750

        pdf.save()

window = Tk()
window.geometry("589x792")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=792,
    width=589,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(293.0, 50.0, image=image_image_1)

# Entry for adding tasks
entry = Entry(window, bd=0, bg="#F4F4F4", fg="#000716", highlightthickness=0)
entry.place(x=50, y=120, width=400, height=40)

# Button to add tasks
add_button = Button(
    window,
    text="Add Task",
    borderwidth=0,
    highlightthickness=0,
    command=add_task,
    relief="flat",
    bg="#6D83F2",
    fg="#000000"
)
add_button.place(x=470, y=120, width=80, height=40)

# Scrollbar for the Listbox
scrollbar = Scrollbar(window)
scrollbar.place(x=550, y=180, height=500)

# Listbox for tasks with scrollbar and increased padding
task_listbox = Listbox(
    window, 
    bg="#F4F4F4", 
    fg="#000716", 
    bd=0, 
    highlightthickness=0, 
    selectbackground="#D3D3D3", 
    activestyle='none', 
    yscrollcommand=scrollbar.set,
    font=("Arial", 14),  # Increase font size
    selectforeground="#000000",  # Ensure text is visible when selected
    selectborderwidth=5,  # Add padding
    selectmode=EXTENDED  # Allow multiple selection
)
task_listbox.place(x=50, y=180, width=500, height=500)
scrollbar.config(command=task_listbox.yview)

# Button to delete tasks
delete_button = Button(
    window,
    text="Delete Task",
    borderwidth=0,
    highlightthickness=0,
    command=delete_task,
    relief="flat",
    bg="#F26D6D",
    fg="#000000"
)
delete_button.place(x=240, y=700, width=110, height=40)

# Button to mark tasks as complete
complete_button = Button(
    window,
    text="Mark Complete",
    borderwidth=0,
    highlightthickness=0,
    command=mark_task_complete,
    relief="flat",
    bg="#6DF26D",
    fg="#000000"
)
complete_button.place(x=50, y=700, width=120, height=40)

# Button to edit tasks
edit_button = Button(
    window,
    text="Edit Task",
    borderwidth=0,
    highlightthickness=0,
    command=edit_task,
    relief="flat",
    bg="#FFD700",
    fg="#000000"
)
edit_button.place(x=370, y=700, width=120, height=40)

# Button to save tasks as PDF
save_pdf_button = Button(
    window,
    text="Save as PDF",
    borderwidth=0,
    highlightthickness=0,
    command=save_tasks_as_pdf,
    relief="flat",
    bg="#FFA500",
    fg="#000000"
)
save_pdf_button.place(x=470, y=60, width=100, height=40)

# Load tasks from JSON file when the app starts
load_tasks()

window.resizable(False, False)
window.mainloop()
