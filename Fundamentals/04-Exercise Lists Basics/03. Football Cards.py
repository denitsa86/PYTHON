#Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than
# 7 players remaining, the game is stopped immediately and the team with less than 7 players loses.
#A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number.
# e.g. the card 'B-7' means player #7 from team B received a card
#Given a list of cards (could be empty), return the number of remaining players on each team at the end
# of the game in the format: "Team A - {players_count}; Team B - {players_count}".
# If the game was terminated print an additional line: "Game was terminated"
#Note for the random tests: If a player that has already been sent off receives another card - ignore it.
#A-1 A-5 A-10 B-2
team_a_list = []
team_b_list = []
team_a_count = 11
team_b_count = 11
kicked_out = []
for a in range(1,12):
    team_a_list.append(F"A-{a}")
for b in range(1,12):
    team_b_list.append(F"B-{b}")

red_cards = input().split(" ")
for card in red_cards:
    if card in kicked_out:
        continue  # Ignore duplicate red cards

    kicked_out.append(card)

    if card.startswith("A-"):
             team_a_count -= 1
    elif card.startswith("B-"):
        team_b_count -= 1
    if team_a_count < 7 or team_b_count < 7:
        break
print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if team_a_count < 7 or team_b_count < 7:
    print("Game was terminated")




