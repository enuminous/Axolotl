from benchmark import episodes,invariants
from axolotl import AxolotlEvaluator

if __name__=="__main__":
    ev=AxolotlEvaluator()
    transformed=ev.evaluate(episodes["transformed"],invariants)
    rollback=ev.evaluate(episodes["rollback"],invariants)
    print("transformed:",transformed)
    print("rollback:",rollback)
    print("endpoint function only:",episodes["transformed"].adapted_function,episodes["rollback"].adapted_function)
