import os, sublime, sublime_plugin
import json

PACKAGE_NAME = 'SublimeNFFT'
PACKAGES_PATH = sublime.packages_path()
TEMPLATE_DIR = os.path.join(PACKAGES_PATH, PACKAGE_NAME, 'templates')

settings = sublime.load_settings('SublimeNfft.sublime-settings')

class SublimeNfftCommand(sublime_plugin.WindowCommand):

    def run(self, type="python", ext="py", dirs=[]):
        tmpl_file = TEMPLATE_DIR + '/%s.tpl' % type
        syntax = settings.get(type)['syntax']

        if not os.path.exists(tmpl_file):
            sublime.message_dialog('[Warning] No such file: ' + tmpl_file)
            return
        else:
            f = open(tmpl_file)
            template = f.read()
            f.close()
        
        v = self.window.new_file()
        v.set_name("untitled.%s" % ext)
        v.set_syntax_file(syntax)
        v.run_command("insert_snippet", {"contents": template})
        if len(dirs) == 1:
            v.settings().set('default_dir', dirs[0])
