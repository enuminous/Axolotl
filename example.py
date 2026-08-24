from axolotl import AxolotlEvaluator, AdaptationEpisode

ep=AdaptationEpisode(
    reference_state={"primary":1.0,"alternate":0.1,"reserve":0.9},
    damaged_state={"primary":0.2,"alternate":0.1,"reserve":0.7},
    adapted_state={"primary":0.3,"alternate":0.9,"reserve":0.7},
    reference_function=1.0,
    damaged_function=0.3,
    adapted_function=0.94,
    adaptation_cost=0.75
)

invariants=[
    lambda s:s["reserve"]>=0.5,
    lambda s:max(s["primary"],s["alternate"])>=0.8
]

print(AxolotlEvaluator().evaluate(ep,invariants))
