from dataclasses import dataclass
from typing import Dict, List, Callable
import math

@dataclass
class AdaptationEpisode:
    reference_state: Dict[str,float]
    damaged_state: Dict[str,float]
    adapted_state: Dict[str,float]
    reference_function: float
    damaged_function: float
    adapted_function: float
    adaptation_cost: float

class AxolotlEvaluator:
    @staticmethod
    def clip01(x):
        return max(0.0,min(1.0,float(x)))

    @staticmethod
    def state_distance(a,b):
        keys=[k for k in a if k in b]
        if not keys: return 0.0
        return math.sqrt(sum((a[k]-b[k])**2 for k in keys)/len(keys))

    def evaluate(self, ep: AdaptationEpisode, invariants: List[Callable[[Dict[str,float]],bool]]=None):
        invariants=invariants or []
        q0=ep.reference_function
        qd=ep.damaged_function
        qa=ep.adapted_function

        loss=max(0.0,(q0-qd)/(abs(q0)+1e-9))
        gain=qa-qd
        denominator=q0-qd
        recovery=gain/(denominator+1e-9) if denominator>0 else (1.0 if qa>=q0 else 0.0)
        transformation=self.state_distance(ep.adapted_state,ep.reference_state)
        efficiency=max(0.0,gain)/(max(1e-9,ep.adaptation_cost))
        inv=(sum(1 for f in invariants if f(ep.adapted_state))/len(invariants)) if invariants else 1.0

        recovery_n=self.clip01(recovery)
        efficiency_n=efficiency/(1.0+efficiency)
        useful_transform=self.clip01(transformation)*recovery_n*inv

        resilience=(
            0.45*recovery_n+
            0.30*inv+
            0.15*efficiency_n+
            0.10*useful_transform
        )

        return {
            "loss_severity":loss,
            "adaptation_gain":gain,
            "functional_recovery":recovery,
            "transformation_distance":transformation,
            "invariant_retention":inv,
            "learning_efficiency":efficiency,
            "adaptive_resilience":self.clip01(resilience)
        }
