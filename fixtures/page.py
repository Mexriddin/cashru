from datetime import datetime
import pytest
from playwright.sync_api import Page, BrowserContext, Browser


@pytest.fixture(autouse=True)
def page(request, browser: Browser):
    context: BrowserContext = browser.new_context(
        viewport={"width": 1920, "height": 2080}
    )
    page: Page = context.new_page()
    request.cls.page = page
    yield page
    page.close()
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get("page")
        take_screenshot(page, item.nodeid)


def take_screenshot(page, nodeid: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{nodeid}_{now}.png".replace("/", "_").replace("::", "__")
    file_path = f"screenshots/{filename}"
    page.screenshot(path=file_path)