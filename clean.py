#!/usr/bin/env python3

from sys import argv, stdout, stderr
from string import printable # For sanitizing strings

def clean_str(string):
	ret = ""
	for char in string:
		if char in printable:
			ret += char
	return ret

def show_help():
	print("Usage: %s [--stdout]", file=stderr)
	raise SystemExit

def main():
	# Refer to /usr/lib/python3.11/site-packages/qui/clipboard.py
	from qui.clipboard import pyinotify, qubesadmin, NotificationApp, DATA, Gtk, Gdk

	print_cleaned = None
	if len(argv) != 1:
		if len(argv) == 2:
			if argv[1] in ["--stdout", "-o"]:
				print_cleaned = stdout.write
			elif argv[1] in ["--print", "-p"]:
				print_cleaned = print
			else:
				show_help()
		else:
			show_help()

	wm = pyinotify.WatchManager()
	qubes_app = qubesadmin.Qubes()
	dispatcher = qubesadmin.events.EventsDispatcher(qubes_app)
	gtk_app = NotificationApp(wm, qubes_app, dispatcher)
	clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
	text = clipboard.wait_for_text()

	with open(DATA, 'rb') as contents:
		cleaned = clean_str(contents.read().decode(encoding="ascii", errors="replace"))

		if print_cleaned != None:
			print_cleaned(cleaned)
		else:
			clipboard.set_text(cleaned, -1)
			gtk_app.copy_dom0_clipboard()

			clipboard.set_text(text, -1)

if __name__ == "__main__":
	main()
