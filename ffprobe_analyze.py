import subprocess
import json

'''
a = info['streams'][0]['codec_name']
b = info['streams'][1]['tags']['language']
c = info['format']['duration']
print(c)
'''


# get informations
# print(round(float(info['format']['duration']) / 60), 'min')
def collect_info(path, size):
    # example for returned dict
    # result = {'video': ['h69', '69x420'], 'audio': ['mp69', 'sprache'], 'subtitle': ['subsprache', 'subname'], 'time':'69 min'}
    result = {'video': [], 'audio': [], 'subtitle': [], 'time': '', 'size': size}
    info = json.loads(subprocess.check_output(
        ['ffprobe', '-v', 'quiet', path, '-print_format', 'json', '-show_streams', '-show_format']).decode(
        'utf-8'))
    duration = round(float(subprocess.check_output(
        ['ffprobe', '-i', path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")]).decode(
        'utf-8')) / 60)
    for item in info['streams']:
        # get video stream informations
        if item['codec_type'] == 'video':
            video_info_list = []
            # print('Video:', item['codec_name'])
            video_info_list.append(item['codec_name'])
            # print('Res:', str(item['width']) + 'x' + str(item['height']))
            video_info_list.append(str(item['width']) + 'x' + str(item['height']))
            result['video'].append(video_info_list)
        # get audio streams informations
        if item['codec_type'] == 'audio':
            audio_info_list = []
            # print('Audio codec:', item['codec_name'], 'Audio lang:', item['tags']['language'])
            audio_info_list.append(item['codec_name'])
            audio_info_list.append(item['tags']['language'])
            result['audio'].append(audio_info_list)
        # get subtitle streams informations
        if item['codec_type'] == 'subtitle':
            subtitle_info_list = []
            # print('Sub lang:', item['tags']['language'], 'Sub name:', item['tags']['title'])
            subtitle_info_list.append(item['tags']['language'])
            if 'title' in item['tags']:
                subtitle_info_list.append(item['tags']['title'])
            result['subtitle'].append(subtitle_info_list)
    # print('Dur:', duration, 'min')
    result['time'] = f'{duration} min'
    # return dict with lists for every video information, uncomment the comment at the bottom for more explanation
    return result




'''
vid_information = collect_info(test_video)
for item in vid_information:
    print(item)
    print(vid_information[item])
'''
