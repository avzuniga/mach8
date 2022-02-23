import requests
import sys

def index_or_none(players_temp, height_complement, complement_index, players):
    try:
        return players_temp.index(str(height_complement), complement_index+1, len(players)-1)
    except ValueError:
        return None

      
def get_player_add_height(height):
    url = 'https://mach-eight.uc.r.appspot.com/'
    data = requests.get(url=url).json()
    players = data['values']
    players_temp = [p["h_in"] for p in data['values']]
    temp_dirs = []
    players_result = []
    for index, value in enumerate(players):
      height_complement = height - int(value["h_in"])
      complement_index = 0
      while(complement_index != len(players)-1):
          if complement_index != None:
              complement_index = index_or_none(
                  players_temp, height_complement, complement_index, players)
              if complement_index and complement_index not in temp_dirs:
                  players_result.append(
                      value["first_name"]+" "+
                      value["last_name"]+" " +
                      players[complement_index]["first_name"] +" "+
                      players[complement_index]['last_name']
                  )
                  temp_dirs.append(complement_index)
              if complement_index == None:
                  break
      temp_dirs.append(index)
    return players_result


if __name__ == "__main__":
    height = sys.argv[1]
    print(get_player_add_height(int(height)))

