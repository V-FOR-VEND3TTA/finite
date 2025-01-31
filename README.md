# finite 
A web application that visualizes a user's remaining time based on their birthdate and estimated lifespan. Built with **Django (backend)** and **Bootstrap (frontend)**, **finite** aims to help users reflect on mortality and make meaningful choices in their daily lives.  

---

## **Table of Contents**  
- [Demo](#demo)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Technologies Used](#technologies-used)  
- [Future Improvements](#future-improvements)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)  

---

## **Demo**  
[Live Demo (not yet available)](https://example.com)  

---

## **Features**  
✅ **Personalized Time Visualization** – Enter birthdate and expected lifespan to see remaining time.  
✅ **Interactive UI** – Clean and minimal interface built with Bootstrap.  
✅ **Django-Powered Backend** – Secure and scalable framework for data processing.  
✅ **Customizable Lifespan Estimates** – Adjust lifespan expectations for better accuracy.  
✅ **Optional User Accounts** – Save and track your data over time (coming soon).  

---

## **Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-username/finite.git
cd finite
```

### **2. Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Apply Migrations**  
```sh
python manage.py migrate
```

### **5. Run the Development Server**  
```sh
python manage.py runserver
```

Now, visit `http://127.0.0.1:8000/` in your browser.

---

## **Usage**  
1. Enter your **birthdate** and **estimated lifespan**.  
2. View a **visual representation** of your remaining time.  
3. Reflect, prioritize, and **make the most of each day**.  

---

## **Configuration**  

### **Environment Variables**  
Create a `.env` file and define any necessary environment variables, such as:  
```
SECRET_KEY=your_secret_key
DEBUG=True
```

### **Customizing Lifespan Estimates**  
By default, the application assumes an **average lifespan of 80 years**. You can modify this in the settings.

---

## **Technologies Used**  
- **Backend**: Django  
- **Frontend**: Bootstrap  
- **Database**: SQLite (default), PostgreSQL (recommended for production)  
- **Styling**: Custom CSS + Bootstrap  
- **Deployment**: (TBD)  

---

## **Future Improvements**  
🚀 **User Accounts & Data Persistence** – Save and track personal lifespan data.  
🚀 **Custom Themes & Dark Mode** – Improve UI/UX.  
🚀 **API Integration** – Allow external applications to query remaining lifespan.  
🚀 **Mobile Optimization** – Enhance mobile experience.  

---

## **License**  
This project is licensed under the [MIT License](LICENSE).  

---

## **Acknowledgments**  
Inspired by the concept of **memento mori**, reminding us to live intentionally.  
