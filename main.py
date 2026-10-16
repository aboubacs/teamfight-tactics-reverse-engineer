# gcloud functions deploy single_fight --runtime python39 --trigger-http --allow-unauthenticated --region europe-west1 && gcloud functions deploy batched_fights --runtime python39 --trigger-http --allow-unauthenticated --region europe-west1

import pygame
pygame.init()
from flask import escape
from flask import jsonify
from flask import make_response
from collections import Counter
import firebase_admin
from firebase_admin import db

from map import Map

firebase_admin.initialize_app(options={'databaseURL': 'https://tft-sandbox-default-rtdb.europe-west1.firebasedatabase.app'})

def single_fight(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json()

    if not request_json or 'board_id1' not in request_json or 'board_id2' not in request_json:
        return make_response(
            jsonify({'error': 'Missing board ids'}),
            404,
            headers
        )
    
    board_id1 = request_json['board_id1']
    board_id2 = request_json['board_id2']

    board1 = db.reference('boards').child(board_id1).get()
    board2 = db.reference('boards').child(board_id2).get()

    map = Map.from_boards(board1, board2)
    map.play(log=True)

    return make_response(
        jsonify({'winner': map.winner, 'units_alive': len(map.units), 'game_log': map.game_log}),
        200,
        headers
    )


def batched_fights(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json()

    if not request_json or 'board_id1' not in request_json or 'board_id2' not in request_json or 'fight_count' not in request_json:
        return make_response(
            jsonify({'error': 'Missing board ids'}),
            404,
            headers
        )
    
    board_id1 = request_json['board_id1']
    board_id2 = request_json['board_id2']
    fight_count = request_json['fight_count']

    board1 = db.reference('boards').child(board_id1).get()
    board2 = db.reference('boards').child(board_id2).get()
    cc = Counter()

    for i in range(fight_count):
        map = Map.from_boards(board1, board2)
        map.play(log=True)
        if map.winner == 1:
            cc[len(map.units)] += 1
        elif map.winner == 2:
            cc[-len(map.units)] += 1
        else:
            cc[0] += 1

    return make_response(
        jsonify(cc),
        200,
        headers
    )

