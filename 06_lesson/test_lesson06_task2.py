from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "NDk3N2NmNzMtMjFjMi00MWU3LTg2NGItNDg1NjRhNzYyZDE2",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # 3. Обновите страницу
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/subzero")

    # 5. Сохраните текущий URL
    user1_url = driver.current_url

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # 7. Установите cookie пользователя 2
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "NmQ2ZmIxM2EtNzdmOS00NTFjLWE3NjktOGNkMmI3OTA5ZGM2",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # 8. Обновите страницу
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/scorpion123145")

    # 10. Сохраните текущий URL
    user2_url = driver.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert user1_url != user2_url, f"URL пользователей совпадают: {user1_url}"

    driver.quit()
