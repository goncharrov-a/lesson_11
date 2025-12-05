import allure
import pytest
from selene import browser

from data.demoqa_user_data import users
from pages.practice_form_page import PracticeFormPage
from utils import attach


@allure.epic("DemoQA")
@allure.feature("Practice Form")
@allure.story("Генерация пользователя через Faker и проверка заполнения формы")
@allure.tag("UI", "PracticeForm", "Faker", "Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "user",
    users,
    ids=lambda u: f"{u.first_name}_{u.last_name}",
)
def test_practice_form(setup_browser, user):
    page = PracticeFormPage()

    allure.dynamic.title(f"Заполнение Practice Form для {user.first_name} {user.last_name}")
    allure.dynamic.description(
        "Тест проверяет корректность заполнения Practice Form с использованием пользовательских "
        "данных, сгенерированных через Faker."
    )

    with allure.step("Открыть форму Practice Form"):
        page.open()

    with allure.step("Заполнить имя и фамилию"):
        page.fill_name(user.first_name, user.last_name)

    with allure.step("Заполнить email"):
        page.set_email(user.email)

    with allure.step("Заполнить номер телефона"):
        page.set_phone(user.phone)

    with allure.step("Выбрать пол"):
        page.set_gender(user.gender)

    with allure.step("Указать дату рождения"):
        page.set_dob(
            user.birth_day,
            user.birth_month,
            user.birth_year,
        )

    with allure.step("Добавить предметы"):
        for subject in user.subjects:
            page.add_subject(subject)

    with allure.step("Выбрать хобби"):
        for hobby in user.hobbies:
            page.select_hobby(hobby)

    with allure.step("Загрузить файл"):
        page.upload_picture(str(user.file_path))

    with allure.step("Заполнить адрес"):
        page.set_address(user.address)

    with allure.step("Выбрать штат и город"):
        page.select_state_city(user.state, user.city)

    with allure.step("Отправить форму"):
        page.submit()

    with allure.step("Проверить модальное окно и данные"):
        page.should_see_modal() \
            .should_have_row("Student Name", f"{user.first_name} {user.last_name}") \
            .should_have_row("Student Email", user.email) \
            .should_have_row("Gender", user.gender)

    with allure.step("Добавить вложения"):
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
