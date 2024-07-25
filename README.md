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

## Getting Started

### Installation

1. Clone the repository:

```sh
git clone https://github.com/turhancan97/wedding-invitation.git
cd wedding-invitation
```

2. Install the dependencies:

```
conda env create -f environment.yml
conda activate wedding-invitation
```

3. Create a .env file and set the following environment variables:

```sh
GOOGLE_FORM_ID = 'YOUR_GOOGLE_FORM_ID'
GOOGLE_FORM_NAME_FIELD = 'YOUR_GOOGLE_FORM_NAME_FIELD'
GOOGLE_FORM_ATTENDANCE_FIELD = 'YOUR_GOOGLE_FORM_ATTENDANCE_FIELD'
GOOGLE_FORM_OTHER_FIELD = 'YOUR_GOOGLE_FORM_OTHER_FIELD'
```

3.1. How to get Google Form:

3.2. How to get Google Form ID and Field Names:


4. Create a `guests.json` file with the following structure:

```json
[
    "John",
    "Jane",
    "Uncle_Bob",
    "Aunt_Mary",
    "Mr_Smith",
    "Mrs_Smith",
    "Billy_with_an_other_person"
]
```

5. Run the application locally:

```sh
python app.py
```

6. Deploy the application to Heroku (check the [Heroku documentation](https://devcenter.heroku.com/articles/getting-started-with-python)):

```sh
heroku login
git add .
git commit -am "make it better"
git push heroku main
```

7. Customization:

* **HTML Templates:** Modify the HTML templates in the templates directory to customize the look and feel of the website.
* **CSS:** Update static/css/style.css to change the styling.

## Contributing

Feel free to fork this repository and make your own enhancements. Pull requests are welcome.

## License