import sublime
import sublime_plugin
from base64 import b64decode, b64encode


class B64decCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region)
                text = b64decode(text.encode('utf-8'))
                self.view.replace(edit, region, text.decode())


class B64encCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region)
                text = b64encode(text.encode('utf-8'))
                self.view.replace(edit, region, text.decode())
