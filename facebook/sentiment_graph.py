import json 
import urllib.request
from access_token import LONGLIVED_ACCESS_TOKEN
from textblob import TextBlob
import plotly.offline as opy
import plotly.graph_objs as go

def get_date(created_time):
    date = created_time.split("T")[0]
    return date

def get_sentiment_graph(effective_object_story_id="114113634875896_142641242042511", post_title="static", access_token=LONGLIVED_ACCESS_TOKEN):
    ads_comment_url  = f"https://graph.facebook.com/v16.0/{effective_object_story_id}/comments?fields=id,message,created_time,is_hidden&summary=true&access_token={access_token}&pretty=1&summary=true&limit=100&after"
    ads_comments_json = json.loads(urllib.request.urlopen(ads_comment_url).read()) 
    comment_and_graph = {}
    comments = []
    comment_list = []
    reversed_comment = ads_comments_json['data'][::-1]
    positive_sentiment = negative_sentiment = neutral_sentiment = 0
    for d in reversed_comment:
        comment_polarity = TextBlob(d['message']).sentiment.polarity
        comments.append(d['message'])
        status = d['is_hidden']
        if comment_polarity < 0.0:
            negative_sentiment += 1
            comment_list.append({"negative_message": d['message'], "id":d['id'], "is_hidden":status,"created_time":get_date(d['created_time'])})
        elif comment_polarity > 0.0:
            comment_list.append({"positive_message": d['message'], "id":d['id'], "is_hidden":status,"created_time":get_date(d['created_time'])})
            positive_sentiment += 1
        elif comment_polarity == 0.0:
            comment_list.append({"neutral_message": d['message'], "id":d['id'], "is_hidden":status,"created_time":get_date(d['created_time'])})
            neutral_sentiment += 1
    value = [negative_sentiment,  positive_sentiment, neutral_sentiment]
    names = ['Negative Comments', 'Positive Comments', 'Neutral Comments']
    comment_and_graph['Comments'] = comment_list
    if sum(value) != 0:  
        trace1 = go.Bar(x=names, y=value )
        data=go.Data([trace1])
        layout=go.Layout(title=post_title, xaxis={'title':'Comments'}, yaxis={'title':'Count'})
        figure=go.Figure(data=data,layout=layout, ) 
        figure.update_traces(marker_color=['red',  'green', 'blue',])             
        div = figure.to_html(
            full_html=False, default_height=400, 
            default_width=500,
            config=dict(displayModeBar=False))
        comment_and_graph['Graph'] = div
        comment_and_graph['adname'] = effective_object_story_id
        return comment_and_graph
    else:
        return "No comments found"





# def get_sentiment_graph_copy(effective_object_story_id="114113634875896_142641242042511", post_title="static", access_token=LONGLIVED_ACCESS_TOKEN):
#     ads_comment_url  = f"https://graph.facebook.com/v16.0/{effective_object_story_id}/comments?fields=id,message,is_hidden&summary=true&access_token={access_token}&pretty=1&summary=true&limit=100&after"
#     ads_comments_json = json.loads(urllib.request.urlopen(ads_comment_url).read()) 
#     comment_and_graph = {}
#     comments = []
#     comment_list = []
#     positive_sentiment = negative_sentiment = neutral_sentiment = 0
#     for d in ads_comments_json['data']:
#         comment_polarity = TextBlob(d['message']).sentiment.polarity
#         comments.append(d['message'])
#         status = d['is_hidden']
#         if comment_polarity < 0.0:
#             negative_sentiment += 1   
#             # status = comment_status(d['id'])     
#             comment_list.append({"negative_message": d['message'], "id":d['id'], "is_hidden":status})
#         elif comment_polarity > 0.0:
#             comment_list.append({"positive_message": d['message'], "id":d['id'], "is_hidden":status})
#             positive_sentiment += 1
#         elif comment_polarity == 0.0:
#             comment_list.append({"neutral_message": d['message'], "id":d['id'], "is_hidden":status})
#             neutral_sentiment += 1
#     value = [negative_sentiment,  positive_sentiment, neutral_sentiment]
#     names = ['Negative Comments', 'Positive Comments', 'Neutral Comments']
#     comment_and_graph['Comments'] = comment_list

#     # return value if post has at least one comment 
#     if sum(value) != 0:  
#         comment_and_graph["negative_count"] = value[0]
#         comment_and_graph["positive_count"] = value[1]
#         comment_and_graph['neutral_count'] = value[2]
#         # trace1 = go.Bar(x=names, y=value )
#         # data=go.Data([trace1])
#         # layout=go.Layout(title=post_title, xaxis={'title':'Comments'}, yaxis={'title':'Count'})
#         # figure=go.Figure(data=data,layout=layout, ) 
#         # figure.update_traces(marker_color=['red',  'green', 'blue',])             
#         # div = figure.to_html(
#         #     full_html=False, default_height=400, 
#         #     default_width=500,
#         #     config=dict(displayModeBar=False))
#         # comment_and_graph['Graph'] = div
#         comment_and_graph['adname'] = effective_object_story_id
#         return comment_and_graph
#     else:
#         return "No comments found"