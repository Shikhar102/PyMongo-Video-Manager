# YouTube Manager Application 🎥

A robust and efficient Python-based application designed for managing YouTube video metadata using MongoDB. This project supports full CRUD operations (Create, Read, Update, Delete), offering an intuitive interface for video management.

---

## 🚀 Features

- **View All Videos**: Display a list of all stored videos with their metadata.
- **Add Videos**: Add new videos by specifying their name and time.
- **Update Videos**: Modify existing video records by ID.
- **Delete Videos**: Safely remove video records from the database.
- **User-Friendly CLI**: Simple and interactive command-line interface for seamless operations.

---

## 🛠️ Prerequisites

- Python 3.7 or higher
- A MongoDB instance (local or cloud)

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shikhar102/PyMongo-Video-Manager.git
   cd YouTube-Manager 
2.  **Set Up a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate
    # On Windows: env\Scripts\activate
3. **Install Required Dependencies**
    ```bash
    pip install -r requirements.txt
4. **Configure Environment Variables**
    - Create a `.env` file in the project root
    ```bash
    MONGO_URL="mongodb+srv://<username>:<password>@<cluster-url>/ytmanager?retryWrites=true&w=majority" 
    ```
    - Replace `<username>`, `<password>`, and `<cluster-url>` with your MongoDB credentials.

## 📖 Usage
1. **Run the application:**
    ```bash
    python app.py # app.py-> application name
    ```
2. **Follow the interactive menu:**

    - 1: List all videos
    - 2: Add a new video
    - 3: Update an existing video
    - 4: Delete a video
    - 5: Exit the application

# 📂 Project Structure
    
**The project is organized as follows:**

```plaintext
YouTube-Manager/
├── app.py              # Main application script
├── requirements.txt    # File listing Python dependencies
├── .env                # Environment variables (excluded from Git)
├── .gitignore          # Specifies files to exclude from version control
├── README.md           # Documentation for the project
```

# 🧰 Technologies Used

- `Python`: For scripting and building the application logic.
- `MongoDB`: A NoSQL database for storing and managing video data.
- `pymongo`: Python driver for interacting with MongoDB.
- `python-dotenv`: For managing sensitive configuration variables securely.

# 👨‍💻 Contributing
**Contributions are highly encouraged! Here's how you can help:**
- Fork the repository.
- Create a new branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -m 'Add a new feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a pull request.

# 📜 License
- This project is licensed under the `MIT License`. You are free to use, modify, and distribute this software as per the license terms.

# 💡 Acknowledgments

- MongoDB for providing a powerful and scalable NoSQL database solution.
- The Python community for their incredible libraries and support.

## ✉️ Contact

**For queries, suggestions, or collaboration, feel free to reach out:**

- 📧 **Email**: [click me](mailto:shikhargupta8080@gmail.com)  
- 💻 **GitHub**: [click me](https://github.com/Shikhar102)  
- 👔 **LinkedIn**: [click me](https://www.linkedin.com/in/connect-shikhargupta/)  

