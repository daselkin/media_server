ASSET_DIRECTORY = 'assets/'
HTML_TEMPLATE = open('assets/html_template.html', 'r').read()
MEDIA_CONTROL_BUTTONS = open('assets/media_control_buttons.html', 'r').read()
MEDIA_SOURCE_SELECTORS = open('assets/media_source_selectors.html', 'r').read()
MEDIA_LIBRARY_ITEM = open('assets/media_library_item.html', 'r').read()
MEDIA_ITEM = open('assets/media_item.html', 'r').read()
NOW_PLAYING_BAR = open('assets/now_playing_bar.html', 'r').read()

LANDING_PAGE_HTML = HTML_TEMPLATE.format(
	title="MusicBox",
	body=f"""
	{MEDIA_CONTROL_BUTTONS}
	{{now_playing}}
	<br><br>
	{MEDIA_SOURCE_SELECTORS}
	"""
)


BROWSE_MEDIA_PAGE_HTML = HTML_TEMPLATE.format(
	title="MusicBox: Browsing Library",
	body="<div filelist>{media_items_list}</div filelist>"
)

