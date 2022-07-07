import sublime
import sublime_plugin

HALF = {
    "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
    "cols": [0.0, 0.5, 1.0],
    "rows": [0.0, 1.0],
}
LEFT_ZOOM = {
    "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
    "cols": [0.0, 0.75, 1.0],
    "rows": [0.0, 1.0],
}
RIGHT_ZOOM = {
    "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
    "cols": [0.0, 0.25, 1.0],
    "rows": [0.0, 1.0],
}


class ToggleZoomGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        # settings = sublime.load_settings("ZoomGroup.sublime-settings")

        # get the current group idx
        # check if you are zoomed
        # if you are zoomed.. change back to 0.5 else 0.8
        active_group_id = self.window.active_group()
        cols = self.window.layout().get("cols")

        is_left_active = active_group_id == 0

        self.window.set_sidebar_visible(False)

        if is_left_active:
            if cols[1] > 0.5:
                self.window.set_layout(HALF)
            else:
                self.window.set_layout(LEFT_ZOOM)
        else:
            if cols[1] < 0.5:
                self.window.set_layout(HALF)
            else:
                self.window.set_layout(RIGHT_ZOOM)

    def is_enabled(self) -> bool:
        rows = self.window.layout().get("rows")
        is_vertical_spilt = rows[0] == 0.0 and rows[1] == 1.0
        return self.window.num_groups() == 2 and is_vertical_spilt
