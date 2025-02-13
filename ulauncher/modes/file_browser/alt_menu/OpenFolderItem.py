from ulauncher.api import SmallResult
from ulauncher.api.shared.action.OpenAction import OpenAction


class OpenFolderItem(SmallResult):
    # pylint: disable=super-init-not-called
    def __init__(self, path: str, name='Open Folder'):
        self.path = path
        self.name = name
        self.icon = 'system-file-manager'

    def on_enter(self, query):
        return OpenAction(self.path)
