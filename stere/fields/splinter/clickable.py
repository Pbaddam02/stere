from stere.browser_spy import XHRSpy
from stere.utils import _retry

from ..decorators import stere_performer, use_after, use_before
from ..field import Field


@stere_performer('click', consumes_arg=False)
class Clickable(Field):
    """Convenience Class on top of Field.

    Implements `click()` as its performer.
    """

    xhr_spy = XHRSpy()

    def wait_for_page_load(self):
        """Wait for browser to finish loading content."""
        return self.browser.evaluate_script(
            "document.readyState === 'complete'")

    def after(self):
        """Wait for page to be silent."""
        # Wait for page load
        loaded = _retry(self.wait_for_page_load)
        if not loaded:
            raise TimeoutError('Page did not finish loading.')

        # Wait for network requests
        self.xhr_spy.add()
        self.xhr_spy.wait_for_no_activity()

    @use_after
    @use_before
    def click(self) -> None:
        """Use Splinter's click method.

        Example:

            >>> purchase = Clickable('id', 'buy_button')
            >>> purchase.click()

        """
        self.is_visible()
        self.is_clickable()
        self.find().click()
