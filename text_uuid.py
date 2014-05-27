import sublime
import sublime_plugin
import uuid


class RandomUuidCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            self.view.replace(edit, region, uuid.uuid4().urn.lstrip('urn:uuid:'))


class DomainUuidCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, region, make_v5_uuid(uuid.NAMESPACE_DNS, self.view.substr(region)))


class TextUuidCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        namespace_setting = self.view.settings().get('namespace_uuid', None)
        if namespace_setting:
            try:
                namespace = uuid.UUID(namespace_setting)
            except (ValueError, TypeError):
                namespace = uuid.uuid4()

        for region in self.view.sel():
            if not region.empty():
                self.view.replace(edit, region, make_v5_uuid(namespace, self.view.substr(region)))

def make_v5_uuid(namespace, string):
    return uuid.uuid5(namespace, string).urn.lstrip('urn:uuid:')
