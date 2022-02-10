from hackaton import get_score

hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def test_verificando_se_get_score_esta_printando_correto():
    result = get_score("Team Ateliware", hackathon_3)
    expected = 2

    assert result == expected




# hackatons = {
#     "hackaton_1": ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"],
#     "hackaton_2": ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"],
#     "hackaton_3": ["Team Mirum", "Team Ateliware", "Team VHSYS", "Team Kenzie"],
# }
