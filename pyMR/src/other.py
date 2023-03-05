import re
import tkinter as tk


class SyntaxHighlighting:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.highlight_patterns = [
            (r"\bTrue\b|\bFalse\b", "orange"),
            (r"\b\d+\b", "purple"),
            (r"(['\"])(\\\1|.)*?\1", "green"),
            (r"#.*$", "gray"),
            (r"\bdef\b|\bclass\b", "blue"),
            (r"\bfor\b|\bin\b|\bwhile\b", "blue"),
            (r"\bif\b|\belse\b|\belif\b", "blue"),
            (r"\btry\b|\bexcept\b", "blue"),
            (r"\bimport\b|\bfrom\b", "blue")
        ]
        self._setup_tags()

    def _setup_tags(self):
        for pattern, tag in self.highlight_patterns:
            self.text_widget.tag_configure(tag, foreground=tag)
            self.text_widget.tag_bind(tag, "<Button-1>", lambda event: "break")

        self.text_widget.tag_configure("selected_line", background="#f2f2f2")

    def highlight(self, event=None):
        for pattern, tag in self.highlight_patterns:
            self.text_widget.tag_remove(tag, "1.0", tk.END)

            for match in re.finditer(pattern, self.text_widget.get("1.0", tk.END)):
                start, end = match.span()
                self.text_widget.tag_add(tag, f"1.0+{start}c", f"1.0+{end}c")

        self._highlight_selected_line()

    def _highlight_selected_line(self):
        self.text_widget.tag_remove("selected_line", "1.0", tk.END)
        index = self.text_widget.index(tk.INSERT)
        self.text_widget.tag_add("selected_line", f"{index}.linestart", f"{index}.lineend+1c")


class AutoIndentation:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.indent_pattern = re.compile(r"^[\s\t]+")

    def indent(self, event):
        current_line = self.text_widget.get("insert linestart", "insert lineend")
        match = self.indent_pattern.match(current_line)

        if match:
            self.text_widget.insert("insert", "\n" + match.group(0))
            return "break"
