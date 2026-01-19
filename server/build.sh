#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Populating initial data..."
python manage.py populate_data || echo "Warning: Could not populate data (may already exist)"

echo "Build completed successfully!"
