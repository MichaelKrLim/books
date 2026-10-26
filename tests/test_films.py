from playwright.sync_api import Page, expect
from lib.seed import seed

def test_list_elements_in_films_page(page: Page):
    seed('seeds/reset_films.sql')
    page.goto('http://127.0.0.1:5002/films')
    expect(page.locator("li")).to_have_text([
        'title: The Gruffalo, release year: 2009',
        'title: Ada Twist, Scientist, release year: 2021',
        'title: The Girl Who Drank the Moon, release year: 2020', 'title: Dragons in a Bag, release year: 2019'
    ])
