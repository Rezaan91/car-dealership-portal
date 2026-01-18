# Project Directory Structure

```
Full Stack Capstone Project/
│
├── 📄 README.md                          # Main project documentation
├── 📄 PROJECT_SUMMARY.md                 # Complete project overview
├── 📄 SETUP_GUIDE.md                     # Installation instructions
├── 📄 GRADING_CHECKLIST.md              # 28 tasks verification
├── 📄 API_TESTING_GUIDE.md              # API documentation with examples
├── 📄 .gitignore                         # Git ignore rules
│
├── 📁 .github/                           # GitHub configuration
│   └── 📁 workflows/
│       └── 📄 ci-cd.yml                  # CI/CD pipeline
│
├── 📁 server/                            # Backend Django application
│   │
│   ├── 📄 manage.py                      # Django management script
│   ├── 📄 requirements.txt               # Python dependencies
│   ├── 📄 Procfile                       # Heroku deployment
│   ├── 📄 runtime.txt                    # Python version
│   ├── 📄 .env.example                   # Environment variables template
│   ├── 📄 db.sqlite3                     # SQLite database (created after migrations)
│   │
│   ├── 📁 djangoproj/                    # Django project configuration
│   │   ├── 📄 __init__.py
│   │   ├── 📄 settings.py                # Project settings (CORS, REST, DB)
│   │   ├── 📄 urls.py                    # Main URL routing
│   │   ├── 📄 asgi.py                    # ASGI configuration
│   │   └── 📄 wsgi.py                    # WSGI configuration
│   │
│   ├── 📁 djangoapp/                     # Main Django application
│   │   ├── 📄 __init__.py
│   │   ├── 📄 models.py                  # Database models (CarMake, CarModel, Dealer, Review)
│   │   ├── 📄 views.py                   # API views (12 endpoints)
│   │   ├── 📄 serializers.py             # DRF serializers
│   │   ├── 📄 urls.py                    # App URL routing
│   │   ├── 📄 admin.py                   # Admin panel configuration
│   │   ├── 📄 apps.py                    # App configuration
│   │   ├── 📄 tests.py                   # Unit tests
│   │   │
│   │   └── 📁 management/                # Custom Django commands
│   │       ├── 📄 __init__.py
│   │       └── 📁 commands/
│   │           ├── 📄 __init__.py
│   │           └── 📄 populate_data.py   # Sample data seeding
│   │
│   └── 📁 frontend/                      # React frontend application
│       │
│       ├── 📄 package.json               # Node.js dependencies
│       ├── 📄 package-lock.json          # Lock file
│       │
│       ├── 📁 public/                    # Public assets
│       │   └── 📄 index.html             # HTML template
│       │
│       ├── 📁 src/                       # React source code
│       │   ├── 📄 index.js               # App entry point
│       │   ├── 📄 index.css              # Global styles
│       │   ├── 📄 App.js                 # Main app component with routing
│       │   │
│       │   └── 📁 components/            # React components
│       │       │
│       │       ├── 📁 Navigation/
│       │       │   └── 📄 Navigation.jsx  # Navigation bar with auth state
│       │       │
│       │       ├── 📁 Home/
│       │       │   └── 📄 Home.jsx        # Home page with dealer listings
│       │       │
│       │       ├── 📁 Login/
│       │       │   └── 📄 Login.jsx       # Login form
│       │       │
│       │       ├── 📁 Register/
│       │       │   └── 📄 Register.jsx    # Registration form (5 fields)
│       │       │
│       │       ├── 📁 Dealers/
│       │       │   ├── 📄 Dealers.jsx     # All dealers list
│       │       │   ├── 📄 DealerDetails.jsx  # Dealer details with reviews
│       │       │   └── 📄 Dealers.css     # Dealer styles
│       │       │
│       │       └── 📁 Review/
│       │           └── 📄 PostReview.jsx  # Post review form
│       │
│       ├── 📁 static/                    # Static HTML pages
│       │   ├── 📄 About.html             # About Us page (Task 3)
│       │   └── 📄 Contact.html           # Contact Us page (Task 4)
│       │
│       └── 📁 build/                     # Production build (created by npm run build)
│           └── 📄 index.html             # Built HTML
│
├── 📄 loginuser                          # Task 5: Login cURL output
├── 📄 logoutuser                         # Task 6: Logout cURL output
├── 📄 getdealerreviews                   # Task 8: Get reviews cURL output
├── 📄 getalldealers                      # Task 9: Get all dealers cURL output
├── 📄 getdealerbyid                      # Task 10: Get dealer by ID cURL output
├── 📄 getdealersbyState                  # Task 11: Get dealers by state cURL output
├── 📄 getallcarmakes                     # Task 14-15: Get car makes/models cURL output
├── 📄 analyzereview                      # Task 16: Sentiment analysis cURL output
├── 📄 django_server                      # Task 2: Django server terminal output
├── 📄 CICD                               # Task 23: GitHub Actions workflow output
└── 📄 deploymentURL                      # Task 24: Deployment URL

```

