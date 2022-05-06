from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time


vacancies = []
driver = webdriver.Chrome('/home/nmxkik/python/selenium/chromedriver')

def save_file(vacancy):
    
    with open ("python_vacancies_list.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Название вакансии", "Название компании", "Зарплата", "Город", "Описание"])

        for vacancy in vacancies:
            writer.writerow((vacancy["vacancy_name"], vacancy['company_name'], vacancy['salary'], vacancy['city'], vacancy['description']))

def search_element(element, class_name):

    try:
        data = element.find_element(By.CLASS_NAME, class_name).text

    except:
        data = "Неизвестно"
    return data


def main():
    driver.get("https://jobs.dou.ua/vacancies/?category=Python")
    while True:
        try:
            driver.find_element(By.LINK_TEXT ,"Більше вакансій").click()
            time.sleep(0.1)
        except:
            break
    elements = driver.find_elements(By.CLASS_NAME, "vacancy")
    for element in elements:
        
        vacancy_name = search_element(element, "vt")
        company_name = search_element(element,"company")
        salary = search_element(element, "salary")
        city = search_element(element, "cities")
        description = search_element(element, "sh-info")

        vacancies.append({
            "vacancy_name" : vacancy_name,
            "company_name" : company_name,
            "salary" : salary,
            "city" : city,
            "description" : description
        })
    save_file(vacancies)
    driver.quit()

if __name__ == "__main__":
    main()