# Restaurant Web Application

A full-featured restaurant web application built with Django, featuring online menu browsing, table reservations, and shopping cart functionality.

## 🌟 Features

- **User Authentication**: Secure registration and login system
- **Menu Management**: Browse restaurant menu with categories and pricing
- **Shopping Cart**: Add items to cart, adjust quantities, and place orders
- **Table Reservations**: Reserve tables with date and time selection
- **Order Tracking**: View order history and reservation details
- **Admin Dashboard**: Manage menu items, orders, and reservations
- **Responsive Design**: Mobile-friendly interface

## 🛠️ Technologies Used

- **Backend**: Django 5.2.5
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript (templates from [original Flask project](https://github.com/avocadopelvis/restaurant-web-app))
- **Authentication**: Django built-in authentication system
- **Image Handling**: Pillow

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/restaurant-web-app.git
cd restaurant-web-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# Create .env file
touch .env  # Mac/Linux
# or
echo. > .env  # Windows
```

Add the following to your `.env` file:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

**To generate a secure SECRET_KEY:**

```python
# Run in Python shell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it in your `.env` file.

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 8. Collect Static Files

```bash
python manage.py collectstatic
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
restaurant-web-app/
├── restaurant/              # Main app (menu, orders, authentication)
│   ├── models.py           # Menu, MenuItem, Order models
│   ├── views.py            # View functions
│   ├── forms.py            # Custom forms
│   └── admin.py            # Admin configurations
├── reservations/           # Reservations app
│   ├── models.py          # Reservation model
│   ├── views.py           # Reservation views
│   └── forms.py           # Reservation forms
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS, images)
├── media/                # Uploaded files (menu item images)
├── restaurant_app/       # Project settings
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL configurations
│   └── wsgi.py          # WSGI configuration
└── manage.py            # Django management script
```

## 👤 Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

**Features:**
- Add/Edit/Delete menu items
- Upload menu item images
- View and manage orders
- View and manage reservations
- Manage users

## 🔑 Key Functionalities

### For Customers:
- Browse menu items with images and prices
- Add items to cart and manage quantities
- Place orders (requires login)
- Reserve tables for specific dates and times
- View order history
- Cancel reservations

### For Admins:
- Full CRUD operations on menu items
- Upload and manage menu item images
- View all orders with details
- Manage table reservations
- User management

## 🧪 Running Tests

```bash
python manage.py test
```

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| SECRET_KEY | Django secret key for security | Yes |
| DEBUG | Debug mode (True/False) | Yes |

## 🚀 Deployment

This project is deployed on PythonAnywhere. For deployment instructions, see [PythonAnywhere Django Tutorial](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

**Live Demo**: [SilverLeaf](https://radical.pythonanywhere.com/)

## 🤝 Contributing

This project is part of my portfolio. Feel free to fork and modify for your own use.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Frontend templates adapted from [avocadopelvis/restaurant-web-app](https://github.com/avocadopelvis/restaurant-web-app)
- Original Flask implementation converted to Django

## 📧 Contact

Ali - [alimehdizadeh127@gmail.com](mailto:alimehdizadeh127@gmail.com)

Project Link: [https://github.com/Ali-127/restaurant-web-app](https://github.com/Ali-127/restaurant-web-app)

## 📸 Screenshots
### Home page
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 10-58-40 SilverLeaf" src="https://github.com/user-attachments/assets/0c5194f6-4620-422e-81ed-83c7e660a230" />

### Log in Page
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 10-58-53 Login   Registration" src="https://github.com/user-attachments/assets/5bacf502-50a6-4291-aed7-730a76723516" />

### Sign in Page
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 10-59-04 Login   Registration" src="https://github.com/user-attachments/assets/03c86069-c7f8-4c4e-8c0b-797ec3a41fcf" />

### Menu
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 11-00-15 Menu" src="https://github.com/user-attachments/assets/e921dd2e-6a8e-4274-a223-0b6f6858328d" />

### Table Reservation
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 11-01-21 Table Reservation" src="https://github.com/user-attachments/assets/4c266b4f-ca75-4965-986b-79dc6dae23c1" />

### Services
<img width="1366" height="635" alt="Screenshot 2025-10-05 at 11-01-32 SilverLeaf" src="https://github.com/user-attachments/assets/5cbfd56d-6810-4abf-94d8-60a84ebcb1db" />

### Cart
<img width="1366" height="768" alt="143269901-21b84d5e-81d3-4ed8-a6be-42692c0ccc58" src="https://github.com/user-attachments/assets/8e36a6f5-409b-438d-b63c-9f194a17fc4e" />

### OrderConfirmation
<img width="1366" height="768" alt="143270441-cb669f88-6d49-4f95-8540-5e5d7d1444f9" src="https://github.com/user-attachments/assets/fb6cdf6d-dcba-4a04-842c-c156b060a7a4" />

---

**Note**: This project was created as a portfolio piece to demonstrate Django web development skills, including user authentication, database management, and full-stack development capabilities.
