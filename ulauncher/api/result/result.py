from typing import Callable, Optional

from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.api.shared.query import Query
from ulauncher.utils.text_highlighter import highlight_text

OnEnterCallback = Optional[Callable[[Query], Optional[BaseAction]]]


# pylint: disable=too-many-instance-attributes
class Result:

    ICON_SIZE = 40
    UI_FILE = 'result'
    name = None  # type: str
    description = None  # type: str
    keyword = None  # type: str
    icon = None  # type: Optional[str]
    _on_enter = None  # type: OnEnterCallback
    _on_alt_enter = None  # type: OnEnterCallback
    highlightable = False  # type: bool
    searchable = False  # type: bool

    # pylint: disable=too-many-arguments
    def __init__(self,
                 name: str = '',
                 description: str = '',
                 keyword: str = '',
                 icon: str = None,
                 highlightable: bool = None,
                 on_enter: OnEnterCallback = None,
                 on_alt_enter: OnEnterCallback = None):
        if not isinstance(name, str):
            raise TypeError(f'"name" must be of type "str", "{type(name).__name__}" given')
        if not isinstance(description, str):
            raise TypeError(f'"description" must be of type "str", "{type(description).__name__}" given')
        if not isinstance(keyword, str):
            raise TypeError(f'"keyword" must be of type "str", "{type(keyword).__name__}" given')
        self.name = name
        self.description = description
        self.keyword = keyword
        self.icon = icon
        if highlightable is not None:
            self.highlightable = highlightable
        self._on_enter = on_enter
        self._on_alt_enter = on_alt_enter

    def get_keyword(self) -> str:
        return self.keyword

    def get_name(self) -> str:
        return self.name

    def get_icon(self) -> Optional[str]:
        return self.icon

    def get_name_highlighted(self, query: Query, color: str) -> Optional[str]:
        if query and self.highlightable:
            return highlight_text(
                query if not self.keyword else query.argument,
                self.name,
                open_tag=f'<span foreground="{color}">',
                close_tag='</span>'
            )
        # don't highlight if query is empty
        return self.name

    # pylint: disable=unused-argument
    def get_description(self, query: Query) -> str:
        return self.description

    def on_enter(self, query: Query) -> Optional[BaseAction]:
        """
        Handle the main action
        """
        return self._on_enter(query) if callable(self._on_enter) else None

    def on_alt_enter(self, query: Query) -> Optional[BaseAction]:
        """
        Handle the optional secondary action (alt+enter)
        """
        return self._on_alt_enter(query) if callable(self._on_alt_enter) else None
