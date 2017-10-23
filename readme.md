# FPL Data Convert

Very simple pyton system to convert FPL data to useable CSV format ⚽👉🖥️

## Getting Started

Clone / Download / Fork onto system, and follow these basic instructions:

- Download https://fantasy.premierleague.com/drf/elements/ to data.json
- What fields do you want? Put them in the headers list
- Run this file: $ python convert.py
- Output file is output.csv - open in spreadsheet prog of choice

### Prerequisites

Built, tested and ran on Python 2.7.13. Needs to import CSV and JSON packages, but thats built in 👍

### Example Data

Use this player block as a way of finding out what fields are available to be taken:

```json
{
  "id": 1,
  "photo": "48844.jpg",
  "web_name": "Ospina",
  "team_code": 3,
  "status": "i",
  "code": 48844,
  "first_name": "David",
  "second_name": "Ospina",
  "squad_number": 13,
  "news": "Groin Injury - Expected back 18 Nov",
  "now_cost": 49,
  "chance_of_playing_this_round": 0,
  "chance_of_playing_next_round": 0,
  "value_form": "0.0",
  "value_season": "0.0",
  "cost_change_start": -1,
  "cost_change_event": 0,
  "cost_change_start_fall": 1,
  "cost_change_event_fall": 0,
  "in_dreamteam": false,
  "dreamteam_count": 0,
  "selected_by_percent": "0.2",
  "form": "0.0",
  "transfers_out": 5811,
  "transfers_in": 1018,
  "transfers_out_event": 248,
  "transfers_in_event": 17,
  "loans_in": 0,
  "loans_out": 0,
  "loaned_in": 0,
  "loaned_out": 0,
  "total_points": 0,
  "event_points": 0,
  "points_per_game": "0.0",
  "ep_this": "0.0",
  "ep_next": "0.0",
  "special": false,
  "minutes": 0,
  "goals_scored": 0,
  "assists": 0,
  "clean_sheets": 0,
  "goals_conceded": 0,
  "own_goals": 0,
  "penalties_saved": 0,
  "penalties_missed": 0,
  "yellow_cards": 0,
  "red_cards": 0,
  "saves": 0,
  "bonus": 0,
  "bps": 0,
  "influence": "0.0",
  "creativity": "0.0",
  "threat": "0.0",
  "ict_index": "0.0",
  "ea_index": 0,
  "element_type": 1,
  "team": 1
}
```