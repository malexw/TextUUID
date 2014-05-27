import sublime
import sublime_plugin
import uuid


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
                selected = self.view.substr(region)
                generated_id = uuid.uuid5(namespace, selected)

                self.view.replace(edit, region, generated_id.urn.lstrip('urn:uuid:'))


class RandomUuidCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            self.view.replace(edit, region, uuid.uuid4().urn.lstrip('urn:uuid:'))
