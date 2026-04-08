import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
    template_folder=os.path.join(BASE_DIR, 'templates', 'malefashion-master'),
    static_folder=os.path.join(BASE_DIR, 'templates', 'malefashion-master'),
    static_url_path=''
)
from datetime import datetime

def convert_date_format(date_string, current_format):
    """
    Converts a date string from a given format to 'YYYY-MM-DD'.
    
    Args:
        date_string (str): The date string to convert (e.g., '12/31/2023').
        current_format (str): The format of the input string (e.g., '%m/%d/%Y').
        
    Returns:
        str: The date in 'YYYY-MM-DD' format, or an error message if parsing fails.
    """
    try:
        # Convert the string to a datetime object based on its current format
        date_obj = datetime.strptime(date_string, current_format)
        
        # Convert the datetime object to the new 'YYYY-MM-DD' format
        new_format = date_obj.strftime('%Y-%m-%d')
        return new_format
    except ValueError as e:
        return f"Error parsing date: {e}"

# --- Examples ---
print(convert_date_format("12/31/2023", "%m/%d/%Y"))    # Output: 2023-12-31
print(convert_date_format("31-12-2023", "%d-%m-%Y"))    # Output: 2023-12-31
print(convert_date_format("Jan 15, 2024", "%b %d, %Y")) # Output: 2024-01-15


# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)