from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss


class PracticeFormPage:
    first_name = s('#firstName')
    last_name = s('#lastName')
    email = s('#userEmail')
    phone = s('#userNumber')
    dob_input = s('#dateOfBirthInput')

    subjects_input = s('#subjectsInput')

    upload_input = s('#uploadPicture')
    address_textarea = s('#currentAddress')

    state_container = s('#state')
    state_input = s('#react-select-3-input')
    city_container = s('#city')
    city_input = s('#react-select-4-input')

    submit_btn = s('#submit')

    modal = s('.modal-content')
    modal_title = s('#example-modal-sizes-title-lg')
    modal_rows = ss('.modal-content tbody tr')
    close_modal = s('#closeLargeModal')

    def gender_label(self, text: str):
        return s(f'//label[text()="{text}"]')

    def hobby_label(self, text: str):
        return s(f'//label[text()="{text}"]')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self, first: str, last: str):
        self.first_name.type(first)
        self.last_name.type(last)
        return self

    def set_email(self, value: str):
        self.email.type(value)
        return self

    def set_phone(self, value: str):
        self.phone.type(value)
        return self

    def set_gender(self, value: str):
        self.gender_label(value).click()
        return self

    def set_dob(self, day: str, month: str, year: str):
        self.dob_input.click()
        s('.react-datepicker__month-select').click()
        ss('.react-datepicker__month-select option').element_by(have.text(month)).click()
        s('.react-datepicker__year-select').click()
        ss('.react-datepicker__year-select option').element_by(have.text(year)).click()
        ss('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
            .element_by(have.exact_text(day)).click()
        return self

    def add_subject(self, subject: str):
        self.subjects_input.type(subject[:2])
        ss('.subjects-auto-complete__menu-list div').element_by(have.text(subject)).click()
        return self

    def select_hobby(self, hobby: str):
        self.hobby_label(hobby).click()
        return self

    def upload_picture(self, file_path: str):
        self.upload_input.send_keys(file_path)
        return self

    def set_address(self, text: str):
        self.address_textarea.type(text)
        return self

    def select_state_city(self, state: str, city: str):
        self.state_container.click()
        self.state_input.type(state).press_enter()
        self.city_container.click()
        self.city_input.type(city).press_enter()
        return self

    def submit(self):
        self.submit_btn.click()
        return self

    def should_see_modal(self):
        self.modal.should(be.visible)
        self.modal_title.should(have.text('Thanks for submitting the form'))
        return self

    def should_have_row(self, label: str, *texts: str):
        cell = self.modal_rows.element_by_its('td:first-child', have.exact_text(label)) \
            .element('td:nth-child(2)')
        for t in texts:
            cell.should(have.text(t))
        return self

    def close(self):
        self.close_modal.click()
        return self
