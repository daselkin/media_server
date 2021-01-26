API_KEY = open('keychain/youtube_api_key', 'r').read().strip()
API_URL_ROOT = "https://www.googleapis.com/youtube/v3"

SEARCH_URL = f"{API_URL_ROOT}/search"
DEFAULT_SEARCH_PARAMS = {
	"type": "video",
	"maxResults": 25,
	"key": API_KEY,
}

LIST_URL = f"{API_URL_ROOT}/videos"
DEFAULT_LIST_PARAMS = {
	'part': 'snippet,contentDetails,topicDetails',
	'key': API_KEY,
}

MUSIC_TOPIC = '/m/04rlf'
GENRES = {
	'/m/05fw6t': "Children's Music",
	'/m/02mscn': "Christian",
	'/m/0ggq0m': "Classical",
	'/m/01lyv': "Country",
	'/m/02lkt': "Electronic",
	'/m/0glt670': "Hip hop",
	'/m/05rwpb': "Indie",
	'/m/03_d0': "Jazz",
	'/m/028sqc': "Asia",
	'/m/0g293': "Latin America",
	'/m/064t9': "Pop",
	'/m/06cqb': "Reggae",
	'/m/06j6l': "Rhythm and Blues",
	'/m/06by7': "Rock",
	'/m/0gywn': "Soul",
}
