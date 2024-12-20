
# Weather App

Weather App is a Python-based desktop application that provides real-time weather information for various cities. It uses a PyQt-powered user interface, retrieves data from weather APIs, and offers recommendations based on current weather conditions. The app uses a `.csv` database for data management.

## Features
- Real-time weather data for multiple cities
- Recommendations based on weather, temperature, humidity, and windspeed
- User-friendly PyQt interface
- Supports international city names and IATA codes

## Installation

### For Regular Users

If you just want to use the app, follow these steps:

1. Go to the `executables` folder.
2. Download the appropriate version of the app for your system:
   - For Windows: `Weather App.exe`
   - For Linux: `Weather App`
3. Run the downloaded file to launch the application.

### For Developers

To build or modify the application, follow these steps:

#### Prerequisites
- Python 3.x
- Virtual Environment (optional but recommended)
- Required Python packages listed in `requirements.txt`

#### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd weather-app
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the app:
    ```bash
    cd ./app
    python ./main_window.py
    ```

## License Agreement
This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

It is free for personal or commercial use with attribution required by mentioning the use of this work as follows: 

> This site or product includes IP2Location™ ISO 3166-2 Subdivision Code which is available from [IP2Location](https://www.ip2location.com).

## Contributors
- **@ThePatrickCastle** - Lead Developer & Project Manager
- **@C4mdax** - Database Architect & Graphic Designer Strategist
- **@Edgar Salgado González** - UI/UX Designer & Usability Analyst

## Contributing
Contributions are welcome! Please follow the typical fork-branch-pull request model. Make sure to check any open issues before starting your work.

## Contact
For any questions or suggestions, please reach out at **patriciosalvador@ciencias.unam.mx**.
