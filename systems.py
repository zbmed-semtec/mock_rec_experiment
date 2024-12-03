import json
import random
import logging
import jsonlines

logging.basicConfig(level=logging.INFO)

class Recommender(object):

    def __init__(self):
        self.idx = None

    def index(self):
        self.idx = []
        with jsonlines.open('./data/relish_text.jsonl') as reader:
            for obj in reader:
                self.idx.append(obj.get('pmid'))

    def recommend_publications(self, item_id, page, rpp):
        filename = '../data/relish_recoms.jsonl'

        recommendations = []

        with open(filename, 'r') as file:
            for line in file:
                record = json.loads(line)
                if int(record['pmid']) == int(item_id):
                    recommendations.append(record)

        itemlist = sorted([int(record['target_pmid']) for record in recommendations[:rpp]])

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }