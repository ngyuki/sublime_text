import sublime, sublime_plugin
import platform
import os
import re
import subprocess

if platform.system() == "Windows":

    def detect_path():
        fn = sublime.active_window().active_view().file_name()
        if fn and len(fn) > 0:
            return fn
        folders = sublime.active_window().folders()
        if len(folders) > 0:
            return folders[0]
        return None

    def open_tgit(command):
        path = detect_path()
        if os.path.isdir(path):
            cwd = path
        else:
            cwd = os.path.dirname(path)

        if "TGIT_BIN_DIR" in os.environ:
            exe = os.environ["TGIT_BIN_DIR"] + "\\TortoiseGitProc.exe"
        else:
            exe = "C:\\Program Files\\TortoiseGit\\bin\\TortoiseGitProc.exe"

        subprocess.Popen(args = [exe, "/command:" + command, "/path:" + path], cwd = cwd)

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
