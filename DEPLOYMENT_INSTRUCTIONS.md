# Deployment Instructions

## ✅ Git Repository Initialized!

Your code is now committed to Git. Here are your deployment options:

---

## 🚀 Option 1: Deploy to Render (Recommended - Free Tier)

### Step 1: Create GitHub Repository
```bash
# Create a new repository on GitHub.com (make it public)
# Then run these commands:

git remote add origin https://github.com/YOUR_USERNAME/car-dealership-portal.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://render.com and sign up (free)
2. Click "New +" → "Web Service"
3. Connect your GitHub account
4. Select your repository
5. Configure:
   - **Name:** car-dealership-portal
   - **Root Directory:** server
   - **Environment:** Python 3
   - **Build Command:** 
     ```
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
     ```
   - **Start Command:** 
     ```
     gunicorn djangoproj.wsgi:application
     ```
6. Add Environment Variables:
   - `SECRET_KEY`: (generate a new secret key)
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: your-app-name.onrender.com
   - `DATABASE_URL`: (Render provides this automatically if you add PostgreSQL)

7. Click "Create Web Service"

### Step 3: Add PostgreSQL Database (Optional but recommended)
1. In Render Dashboard, click "New +" → "PostgreSQL"
2. Name it and create
3. Copy the "Internal Database URL"
4. Add it to your web service as `DATABASE_URL` environment variable

---

## 🚀 Option 2: Deploy to Railway (Easy - Free Tier)

### Step 1: Push to GitHub (same as above)

### Step 2: Deploy on Railway
1. Go to https://railway.app and sign up (free)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect Django and deploy!
5. Add environment variables in Settings:
   - `SECRET_KEY`: (generate new)
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: *.railway.app

---

## 🚀 Option 3: Deploy to Heroku (Classic)

### Prerequisites
```bash
# Install Heroku CLI from: https://devcenter.heroku.com/articles/heroku-cli
heroku --version
```

### Deployment Steps
```bash
cd "c:\Users\rezaa\OneDrive\Desktop\Full Stack Application Development Capstone Project\Full Stack Capstone Project"

# Login to Heroku
heroku login

# Create Heroku app
heroku create car-dealership-portal-unique-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=".herokuapp.com"

# Deploy
git push heroku main

# Run migrations
heroku run python server/manage.py migrate

# Create superuser
heroku run python server/manage.py createsuperuser

# Populate sample data
heroku run python server/manage.py populate_data

# Open your app
heroku open
```

---

## 🖥️ Option 4: Test Locally First

Before deploying, test the application locally:

### Terminal 1 - Start Django Backend:
```bash
cd "c:\Users\rezaa\OneDrive\Desktop\Full Stack Application Development Capstone Project\Full Stack Capstone Project\server"

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data
python manage.py populate_data

# Start server
python manage.py runserver
```

### Terminal 2 - Start React Frontend:
```bash
cd "c:\Users\rezaa\OneDrive\Desktop\Full Stack Application Development Capstone Project\Full Stack Capstone Project\server\frontend"

# Install dependencies
npm install

# Start React app
npm start
```

### Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Admin Panel: http://localhost:8000/admin/

### Test Credentials:
- Username: testuser
- Password: testpass123

---

## 🔑 Generate Secret Key for Production

```python
# In Python terminal:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use this command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📝 Update After Deployment

Once deployed, update the `deploymentURL` file:

```bash
echo "https://your-app-name.render.com" > deploymentURL
```

Or:
```bash
echo "https://your-app-name.herokuapp.com" > deploymentURL
```

Or:
```bash
echo "https://your-app-name.up.railway.app" > deploymentURL
```

---

## 🧪 Verify Deployment

After deployment, test these endpoints:

1. **Home Page:** https://your-app.com/
2. **API Dealers:** https://your-app.com/api/dealers/
3. **About Page:** https://your-app.com/static/About.html
4. **Admin Panel:** https://your-app.com/admin/

---

## 🐛 Troubleshooting

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic` and ensure `STATIC_ROOT` is set.

### Issue: Database connection error
**Solution:** Ensure `DATABASE_URL` is set in environment variables.

### Issue: CORS errors
**Solution:** Add your deployment domain to `CORS_ALLOWED_ORIGINS` in settings.py.

### Issue: 500 Internal Server Error
**Solution:** Set `DEBUG=True` temporarily to see detailed error, then fix and set back to `False`.

---

## 📋 Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] Can view dealers on home page
- [ ] Can register new user
- [ ] Can login/logout
- [ ] Can view dealer details
- [ ] Can post reviews
- [ ] Admin panel accessible
- [ ] All 28 tasks verified

---

## 🎉 Congratulations!

Your full-stack car dealership application is now deployed and accessible to the world!

**Next Steps:**
1. Share your GitHub repository URL
2. Share your deployment URL
3. Test all features on the live site
4. Submit for grading with both URLs

---

**Current Status:** ✅ Code committed to Git, ready for deployment!
**Files Committed:** 56 files (5,194+ lines of code)
**Deployment Ready:** Yes
**GitHub Ready:** Yes (just need to push)

Choose your preferred deployment method above and follow the steps!
