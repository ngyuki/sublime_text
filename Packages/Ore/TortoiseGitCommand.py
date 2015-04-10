import sublime, sublime_plugin
import platform
import os
import re
import subprocess

if platform.system() == "Windows":

    def detect_path():
        fn = sublime.active_window().active_view().file_name()
        if fn and len(fn) > 0:
            if os.path.isdir(fn):
                return fn
            else:
                return os.path.dirname(fn)
        folders = sublime.active_window().folders()
        if len(folders) > 0:
            return folders[0]
        return None

    def open_tgit(command):
        cwd = detect_path()
        exe = os.environ["TGIT_BIN_DIR"] + "\\TortoiseGitProc.exe"
        arg = "/command:" + command
        subprocess.Popen(args = [exe, arg], cwd = cwd)

    class TortoiseGitStatus(sublime_plugin.TextCommand):
        def run(self, edit):
            open_tgit("repostatus")
        def is_enabled(self):
            return detect_path() is not None

    class TortoiseGitLog(sublime_plugin.TextCommand):
        def run(self, edit):
            open_tgit("log")
        def is_enabled(self):
            return detect_path() is not None

    class TortoiseGitFetch(sublime_plugin.TextCommand):
        def run(self, edit):
            open_tgit("fetch")
        def is_enabled(self):
            return detect_path() is not None

    class TortoiseGitCommit(sublime_plugin.TextCommand):
        def run(self, edit):
            open_tgit("commit")
        def is_enabled(self):
            return detect_path() is not None
