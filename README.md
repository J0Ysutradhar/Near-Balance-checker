# Near Wallet Balance Checker

This project is a Python script that uses Selenium to check the balance of multiple Near wallets and calculate the total balance in Near, USDT, and BDT.

## Prerequisites

- Python 3.12
- Google Chrome
- ChromeDriver
- Selenium

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/J0Ysutradhar/Near-Balance-checker.git
    cd bar
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium
    ```

3. Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system's PATH.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script:
    ```sh
    python source/near.py
    ```

## Documentation

The script performs the following steps:

1. Initializes the Selenium WebDriver.
2. Iterates through a list of Near wallet usernames.
3. For each username, navigates to the wallet's balance page and retrieves the balance.
4. Calculates the total balance in Near, USDT, and BDT.
5. Prints the results to the console.

### Example Output
Total Hot wallet counted 60/60 Total Near available: 1234.56 Near The current price of near is: 10.0$ Available USDT 12345.6$ Available BDT 1604928.0 Tk


## License

This project is licensed under the MIT License. See the LICENSE file for details.