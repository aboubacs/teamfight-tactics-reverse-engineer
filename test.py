import pygame
pygame.init()

from map import Map

board1 = {
	"board_data": """[[{},{},{\"name\":\"aatrox\",\"starLevel\":2,\"items\":[\"gargoyle_stoneplate\",\"\",\"\"],\"dialog\":false},{},{},{},{}],[{},{},{},{},{},{},{}],[{\"name\":\"kha'zix\",\"starLevel\":1,\"items\":[\"\",\"\",\"\"],\"dialog\":false},{\"name\":\"gragas\",\"starLevel\":1,\"items\":[\"\",\"\",\"\"],\"dialog\":false},{},{},{},{},{}],[{\"name\":\"vayne\",\"starLevel\":1,\"items\":[\"\",\"\",\"\"],\"dialog\":false},{},{},{},{},{},{}]]""",
	"edited_at": 1625426988751,
	"edited_by": "Faellan",
	"id": "-MdmvbAxYKegboIuBw6D",
	"name": "new board"
}

board2 = board1
for i in range(10):
	map = Map.from_boards(board1, board2)
	map.play(log=True)
	print(map.winner, len(map.units), map.game_log)
