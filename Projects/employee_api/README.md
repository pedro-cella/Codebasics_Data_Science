# Company Management API 🚀

A high-performance REST API built with **FastAPI** for resources data analysis. This project demonstrates a clean separation of concerns, moving from raw data queries to complex business insights using **NumPy**.

## 🏗️ Project Architecture

The API is organized into four logical levels to facilitate data consumption:

1. **Queries**: Basic CRUD-like operations for raw data retrieval (Find all, by ID, by Department).
2. **Statistics**: Quantitative metrics and averages (Salary averages, worker counts, distribution).
3. **Analysis**: Logical filters and conditional data processing (Salary range, tenure operations).
4. **Insights**: High-level business intelligence (Top performers, satisfaction peaks, veteran analysis).

## 🛠️ Technologies Used

* **Python 3.10+**
* **FastAPI**: Modern web framework for high-performance API development.
* **NumPy**: Scientific computing for efficient statistical analysis.
* **Uvicorn**: Lightning-fast ASGI server implementation.
* **Pydantic**: Data validation and settings management.

---

## 🧠 Concepts Practiced

This project was developed not only to build an API, but also to reinforce fundamental and intermediate programming concepts studied throughout my learning journey.

### 🔹 Core Python Concepts
* Variables and data types (int, float, string)
* String manipulation
* Control flow (if, elif, else)
* Loops (for, basic iteration patterns)

### 🔹 Data Structures
* Lists (iteration, filtering)
* Dictionaries (data organization and access)
* Tuples (basic usage)

### 🔹 Functions & Code Organization
* Function creation and reuse
* Parameters and return values
* Code modularization

### 🔹 Object-Oriented Programming
* Classes and objects
* Methods and basic structure

### 🔹 Error Handling
* try / except blocks
* Basic exception management

### 🔹 Data Handling & Processing
* Data filtering and transformation
* Conditional logic applied to datasets

### 🔹 Analytical Thinking
* Breaking down problems into smaller steps
* Translating business rules into code
* Working with real-world data scenarios

---

### 🎯 Learning Goal

This project is part of my journey to become a Data Scientist, focusing on transforming theoretical knowledge into practical, real-world applications.

---

## 🚀 How to Run the Project

### 1. Prerequisites
Make sure you have Python installed on your machine. We recommend using a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Linux/Mac)
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn main:app --reload
```
### 4. Access the API Documentation

After running the server, open your browser and go to:

#### 👉 Swagger UI (interactive docs)
- http://127.0.0.1:8000/docs

#### 👉 ReDoc (alternative documentation)
- http://127.0.0.1:8000/redoc

---

💡 You can test all endpoints directly from the browser using the Swagger interface.
