from flask import Flask, render_template, request, redirect, url_for, abort
import requests
import json

# Initialize Flask app
app = Flask(__name__)

# Load guest names from JSON file
with open('guests.json') as f:
    names = json.load(f)

def adjust_name(guest_name):
    if 'Wujek_' in guest_name or 'Ciocia_' in guest_name:
        # delete 'Wujek' or 'Ciocia' from the guest name
        guest_name = guest_name.replace('Wujek_', 'Wujek ').replace('Ciocia_', 'Ciocia ')
    if '_z_osoba_towarzyszaca' in guest_name:
        # delete '_z_osoba_towarzyszaca' from the guest name
        guest_name = guest_name.replace('_z_osoba_towarzyszaca', ' z osobą towarzyszącą')
    if 'Pan_' in guest_name or 'Pani_' in guest_name:
        guest_name = guest_name.replace('Pan_', 'Pan ').replace('Pani_', 'Pani ')
    # split guest names by underscore
    guest_names = guest_name.split('_')
    # # capitalize each name
    # guest_names = [name.capitalize() for name in guest_names]
    # join guest names with space and add 'and' before the last name
    display_name = ' i '.join(', '.join(guest_names).rsplit(', ', 1))
    return display_name

# Google Form action URL and field names
id_ = '1FAIpQLSdi897ORN2YPNSvG7Yagh1yRN1KKDJU5ORbdNZQ9KrHYfjqqg'
x_ = '2006475847'
y_ = '455591977'
z_ = '245816835'
GOOGLE_FORM_ACTION = f"https://docs.google.com/forms/d/e/{id_}/formResponse"
GOOGLE_FORM_NAME_FIELD = f"entry.{x_}"
GOOGLE_FORM_ATTENDANCE_FIELD = f"entry.{y_}"
GOOGLE_FORM_OTHER_FIELD = f"entry.{z_}"

# Homepage route
@app.route('/')
def home():
    return render_template('home.html')

# Guest route with updated logic for multiple guests
@app.route('/<guest_name>', methods=['GET', 'POST'])
def guest(guest_name):
    if guest_name not in names:
        return abort(404)

    display_name = adjust_name(guest_name)

    if request.method == 'POST':
        # Extract attendance information from the form
        attendance = request.form.get(GOOGLE_FORM_ATTENDANCE_FIELD)
        answer = request.form.get(GOOGLE_FORM_OTHER_FIELD)

        # Prepare data for submission to Google Forms
        form_data = {
            GOOGLE_FORM_NAME_FIELD: display_name,
            GOOGLE_FORM_ATTENDANCE_FIELD: attendance,
            GOOGLE_FORM_OTHER_FIELD: answer,
        }
        # Submit data to Google Forms
        response = requests.post(GOOGLE_FORM_ACTION, data=form_data)
        if response.status_code == 200:
            # Redirect to the custom confirmation page on successful submission
            return redirect(url_for('confirmation', guest_name=guest_name))
        else:
            # Handle submission error
            return "There was an error submitting your response. Please try again."

    return render_template('guest.html', guest_name=display_name,
                           google_form_action=GOOGLE_FORM_ACTION,
                           name_field=GOOGLE_FORM_NAME_FIELD,
                           attendance_field=GOOGLE_FORM_ATTENDANCE_FIELD,
                           other_field=GOOGLE_FORM_OTHER_FIELD)

@app.route('/confirmation/<guest_name>')
def confirmation(guest_name):
    if guest_name not in names:
        return abort(404)
    guest_name = adjust_name(guest_name)
    # Display the wedding details and a personalized message
    return render_template('confirmation.html', guest_name=guest_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
