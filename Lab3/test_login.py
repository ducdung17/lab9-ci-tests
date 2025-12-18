import sys
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Thay đổi mã hóa của stdout để hỗ trợ Unicode
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cấu hình WebDriver cho Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mở trang đăng nhập
driver.get("https://online.mospolytech.ru/login/index.php")

# Cấu hình WebDriverWait để chờ phần tử
wait = WebDriverWait(driver, 10)

# Chờ trường nhập username xuất hiện và điền thông tin
username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Tìm phần tử có id="username"
username_input.send_keys("doducdung1701@gmail.com")  # Điền email vào ô username

# Chờ trường nhập password xuất hiện và điền thông tin
password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))  # Tìm phần tử có id="password"
password_input.send_keys("Anhdung2002")  # Điền mật khẩu vào ô password

# Gửi form đăng nhập (nhấn Enter)
password_input.send_keys(Keys.RETURN)

# Đợi và kiểm tra kết quả đăng nhập
try:
    # Chờ phần tử "Выйти" (nút đăng xuất) xuất hiện
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Выход']")))  # Thử dùng XPath thay vì LINK_TEXT
    print("Вход выполнен успешно!")
except:
    print("Ошибка входа")

# Đóng trình duyệt
driver.quit()
