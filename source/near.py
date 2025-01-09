from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize WebDriver
driver = webdriver.Chrome()

js_usernames = [
    "pcdogh.tg", "bybit_suppor.tg", "7937417952.tg", "mahojabin090.tg", "jahidur19.tg",
    "h2on06.tg", "6517864089.tg", "binanc_toke.tg", "moneysoul1.tg", "kop_23456.tg",
    "mulakop.tg", "ramkop123.tg", "kopmama1234.tg", "texiumq.tg", "sxnium.tg",
    "ramthapkup.tg", "scnium.tg", "oxygen_hacker.tg", "7512938900.tg", "metasoul77.tg",
    "jsmetasoul.tg", "durga0_0.tg", "jdmm999.tg", "cs2skintop.tg", "xepsiam.tg",
    "emptysoul77.tg", "tentifires.tg", "xenomorph234.tg", "xepsiam1.tg", "ndearium.tg",
    "rentunium.tg", "vetarium.tg", "kallu_123456.tg", "dipsd77.tg", "gptopena.tg",
    "dev969696.tg", "jomonatv2.tg", "deshtv77.tg", "7547148001.tg", "bhaskarbro77.tg",
    "bangladesh852.tg", "hungrysoul77.tg", "refersell1234.tg", "djkallu12345.tg",
    "xenicius.tg", "bendradox.tg", "foxzium.tg", "cross_wallets.tg","ayanokoji80.tg","ayanabdulh.tg","faysalbh.tg","ayannokoji80.tg",
        "faysalhot1.tg","faysalhot2.tg","faysalhot3.tg","6701489175.tg",
        "7044785100.tg","6586505076.tg","mentanium.tg","teterium1.tg",
        "fentaniu.tg","henatrium.tg","oterium.tg","solarium12.tg","utirium.tg",
        "rentiums.tg","penetrium.tg","jetrify.tg","metafunky.tg","heyperium.tg","keterium.tg",
        "phentasiam.tg","melvodium.tg"
]

total = []
count=0
for user in js_usernames:
    try:
        url = f"https://nearvalidate.org/address/{user}"
        driver.get(url)
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        balance_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//div[h2[text()='Balance']]/span/p[@class='font-heading font-medium text-[26px]'])[2]")))
        balance1 = balance_element.text
        balance=balance1.split()[0]

        balance_float = float(balance)
        total.append(balance_float)

        print(f"{user} Balance:", balance_float)
        count=count+1

    except Exception as e:
        print(f"Error fetching balance for {user}:")
        # print(f"{user} This wallet's balance not Showing,Try again")



nearurl="https://nearblocks.io/charts/near-price"
driver.get(nearurl)
near_element = driver.find_element(By.XPATH, "//p[@class='text-sm text-gray-500 dark:text-neargray-10 font-medium leading-6 px-1']")
raw_price=near_element.text.replace("$", "").strip()
price=float(raw_price)

driver.quit()




print("----------------------------------------------------------")

print(f"Total Hot wallet counted {count}/{len(js_usernames)}")
print("Total Near available:", sum(total),"Near")
print(f"The current price of near is: {price}$")
print(f'Available USDT {sum(total)*price}$')
print(f'Available BDT {sum(total)*price*130} Tk')
