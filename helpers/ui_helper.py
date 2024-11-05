from playwright.sync_api import Page, expect


class UiHelper:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def open(self):
        self.page.goto(self._PAGE_URL, wait_until="domcontentloaded", timeout=50000)

    def shadow_root(self, shadow_host_loc):
        shadow_host = self.page.wait_for_selector(f"css={shadow_host_loc}", state="visible", timeout=100000)
        root = shadow_host.evaluate_handle("element => element.shadowRoot").as_element()
        return root