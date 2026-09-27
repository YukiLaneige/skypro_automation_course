import faker
from playwright.sync_api import expect


def test_update_change_name(main_page):
    # Перейти на страницу профиля
    main_page.goto("https://gitflic.ru/user/airsworld")
    main_page.screenshot(path="screenshots/full_page.png")

    # Нажать кнопку редактирования профиля
    main_page.locator(".user-profile__edit").click()

    # Изменить Ф и И в форме
    user_name = faker.Faker().first_name()
    main_page.locator("#name").fill(user_name)

    user_surname = faker.Faker().last_name()
    main_page.locator("#surename").fill(user_surname)

    # Сохранить изменения
    main_page.locator(".gf-button.--success").click()

    # Вернуться на страницу профиля
    main_page.goto("https://gitflic.ru/user/airsworld")
    main_page.screenshot(path="screenshots/full_page_after.png")

    # Ожидаемый результат: Ф и И успешно изменены и
    # отображается на странице профиля
    user_name_main = main_page.locator("h6.mb-0")
    user_name_main.screenshot(path="screenshots/user_name.png")

    expect(user_name_main).to_have_text(user_name+" "+user_surname)
