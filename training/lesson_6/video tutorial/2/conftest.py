# import pytest
# from playwright.sync_api import Page
#
#
# @pytest.fixture()
# def main_page(page: Page):
#     page.set_viewport_size({"width": 1920, "height": 1080})
#     page.goto("https://gitflic.ru/")
#
#     cookies_to_add = [
#         {
#             "name": "SESSION",
#             "value": "NzYyZmJiZjctZjRmZi00OTA4LThkNDYtMWY4ZmUyZTY0OGU0",
#             "domain": "gitflic.ru",
#             "path": "/"
#         },
#         {
#             "name": "cookiesAccepted",
#             "value": "true",
#             "domain": "gitflic.ru",
#             "path": "/"
#         }]
#     page.context.add_cookies(cookies_to_add)
#     page.reload()
#     page.wait_for_load_state("networkidle")
#
#     return page
