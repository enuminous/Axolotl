from axolotl import AxolotlEvaluator, AdaptationEpisode

reference={"path_a":1.0,"path_b":0.2,"reserve":0.8}
damaged={"path_a":0.2,"path_b":0.2,"reserve":0.6}

invariants=[
    lambda s:s["reserve"]>=0.4,
    lambda s:max(s["path_a"],s["path_b"])>=0.7
]

episodes={
    "failed":AdaptationEpisode(reference,damaged,{"path_a":0.25,"path_b":0.25,"reserve":0.55},1.0,0.35,0.40,0.8),
    "rollback":AdaptationEpisode(reference,damaged,{"path_a":0.92,"path_b":0.22,"reserve":0.75},1.0,0.35,0.91,0.8),
    "transformed":AdaptationEpisode(reference,damaged,{"path_a":0.30,"path_b":0.95,"reserve":0.70},1.0,0.35,0.96,0.7)
}

if __name__=="__main__":
    ev=AxolotlEvaluator()
    for name,ep in episodes.items():
        print(name,ev.evaluate(ep,invariants))
