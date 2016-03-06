import urllib.request
import csv

outfile_path = 'LASTNAME_buzzfeed_data.csv'
writer = csv.writer(open(outfile_path, 'w'))

def get_html(url):
    f = urllib.request.urlopen(url)
    my_file = f.read().decode('utf-8')
    return my_file

def get_between_tags(my_html, tag1, tag2):
    """Finds one instance of text between two HTML tags.
    my_html: text file of web page HTML
    tag1: string defining the tag or other text to begin with, i.e. '<a href'
    tag2: string defining the tag or other text to end with, i.e. '</a>'
    return: string of content found between tag1 & tag2
    """
    begin = my_html.find(tag1) + len(tag1)
    end = my_html.find(tag2, begin)
    return my_html[begin: end]

def get_data_loop(my_html, tag1, tag2, return_data=0):
    """Finds all instances of text between two HTML tags.
    my_html: text file of web page HTML
    tag1: string defining the tag or other text to begin with, i.e. '<a href'
    tag2: string defining the tag or other text to end with, i.e. '</a>'
    return_data: set to 0 (default) to return dictionary; set to 1 to return list
    return: dictionary or list of content found between tag1 & tag2. 
            If dictionary is returned, it includes counts as values.
    """
    d_list = []
    start = 0
    while start >= 0:
        data_begin = my_html.find(tag1, start)
        my_html2 = my_html[start:]
        my_data = get_between_tags(my_html2, tag1, tag2)
        start = my_html.find(tag1, data_begin + len(tag1))
        d_list.append(my_data)
    if return_data == 1:
        return d_list
    else:
        d = dict()
        for item in d_list:
            d[item] = d.get(item, 0) + 1
        return d

urls = ['http://www.buzzfeed.com/sallytamarkin/total-body-workouts#.ai40YmR02', 'http://www.buzzfeed.com/sallytamarkin/get-fit-bodyweight-exercises#.vxxev52eb', 'http://www.buzzfeed.com/iramadison/definitive-proof-back-to-the-future-part-ii-predicted-the-da#.xvrEyPpEk']

for url in urls:
    my_file = get_html(url)
    row = []
    id = get_between_tags(my_file, '<meta property="bf:buzzid" content="', '" />')
    bylines = get_data_loop(my_file, 'class="byline__author" data-action="user/username">', '</a>', 1)
    #title = 
    #tags = 
    #superlists = 
    #impressions = 
    #fb_count = 
    row.append(id)
    row.append(bylines)
    #add appropriate row.append statements
    #writer.writerow(row)
    print(row)


