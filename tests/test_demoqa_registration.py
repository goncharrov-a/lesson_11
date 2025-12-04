from pathlib import Path

from pages.practice_form_page import PracticeFormPage

FIRST_NAME = 'Luke'
LAST_NAME = 'Skywalker'
EMAIL = 'example.user@mail.ru'
GENDER = 'Male'
PHONE = '9990003388'

BIRTH_DAY = '15'
BIRTH_MONTH = 'January'
BIRTH_YEAR = '1992'

SUBJECT_1 = 'Maths'
SUBJECT_2 = 'Computer Science'

HOBBY_1 = 'Sports'
HOBBY_2 = 'Reading'
HOBBY_3 = 'Music'

ADDRESS = 'Tatooine home'
STATE = 'NCR'
CITY = 'Delhi'

FILE = Path(__file__).parent / 'resources' / 'image.png'
FILE_NAME = FILE.name

EXPECTED_DOB = f'{BIRTH_DAY} {BIRTH_MONTH},{BIRTH_YEAR}'
EXPECTED_STATE_CITY = f'{STATE} {CITY}'


def test_demo_qa_pom():
    page = PracticeFormPage().open()

    page.fill_name(FIRST_NAME, LAST_NAME) \
        .set_email(EMAIL) \
        .set_phone(PHONE) \
        .set_dob(BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR) \
        .set_gender(GENDER) \
        .add_subject(SUBJECT_1) \
        .add_subject(SUBJECT_2) \
        .select_hobby(HOBBY_1) \
        .select_hobby(HOBBY_2) \
        .select_hobby(HOBBY_3) \
        .upload_picture(str(FILE)) \
        .set_address(ADDRESS) \
        .select_state_city(STATE, CITY) \
        .submit()

    page.should_see_modal() \
        .should_have_row('Student Name', f'{FIRST_NAME} {LAST_NAME}') \
        .should_have_row('Student Email', EMAIL) \
        .should_have_row('Gender', GENDER) \
        .should_have_row('Mobile', PHONE) \
        .should_have_row('Date of Birth', BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR) \
        .should_have_row('Subjects', SUBJECT_1) \
        .should_have_row('Subjects', SUBJECT_2) \
        .should_have_row('Hobbies', HOBBY_1) \
        .should_have_row('Hobbies', HOBBY_2) \
        .should_have_row('Hobbies', HOBBY_3) \
        .should_have_row('Picture', FILE_NAME) \
        .should_have_row('Address', ADDRESS.replace('\n', ' ')) \
        .should_have_row('State and City', STATE, CITY) \
        .close()
