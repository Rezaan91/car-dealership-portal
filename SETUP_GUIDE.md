# Quick Start Guide - Car Dealership Portal

## Prerequisites
- Python 3.10 or higher
- Node.js 18.x or higher
- Git
- pip and npm

## Step 1: Clone Repository (After uploading to GitHub)
```bash
git clone <your-github-repo-url>
cd "Full Stack Capstone Project"
```

## Step 2: Backend Setup

### 2.1 Create Virtual Environment (Recommended)
```bash
cd server
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2.2 Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2.3 Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2.4 Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 2.5 Populate Sample Data
```bash
python manage.py populate_data
```
This will create sample dealers, car makes, models, and reviews.

### 2.6 Start Django Server
```bash
python manage.py runserver
```
Backend will be available at http://localhost:8000

## Step 3: Frontend Setup

### 3.1 Open New Terminal
Keep the Django server running and open a new terminal window.

### 3.2 Navigate to Frontend Directory
```bash
cd server/frontend
```

### 3.3 Install Node Dependencies
```bash
npm install
```

### 3.4 Start React Development Server
```bash
npm start
```
Frontend will automatically open at http://localhost:3000

## Step 4: Verify Installation

### 4.1 Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Admin Panel: http://localhost:8000/admin/

### 4.2 Test Login
Use the test user credentials:
- Username: `testuser`
- Password: `testpass123`

Or use the superuser account you created.

### 4.3 Test Features
1. Browse dealers on home page
2. Filter dealers by state
3. View dealer details
4. Login with test credentials
5. Post a review
6. View reviews with sentiment analysis

## Step 5: Access Admin Panel

1. Navigate to http://localhost:8000/admin/
2. Login with superuser credentials
3. Manage:
   - Car Makes
   - Car Models
   - Dealers
   - Reviews
   - Users

## Step 6: Testing API Endpoints

### Test with cURL:

**Get All Dealers:**
```bash
curl http://localhost:8000/api/dealers/
```

**Login:**
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"testuser\", \"password\": \"testpass123\"}" \
  -c cookies.txt
```

**Get Dealer Reviews:**
```bash
curl http://localhost:8000/api/reviews/dealer/1/
```

**Analyze Sentiment:**
```bash
curl -X POST http://localhost:8000/api/analyze/ \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Fantastic services\"}"
```

## Step 7: Running Tests

```bash
cd server
python manage.py test
```

## Step 8: Building for Production

### Backend:
```bash
cd server
python manage.py collectstatic
```

### Frontend:
```bash
cd server/frontend
npm run build
```

## Troubleshooting

### Issue: Port 8000 already in use
**Solution:** 
```bash
python manage.py runserver 8001
```
Then update frontend proxy in package.json.

### Issue: Port 3000 already in use
**Solution:**
```bash
PORT=3001 npm start
```

### Issue: Module not found errors
**Solution:**
```bash
# For Python:
pip install -r requirements.txt

# For Node:
cd server/frontend
npm install
```

### Issue: Database errors
**Solution:**
```bash
# Delete db.sqlite3 and run:
python manage.py makemigrations
python manage.py migrate
python manage.py populate_data
```

### Issue: CORS errors
**Solution:** Ensure django-cors-headers is installed and configured in settings.py.

## Project Structure Overview

```
Full Stack Capstone Project/
├── server/
│   ├── djangoproj/           # Django project settings
│   │   ├── settings.py       # Project settings
│   │   ├── urls.py          # Main URL configuration
│   │   └── wsgi.py          # WSGI configuration
│   ├── djangoapp/           # Main Django app
│   │   ├── models.py        # Database models
│   │   ├── views.py         # API views
│   │   ├── serializers.py   # DRF serializers
│   │   ├── urls.py          # App URL routes
│   │   ├── admin.py         # Admin configuration
│   │   └── management/      # Custom commands
│   ├── frontend/            # React application
│   │   ├── src/
│   │   │   ├── components/  # React components
│   │   │   ├── App.js       # Main app
│   │   │   └── index.js     # Entry point
│   │   ├── static/          # Static HTML pages
│   │   │   ├── About.html
│   │   │   └── Contact.html
│   │   └── package.json
│   ├── manage.py
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # CI/CD pipeline
├── README.md
├── GRADING_CHECKLIST.md
└── Output files for grading
```

## Available URLs

### Frontend Routes:
- `/` - Home page with dealer listings
- `/dealers` - All dealers page
- `/dealer/:id` - Dealer details
- `/login` - Login page
- `/register` - Registration page
- `/postreview/:id` - Post review for dealer

### Backend API Endpoints:
- `/api/login/` - User login
- `/api/logout/` - User logout
- `/api/register/` - User registration
- `/api/user/` - Current user info
- `/api/dealers/` - All dealers
- `/api/dealers/:id/` - Dealer by ID
- `/api/dealers/state/:state/` - Dealers by state
- `/api/reviews/dealer/:id/` - Dealer reviews
- `/api/reviews/` - Post review
- `/api/cars/makes/` - All car makes
- `/api/cars/models/` - All car models
- `/api/analyze/` - Sentiment analysis

### Static Pages:
- `/static/About.html` - About Us page
- `/static/Contact.html` - Contact Us page

## Sample Users

The populate_data command creates these test users:

1. **testuser**
   - Password: testpass123
   - Email: testuser@example.com

2. **john_doe**
   - Password: password123
   - Email: john@example.com

3. **jane_smith**
   - Password: password123
   - Email: jane@example.com

## Next Steps

1. **Upload to GitHub:**
   - Initialize git repository
   - Add all files
   - Push to GitHub
   - Make repository public
   - Update README with GitHub URLs

2. **Deploy Application:**
   - Choose platform (Heroku, Render, Railway, etc.)
   - Follow platform-specific deployment guide
   - Update deploymentURL file with actual URL

3. **Test All Features:**
   - Go through GRADING_CHECKLIST.md
   - Verify all 28 tasks
   - Test all API endpoints
   - Ensure frontend works correctly

4. **Submit Project:**
   - Provide GitHub repository URL
   - Provide deployment URL
   - Include all output files

## Support

For issues or questions:
- Check GRADING_CHECKLIST.md for detailed task verification
- Review README.md for API documentation
- Ensure all dependencies are installed correctly

## License

MIT License - See README.md for details

---

**Project Created:** January 18, 2026
**Framework:** Django 4.2.7 + React 18.2.0
**Status:** Ready for Deployment and Grading
