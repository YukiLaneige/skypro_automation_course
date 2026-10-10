import faker
import config
from ..pages.profile_page import ProfilePage

Faker = faker.Faker()
first_name = Faker.first_name()
last_name = Faker.last_name()
full_name = f"{first_name} {last_name}"


def test_change_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    profile.update_profile(first_name, last_name)
    profile.open_profile_page("airsworld")

    assert profile.get_user_name() == full_name, \
        "Имя профиля не было обновлено"


def test_check_profile_name(driver):
    profile = ProfilePage(driver, config.BASE_URL)
    profile.open_profile_page("airsworld")
    name = profile.get_user_name()

    assert name != "", "Имя профиля должно быть не пустым"
    assert len(name) > 0, "Имя профиля должно содержать хотя бы один символ"
