# SRM Portal Automation Script

This repository contains a Python script that automates interactions with the SRM (Service Request Management) Portal using Selenium WebDriver. The script performs tasks such as logging in and logging out based on the network status displayed on the portal.

Features

- Automates login and logout functionality based on network status.
- Uses Selenium WebDriver to interact with the SRM Portal.
- Stores sensitive credentials (username, password, and portal URL) securely in a `.env` file.
- Configurable for use with Microsoft Edge browser via `msedgedriver.exe`.
- Includes error handling and basic logging.

## Prerequisites

Before running this script, you need to have the following installed:

- Python (>= 3.6)
- Selenium: Install via pip:
  ```bash
  pip install selenium
  ```
- python-dotenv: Install via pip:
  ```bash
  pip install python-dotenv
  ```
- Microsoft Edge WebDriver: Download it from the [official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in the same directory as the script or add its path to your system environment variables.
  
## Setup

### 1. Clone this Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/srm-portal-automation.git
cd srm-portal-automation
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory of the repository with the following format:

```
url=your_srm_portal_url
id=your_username
pass=your_password
```

Make sure to replace the values with your actual SRM portal URL, username, and password.

### 4. Place the WebDriver

Download the Microsoft Edge WebDriver (`msedgedriver.exe`) and place it in the same directory as the script, or ensure it's available in your system's `PATH`.

## Usage

Once you've set up everything, you can run the script using the following command:

```bash
python srm_automation.py
```

This will:

- Open the SRM portal.
- Check the network status.
- Log in if "Network Access Login" is detected.
- Log out and log in again if "Network Access Granted" is detected.

## Script Overview

- Imports: The script uses `selenium` for web automation and `python-dotenv` for environment variable management.
- WebDriver Setup: Configures Microsoft Edge WebDriver (`msedgedriver.exe`) and options to ignore certificate errors.
- Login & Logout: The script automates logging in or logging out based on the network status.
- Error Handling: Basic error handling is included in the script to catch issues during login, logout, or when locating web elements.
  
## Code Breakdown

- WebDriver Setup:
  The script uses Selenium to launch Microsoft Edge and navigate to the SRM portal.

- Network Status Check:
  The script checks the network status on the page using the element class name `usercheck_title_class`.

- Login Function:
  If the network status requires login, the script automates the login process by filling out the username and password fields.

- Logout Function:
  If the network status indicates access is granted, the script automates logging out.

- Decision Logic:
  Based on the network status, the script will log in or log out as necessary.

## Contributing

Feel free to open issues or submit pull requests if you encounter bugs, need improvements, or have suggestions for additional features.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Selenium WebDriver: Used for browser automation.
- python-dotenv: Used for securely loading environment variables.
  
## Contact

For any inquiries, you can reach me via:

- [GitHub Profile](https://github.com/your-username)
- [Email](mailto:your-email@example.com)

---

Happy automating! 🚀
