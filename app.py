import random
from flask import Flask, render_template
# from hospitals_string_data import generate_hospitals_Data_to_HTML
# from covid_centers_string_data import generate_covid_centers_Data_to_HTML

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/form')
def form_page():
    return render_template('includes/form.html')

# func 1 - SOS route
@app.route('/nearest-hospitals', methods=['GET', 'POST'])
def show_nearest_hospitals():
    # stores data into a long html string
    final_hospitals_html = generate_hospitals_Data_to_HTML()
    # print(final_hospitals_html)
    return final_hospitals_html

# func 2 - get nearby covid centers route
@app.route('/covid-centers', methods=['GET', 'POST'])
def show_covid_centers():
    # stores data into a long html string
    final_covid_html = generate_covid_centers_Data_to_HTML()
    # print(final_covid_html)
    return final_covid_html


# # repl run
# # # to run the app via terminal
# if __name__ == "__main__":
#     app.run(
#             host='0.0.0.0',
#             port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
#             debug=True
#         )

# to run the app via terminal
if __name__ == "__main__":
    app.run(debug=False)
