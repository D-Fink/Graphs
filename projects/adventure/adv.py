from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# visited room dict
visited_rooms = {}
# store the reverse path to backtrack
path_finder = []
# need opposite directions to backtrack
reverse_dir ={'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# get starting room and find the exits
visited_rooms[player.current_room.id] = player.current_room.get_exits()
# while we havent visited all the rooms
while len(visited_rooms) < len(room_graph):
    # if not visited
    if player.current_room.id not in visited_rooms:
        # mark as visited and get exits
        visited_rooms[player.current_room.id] = player.current_room.get_exits()
        # get the room we came from and remove it from list of exits
        last_dir = path_finder[-1]
        visited_rooms[player.current_room.id].remove(last_dir)
    # when all paths in room have been visited
    if len(visited_rooms[player.current_room.id]) == 0:
        # backtrack until an unexplored path is found and pop as we go
        last_dir = path_finder[-1]
        path_finder.pop()
        # add last direction to traversal_path
        traversal_path.append(last_dir)
        # move player in direction
        player.travel(last_dir)

    # if there are unexplored directions
    else:
        # define first available direction
        direction = visited_rooms[player.current_room.id][-1]
        # pop it from the list
        visited_rooms[player.current_room.id].pop()
        # append to the traversal_path
        traversal_path.append(direction)
        # track the path so we can backtrack
        path_finder.append(reverse_dir[direction])
        # move player in direction
        player.travel(direction)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
