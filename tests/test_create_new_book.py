from playwright.sync_api import Page, expect
from lib.seed import seed

def test_create_new_book(page: Page):
    seed("seeds/reset_books.sql")

    page.goto("http://localhost:5002/books")
    page.get_by_label("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_label("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]

    assert new_book == "title: The Chroicles of Geronimo (the cat), author: Geronimo"
