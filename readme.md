0. GET root

/

response index.html

1. GET videos list

/api/videos?page=x&per=y

x - integer, > -1
y - integer, > 0

response (x, y are valid):

{
	data: [
		{id: id, name: 'foo'},
		...
	],
	page: x,
	per: y,
	total: z
}

response (x or y is invalid, or error)

{
	data: [],
	page: 0,
	per: 0,
	total: 0
}

================================================

2. GET video details

/api/videos/:id

response (video is found by id)

{
	id: id,
	name: 'bar',
	likes: x,
	dislikes: y,
	views: z,
	comments: k,
	subscribers: i
}

response (video is not found by id)

{}

================================================

3. POST video details

/api/videos

body

{
	name: 'bar',
	likes: l,
	dislikes: d,
	views: v,
	comments: c,
	subscribers: s,
url: youtube_video_url
}

response (saved)

{status: 200}

response (save error)

{status: xxx, error: 'a error message'}





os.environ["MONGODB_URI"] = "mongodb://admin:admin123@ds159216.mlab.com:59216/videostats"