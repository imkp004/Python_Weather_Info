# Python_Weather_Info

**Project Name: WeatherApp**

**Description:**
The WeatherApp is a simple web application that allows users to retrieve weather information for a specified city. It leverages the OpenWeatherMap API to fetch real-time weather data and presents it in a user-friendly interface. The application is built using Python, Flask, HTML, CSS, and JavaScript.

**Key Features:**
1. **User Input:** The application prompts the user to input a city name through a text input field.
2. **Weather Information Display:** Upon entering a city name and clicking the "Get Weather" button, the app fetches weather data from the OpenWeatherMap API.
3. **Temperature Conversion:** The temperature data retrieved from the API, provided in Kelvin, is converted to Fahrenheit for better user understanding.
4. **Dynamic UI Updates:** The application dynamically updates the UI to display the weather description and temperature without requiring a page refresh.
5. **Exit Functionality:** Users can type 'stop' in the input field and click the "Stop App" button to exit the application.

**Technologies Used:**
- **Python:** Used for server-side scripting and application logic.

**How to Run the Project:**
1. Install Flask by running `pip install Flask` in your terminal.
2. Save the provided Python code in a file named `app.py`.
3. Run the script by executing `python app.py` in the terminal.

**Project Structure:**
- `Weather.py`: Python script containing the Flask application and server logic.

This project provides a basic foundation that can be expanded and enhanced with additional features, such as multiple city support, more detailed weather information, and improved user interactions.
