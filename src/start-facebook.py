import facebook
import sys

args = sys.argv

#token = 'EAACZAe0FHKoABAERrKv0xqvFleSxVFcZC45HTFZAexjBHv1caxM7bZC7JlD4MorykS4ZCZC90r93C7SOflq8gLlPtYNZATTmMacZAdgYQlOA9JLfsrxZAU5xNxVVEdISmB0F3TV2C7sFIZADPglJjt5ZBZAGzMwrlyhRh3ZBILDxQXdsHFm5QlntgHkljZCvsM0f5L2vNlZA4N4mKOueKmhYbsyytMU'
#token = 'EAACZAe0FHKoABAPelLrNNnNlwhFSCElOHrGeqrQbL5uosBqq0m5DDTdZB2lYIqwm1ZBkEljqyhSeZChHhsVeWgiVyREplNJuxXh8zZB5N3uiGJF78aub9huSKi5rB5MVA7xcbEC8kDzQwBy6nJfzRorEZBjtZB5UORlLblRzUtBsHTgrwQUizGkBK65cZBBea9ZBDIlSNWZCtzHyUnLvdgqqys'
token = 'EAACZAe0FHKoABAMfs6MZC2ZAcZCmDczGIq2xlnNphUUpyBhwcuguekNByT9rnWoq1XXXZCKjObmUtfqqoZBQOltPTQZB7zGyjMKcYZBfANWeGBdBBQZBdhUafZBVK10RxCITjJt0zSAYzP8NDZBcTI8mwPgjPdP22H3iUFZBShZBRIHZC2yFTOHuOvSnYKwsMLu51ZBkdHtcRkjzQpLw1jyQeGx38uo'
video_id = args[1]
graph = facebook.GraphAPI(access_token=token, version='2.12')

graph.put_comment(object_id=video_id, message='Great post...')
graph.put_comment(object_id=video_id, message='Keep going')
graph.put_comment(object_id=video_id, message='Nice mate')
graph.put_comment(object_id=video_id, message='Really nice')
graph.put_comment(object_id=video_id, message='Good job')

#   https://developers.facebook.com/tools/explorer/