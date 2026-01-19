# Render Deployment Guide

This guide provides step-by-step instructions for deploying the Car Dealership Portal to Render.

## Prerequisites

- GitHub account
- Render account (sign up at https://render.com)
- Code pushed to GitHub repository

---

## 🚀 Deployment Steps

### 1. Push Code to GitHub

If you haven't already pushed your code to GitHub:

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Create Render Account

1. Go to https://render.com
2. Sign up using your GitHub account (recommended)
3. Authorize Render to access your repositories

### 3. Deploy Using Blueprint (Recommended)

Since we have a `render.yaml` file, Render will automatically detect and configure everything:

1. **Go to Render Dashboard**: https://dashboard.render.com
2. **Click "New +"** → **"Blueprint"**
3. **Connect Repository**: Select `car-dealership-portal`
4. **Review Configuration**: Render will show:
   - Web Service: `car-dealership-portal`
   - Database: `car-dealership-db`
5. **Set Environment Variables** (if not auto-generated):
   - `SECRET_KEY`: Click "Generate" or use your own secure key
   - `ALLOWED_HOSTS`: Will be auto-set to your Render domain
6. **Click "Apply"**

Render will:
- Create PostgreSQL database
- Deploy Django application
- Run migrations
- Collect static files
- Start the server

### 4. Manual Deployment (Alternative)

If you prefer manual setup:

#### 4.1 Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. **Name**: `car-dealership-db`
3. **Database**: `car_dealership`
4. **User**: `car_dealership_user`
5. **Plan**: Free
6. Click "Create Database"
7. Copy the **Internal Database URL**

#### 4.2 Create Web Service
1. Click "New +" → "Web Service"
2. **Connect Repository**: Select your GitHub repo
3. **Configure**:
   - **Name**: `car-dealership-portal`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Root Directory**: `server`
   - **Environment**: Python 3
   - **Build Command**:
     ```bash
     chmod +x build.sh && ./build.sh
     ```
   - **Start Command**:
     ```bash
     gunicorn djangoproj.wsgi:application --bind 0.0.0.0:$PORT --workers 4
     ```
   - **Plan**: Free

#### 4.3 Environment Variables

Add these in the Render Dashboard under "Environment":

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `DEBUG` | `False` |
| `SECRET_KEY` | Click "Generate" |
| `DATABASE_URL` | Paste Internal Database URL from step 4.1 |
| `ALLOWED_HOSTS` | Your Render URL (e.g., `car-dealership-portal.onrender.com`) |
| `WEB_CONCURRENCY` | `4` |
| `DJANGO_SETTINGS_MODULE` | `djangoproj.settings` |

### 5. Monitor Deployment

1. Watch the **Logs** tab during deployment
2. Look for:
   - ✅ Dependencies installed
   - ✅ Static files collected
   - ✅ Database migrations applied
   - ✅ Server started successfully

### 6. Verify Deployment

Once deployed, your app will be available at:
```
https://car-dealership-portal.onrender.com
```

Test the following endpoints:
- `https://your-app.onrender.com/` - Homepage
- `https://your-app.onrender.com/admin/` - Django Admin
- `https://your-app.onrender.com/api/` - API endpoints

---

## 🔧 Configuration Details

### Build Process

The `build.sh` script automatically:
1. Installs dependencies from `requirements.txt`
2. Collects static files
3. Runs database migrations
4. Populates initial data

### Database

- **Type**: PostgreSQL 15
- **Plan**: Free (limited resources)
- **Auto-backups**: Not available on free tier
- **Connection**: Secured with SSL

### Server Configuration

- **Workers**: 4 Gunicorn workers
- **Timeout**: 120 seconds
- **Port**: Auto-assigned by Render ($PORT)
- **Health Check**: Root path (`/`)

### Security

Production security settings are automatically enabled:
- SSL redirect
- Secure cookies
- HTTPS proxy headers
- CORS configuration
- WhiteNoise for static files

---

## 🔄 Continuous Deployment

Render automatically redeploys when you push to the `main` branch:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Monitor deployment in the Render Dashboard → Logs tab.

---

## 🛠️ Troubleshooting

### Build Fails

**Check logs for:**
- Missing dependencies → Update `requirements.txt`
- Python version mismatch → Verify `PYTHON_VERSION` env var
- Permission issues → Ensure `build.sh` is executable

**Fix:**
```bash
chmod +x server/build.sh
git add server/build.sh
git commit -m "Fix build script permissions"
git push
```

### Database Connection Errors

1. Verify `DATABASE_URL` is set correctly
2. Check database status in Render Dashboard
3. Ensure database and web service are in the same region

### Static Files Not Loading

1. Check `STATIC_ROOT` and `STATIC_URL` in settings
2. Verify WhiteNoise middleware is enabled
3. Ensure `collectstatic` ran during build

### Application Errors

1. Check Render logs: Dashboard → Your Service → Logs
2. Verify environment variables
3. Check `DEBUG=False` is set
4. Review `ALLOWED_HOSTS` configuration

---

## 📊 Monitoring & Maintenance

### Logs

Access logs in Render Dashboard:
- **Build Logs**: Deployment process
- **Runtime Logs**: Application errors and info
- **Download**: Export logs for analysis

### Database Management

**Access PostgreSQL:**
1. Get connection string from Render Dashboard
2. Use any PostgreSQL client:
   ```bash
   psql <connection-string>
   ```

**Backup Database:**
```bash
pg_dump <connection-string> > backup.sql
```

### Scaling

**Free Tier Limitations:**
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month of runtime

**Upgrade Options:**
- Starter Plan: $7/month (always-on, no spin-down)
- Professional Plans: Better performance, resources

---

## 🌐 Custom Domain

To use a custom domain:

1. Go to Service Settings → Custom Domain
2. Add your domain (e.g., `www.yourdomain.com`)
3. Update DNS records with your domain provider:
   ```
   CNAME www <your-app>.onrender.com
   ```
4. Update `ALLOWED_HOSTS` environment variable

---

## 📝 Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] Admin panel accessible
- [ ] Database connected
- [ ] Static files serving correctly
- [ ] API endpoints working
- [ ] Authentication functional
- [ ] HTTPS enabled
- [ ] Environment variables set
- [ ] Logs monitoring configured
- [ ] Auto-deploy enabled

---

## 🔐 Security Best Practices

1. **Secret Key**: Always use generated value, never commit to Git
2. **DEBUG**: Must be `False` in production
3. **ALLOWED_HOSTS**: Specify exact domains
4. **Database**: Use strong passwords
5. **HTTPS**: Always enabled on Render
6. **Environment Variables**: Store sensitive data only in Render Dashboard

---

## 📞 Support

- **Render Documentation**: https://render.com/docs
- **Render Community**: https://community.render.com
- **Django Documentation**: https://docs.djangoproject.com

---

## 🎉 Success!

Your Car Dealership Portal is now live on Render!

**Next Steps:**
1. Test all functionality
2. Set up monitoring/alerts
3. Configure custom domain (optional)
4. Share your live URL!

**Live URL**: `https://car-dealership-portal.onrender.com`
