"""Strategy registry; each teammate adds a class implementing propose(context)."""

from .full_generation import FullGeneration
from .corridor_portfolio import CorridorPortfolio
from .submission_generation import SubmissionGenerationPortfolio

STRATEGIES = {"full_generation": FullGeneration, "corridor_portfolio": CorridorPortfolio,
              "submission_generation": SubmissionGenerationPortfolio}


def build_strategy(name: str, params: dict):
    try:
        strategy_class = STRATEGIES[name]
    except KeyError:
        raise ValueError(f"unknown strategy {name!r}; choices: {', '.join(STRATEGIES)}") from None
    return strategy_class(**params)
