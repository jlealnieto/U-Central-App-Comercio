# FastAPI Productos CRUD

This project is a FastAPI application that implements a CRUD (Create, Read, Update, Delete) functionality for managing a "productos" table in a database. 

## Project Structure

```
fastapi-productos-crud
├── app
│   ├── main.py               # Entry point of the FastAPI application
│   ├── models
│   │   └── productos.py      # SQLAlchemy model for the "productos" table
│   ├── schemas
│   │   └── productos.py      # Pydantic schemas for data validation and serialization
│   ├── crud
│   │   └── productos.py      # CRUD operations for the "productos" table
│   ├── database.py           # Database connection setup
│   └── routers
│       └── productos.py      # API routes for the "productos" resource
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-productos-crud
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## Usage

Once the application is running, you can access the API documentation at `http://127.0.0.1:8000/docs`. Here you can test the CRUD operations for the "productos" resource.

## License

This project is licensed under the MIT License - see the LICENSE file for details.