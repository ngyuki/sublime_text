import sublime, sublime_plugin
import os
import subprocess
import re
import sys

class Ore:
    # def openBash(path):
    #     if os.path.isdir(path):
    #         dir = path
    #     else:
    #         dir = os.path.dirname(path)
    #     subprocess.Popen(
    #         executable = 'C:\\Program Files\\ConEmu\\ConEmu64.exe',
    #         args = ["/dir", dir, "/cmd", "bash", "--login"],
    #         cwd = dir)
    #     sublime.status_message("Open Bash in " + dir)

    def openWinMerge(path1, path2):
        dir = os.path.dirname(path2)
        prog = 'C:\\Program Files\\WinMerge\\WinMergeU.exe'
        subprocess.Popen(
            shell = False,
            args = [prog, "/u", "/r", path1, path2],
            cwd = dir)

# class OreBashCommand(sublime_plugin.TextCommand):

#     def detect_path(self):
#         fn = self.view.file_name()
#         if fn and len(fn) > 0:
#             return fn
#         folders = sublime.active_window().folders()
#         if len(folders) > 0:
#             return folders[0]
#         return None

#     def run(self, edit):
#         Ore.openBash(self.detect_path())

#     def is_enabled(self):
#         return self.detect_path() is not None

# class OreBashForSideBarCommand(sublime_plugin.WindowCommand):

#     def run(self, paths = []):
#         if len(paths) == 1:
#             Ore.openBash(paths[0])

#     def is_visible(self, paths = []):
#         return len(paths) == 1 and os.path.isdir(paths[0])

#     def is_enabled(self, paths = []):
#         return len(paths) == 1 and os.path.isdir(paths[0])

class OreWinMergeForSideBarCommand(sublime_plugin.WindowCommand):

    def run(self, paths = []):
        if len(paths) == 2:
            Ore.openWinMerge(paths[0], paths[1])

    def is_enabled(self, paths = []):
        return len(paths) == 2

    def is_visible(self, paths = []):
        return len(paths) == 2

# class OreMarkdownPreviewCommand(sublime_plugin.TextCommand):

#     def run(self, edit):
#         fn = self.view.file_name()
#         dir = os.path.dirname(fn)
#         subprocess.Popen(["mdlive", fn], cwd=dir, shell=True)

#     def is_enabled(self):
#         fn = self.view.file_name()
#         return fn is not None and len(fn) > 0 and re.search(r'\.(md|markdown)$', fn) is not None
