from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Stillingar
number_of_rounds = 3600
name = 'github.com/thrkll/kvizz-bot'
email = 'free_burger_generator@protonmail.com'
phone = '5554433'

# Opnar Firefox
driver = webdriver.Firefox()

def main():
    email_combos = dot_combinations(email)
    open_kvizz()

    win_count = 0
    for round in range(number_of_rounds):
        # Prentar tölfræði um hvað er búið að spila og vinna marga leiki
        print(f'Rounds: {round + 1}/{number_of_rounds}\tWins: {win_count}',
            end='\r')

        kvizz_setup(name, email_combos, phone)
        answers = read_answers()

        for each_question in range(5):
            question_page(answers)
            time.sleep(2)
        outcome = play_again()
        win_count += outcome

def read_answers():
    # Les svör úr answers.csv og vistar í answers
    answers = []
    with open('answers.csv', encoding='utf-8') as f:
        for line in f:
            answers.append(line.rstrip('\n'))
    return answers

def open_kvizz():
    driver.get('https://kvizz.olis.is')

    # Vafrakökur samþykktar (glugginn obscurar í question_page)
    element = element_maker('button.ch2-btn:nth-child(1)')
    element.click()

def email_manipulator(email_combos):
    # Email nr. 2 í lista verður email nr. 1 í næsta leik o.s.frv.
    email = email_combos[0]
    del email_combos[0]
    return email

def kvizz_setup(name, email_combos, phone):
    # Setur inn nafn
    element = element_maker('#name')
    element.clear()
    element.send_keys(name)

    # Setur inn tölvupóstfang
    email = email_manipulator(email_combos)
    element = element_maker('#email')
    element.clear()
    element.send_keys(email)

    # Setur inn símanúmer
    element = element_maker('#phone')
    element.clear()
    element.send_keys(phone)

    # Setur inn aldur
    element = element_maker('#age')
    Select(element).select_by_value('20')

    # Checkar í skilmála-boxið
    element = element_maker('#terms')
    if not element.is_selected():
        element.click()

    # Ýtir á Skrá mig til leiks
    element = element_maker('button.btn:nth-child(7)')
    element.click()

    # (Á næstu síðu) Ýtir á Byrja
    element = element_maker('button.btn-primary:nth-child(4)')
    element.click()

def question_page(answers):
    # Les svarmöguleika og velur svar ef það er í answers
    for option in range(1,5):
        element = element_maker(
            f'.question-options > li:nth-child({option}) > a:nth-child(1)')
        if element.text in answers:
            element.click()
            return

    # Ef svar er ekki í answers er síðasti valmöguleiki valinn (random)
    element.click()

    # Athugar hvort random möguleikinn hafi verið réttur
    css_sl = '.question-options > li:nth-child(4)'
    element = driver.find_element_by_css_selector(css_sl)
    option_text = element.text
    result = element.get_attribute("class")

    # Ef hann var réttur er honum bætt við answers.csv
    if 'correct' in result:
        with open('answers.csv', 'a', encoding='utf-8') as f:
            f.write(option_text + '\n')

def play_again():
    element = element_maker('a.btn-block:nth-child(2)')

    # Athugar hvort umferðin hafi skilað vinningi
    try:
        driver.find_element_by_css_selector('.prize')
        outcome = 1
    except:
        outcome = 0

    # Ýtir á Spila aftur og lokar lúppunni
    element.click()
    return outcome

def element_maker(css_sl):
    # Bíður eftir að loader verði 'display: none'
    while True:
        if not driver.find_elements_by_class_name('loader')[0].is_displayed():
            break

    return WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_sl)))

def dot_combinations(email):
    # Skilar lista af emails með punktum. T.d.
    #   f.ree_burger_generator
    #   f.r.ree_burger_generator
    #   ...
    # Bottinn getur spilað ca. 3600 leiki á dag. Til að email verði ekki endur-
    # tekið þarf fyrri hluti emails að vera a.m.k. 13 stafir (2^12 = 4096)
    # https://stackoverflow.com/a/50023811

    temp, email_second = email.split('@')

    count = 0
    combinations = []
    while count.bit_length() < len(temp):
        current_word = []
        for index, letter in enumerate(temp):
            current_word.append(letter)
            if (1 << index) & count:
                current_word.append(".")

        email_first = "".join(current_word)
        email = email_first + '@' + email_second
        combinations.append(email)
        count += 1

        # Óþarft að búa til fleiri samsetningar en fjöldi umferða sem á að spila
        if count == number_of_rounds:
            break

    return combinations

main()
