from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players, teams
import us
from pprint import pprint


def printTeamsByState(state):
    print(f'-------------- NBA Teams in {state.title()} ---------------')
    print('')
    teamsInState = teams.find_teams_by_state(state)
    stateTeamNames = [teamDict['full_name'] for teamDict in teamsInState]
    if(state.lower() == 'ontario'):
        print(
            f"The NBA has {len(teamsInState)} {'team' if len(teamsInState) == 1 else 'teams'} in the province of {state.title()}: {', '.join(stateTeamNames)}")
    else:
        print(
            f"The NBA has {len(teamsInState)} {'team' if len(teamsInState) == 1 else 'teams'} in the state of {state.title()}: {', '.join(stateTeamNames)}")
    print('')
    pprint(stateTeamNames)
    print('')


def getTeamsByStateOrProvince():
    teamsByStateOrProvince = {}
    for state in us.states.STATES:
        stateStr = str(state)
        teamsInState = teams.find_teams_by_state(stateStr)
        stateTeamNames = [teamDict['full_name'] for teamDict in teamsInState]
        teamsByStateOrProvince[stateStr] = ', '.join(stateTeamNames)
    teamsByStateOrProvince['Ontario'] = 'Toronto Raptors'

    return teamsByStateOrProvince


# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
printTeamsByState('ontario')
pprint(getTeamsByStateOrProvince())
