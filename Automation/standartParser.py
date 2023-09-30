from urllib.request import urlopen
from re import findall

def get_links(text):
	pattern = r"href\s*=\s*['\"]([^'\"]+)"
	return findall(pattern, text)

with urlopen("https://1win.io/casino/play/1play_1play_luckyjet") as page:
	html = page.read().decode()

[print(x) for x in get_links(html)]
