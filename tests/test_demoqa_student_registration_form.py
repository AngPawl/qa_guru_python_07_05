import os
from selene import browser, command, have


def test_open():
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test_email.demoqa@test.com')

    browser.element('#genterWrapper [for="gender-radio-1"]').click()

    browser.element('#userNumber').type('8800111111')

    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('[class="react-datepicker__month-select"]').click().element(
        'option[value = "0"]'
    ).click()
    browser.element('[class="react-datepicker__year-select"]').click().element(
        'option[value = "2000"]'
    ).click()
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsInput').type('computer').press_tab()

    browser.element('#hobbiesWrapper [for="hobbies-checkbox-1"]').perform(
        command.js.scroll_into_view
    ).click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath('resources/student.png')
    )

    browser.element('#currentAddress').type(
        '42 Best street, suite 1, Dallas, TX, 11111'
    ).press_tab()

    browser.element('#stateCity-wrapper #state').click().element('input').type(
        'NCR'
    ).press_tab()

    browser.element('#stateCity-wrapper #city').click().element('input').type(
        'Delhi'
    ).press_tab()

    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )
    browser.element('.table').should(have.text('John Doe'))
    browser.element('.table').should(have.text('test_email.demoqa@test.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('8800111111'))
    browser.element('.table').should(have.text('01 January,2000'))
    browser.element('.table').should(have.text('Computer Science'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('student.png'))
    browser.element('.table').should(
        have.text('42 Best street, suite 1, Dallas, TX, 11111')
    )
    browser.element('.table').should(have.text('NCR Delhi'))
