#!/bin/bash
# Post-deployment script for Render
# This script runs after successful deployment

echo "🎉 Deployment successful!"
echo "📊 Application Status:"
echo "- Django version: $(python -m django --version)"
echo "- Database: PostgreSQL (via DATABASE_URL)"
echo "- Static files: Collected"
echo "- Migrations: Applied"

# Check if superuser exists (optional)
echo ""
echo "⚠️  Remember to create a superuser for admin access:"
echo "   python manage.py createsuperuser"
