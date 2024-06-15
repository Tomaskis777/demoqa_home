# from pages.base_page import BasePage
# from selenium.common.exceptions import NoSuchElementException
#
# class SwagLabs(BasePage):
#
#     def exist_icon(self):
#         try:
#             self.find_element(locator='div.login_logo')
#         except NoSuchElementException:
#             return False
#         return True
#
#     def find_name(self):
#         try:
#             self.find_element(locator='user-name')
#         except NoSuchElementException:
#             return False
#         return True
#
#     def find_password(self):
#         try:
#             self.find_element(locator='password')
#         except NoSuchElementException:
#             return False
#         return True
#
#     # def get_text(self):
#     #     try:
#     #         self.find_element(locator='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.').text
#     #     except NoSuchElementException:
#     #         return False
#     #     return True
