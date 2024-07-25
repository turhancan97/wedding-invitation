# Wedding Invitation Website

This is a Flask-based web application for managing wedding invitations. Guests can confirm their attendance through a Google Form embedded in the website.

## Features
- Personalized invitation pages for each guest.
- Integration with Google Forms for attendance confirmation.
- Easy customization for different weddings.

## Project Structure
```
wedding-invitation
│
├── requirements.txt       # Dependencies for Heroku
├── guests.json            # List of guests
├── Procfile               # Heroku deployment file
├── runtime.txt            # Python version for Heroku
├── environment.yml        # Conda environment file
├── README.md              # Project documentation
├── app.py                 # Main application file
├── templates/             # HTML templates
│   ├── home.html
│   ├── guest.html
│   ├── confirmation.html
│   └── 404.html
└── static/
    └── css/
        └── style.css      # Custom CSS
```