## File Count Summary

### Documentation Files: 5
- README.md
- PROJECT_SUMMARY.md
- SETUP_GUIDE.md
- GRADING_CHECKLIST.md
- API_TESTING_GUIDE.md

### Backend Files: 15
- Django configuration: 5 files
- Django app: 8 files
- Management commands: 2 files

### Frontend Files: 13
- React components: 8 files
- Configuration: 2 files
- Static pages: 2 files
- Entry points: 1 file

### Grading Output Files: 11
- cURL outputs: 8 files
- Terminal outputs: 2 files
- Deployment URL: 1 file

### Configuration Files: 6
- .gitignore
- requirements.txt
- package.json
- Procfile
- runtime.txt
- ci-cd.yml

**Total Files: 50+ files**

---

## Key Directories Explained

### `/server/djangoproj/`
Django project configuration with settings for CORS, REST framework, database, static files, and middleware.

### `/server/djangoapp/`
Main application containing models, views, serializers, and admin configuration for the car dealership features.

### `/server/djangoapp/management/commands/`
Custom Django management commands, including the data population script.

### `/server/frontend/src/components/`
React components organized by feature (Navigation, Home, Login, Register, Dealers, Review).

### `/server/frontend/static/`
Static HTML pages (About Us, Contact Us) with custom styling and content.

### `/.github/workflows/`
GitHub Actions CI/CD pipeline configuration for automated testing and deployment.

---

## Important Files

### Configuration
- **settings.py**: Django settings with CORS, REST framework, database
- **urls.py**: URL routing for all API endpoints
- **package.json**: React dependencies and scripts

### Models
- **models.py**: CarMake, CarModel, Dealer, Review models

### API
- **views.py**: 12 API endpoints for authentication, dealers, reviews, cars, sentiment
- **serializers.py**: DRF serializers for data formatting

### Frontend
- **App.js**: Main React app with routing
- **Navigation.jsx**: Navigation with authentication state
- **Register.jsx**: Registration form with 5 required fields
- **DealerDetails.jsx**: Dealer info with reviews
- **PostReview.jsx**: Review submission form

### Documentation
- **README.md**: Main documentation
- **GRADING_CHECKLIST.md**: All 28 tasks detailed

---

## Generated/Created After Setup

These files/folders are created after running setup commands:

```
server/
├── db.sqlite3                    # After: python manage.py migrate
├── __pycache__/                  # After: Running Python
├── djangoapp/migrations/         # After: python manage.py makemigrations
└── frontend/
    ├── node_modules/             # After: npm install
    └── build/                    # After: npm run build
```

---

## File Relationships

```
User Request
    ↓
React Component (e.g., PostReview.jsx)
    ↓
Axios HTTP Request
    ↓
Django URL Router (urls.py)
    ↓
Django View (views.py)
    ↓
Django Serializer (serializers.py)
    ↓
Django Model (models.py)
    ↓
SQLite Database (db.sqlite3)
```

---

## Development vs Production

### Development:
- db.sqlite3 (SQLite database)
- DEBUG = True
- CORS allows localhost:3000
- React dev server on port 3000
- Django dev server on port 8000

### Production:
- PostgreSQL database (via DATABASE_URL)
- DEBUG = False
- CORS configured for production domain
- React build served by Django
- Gunicorn WSGI server
- Static files collected

---

This structure ensures:
✓ Separation of concerns
✓ Organized code
✓ Easy navigation
✓ Scalable architecture
✓ Clear file purposes
✓ Professional organization
