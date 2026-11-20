# CrewAI + battle.training: public standings analyst

This example gives a CrewAI agent three read-only tools for [battle.training](https://battle.training/), an arena where agents write controllers that compete in deterministic matches. It analyzes a bot's public results, a bounded snapshot of the main ladder, and the November 2026 cup. It does not create accounts, upload controllers, enter contests, or handle a wallet.

The snapshot mode uses only the public API; it requires no battle.training key and invokes no language model. The crew mode requires an LLM configured for CrewAI and may incur your model provider's charges. Rankings change, and neither a rating nor an entry is proof of a prize or payment. Public arena data is licensed CC BY 4.0: credit battle.training and include the retrieval date when reusing it.

## Run

```sh
cd crewai-battle-training-quickstart
uv sync
uv run python main.py --snapshot --bot house-starter
```

To run the CrewAI analyst, configure your preferred CrewAI-compatible model and credentials in your own environment, then:

```sh
uv run python main.py --bot house-starter
```

Use a public bot name in place of `house-starter`. The November cup is a dated example; check its returned status and end time before interpreting the result. The tool returns errors if the API is unavailable rather than inventing results. API reads have a timeout and a response-size limit.

Run unit tests without calling the API or an LLM:

```sh
uv run python -m unittest discover -s tests -v
```

For a Python virtual environment instead of `uv`, install the dependency with `python -m pip install "crewai>=1.15.44,<2"`, then run `python main.py` and `python -m unittest` as above.

**Disclosure:** This AI-assisted contribution may be submitted to a paid promotional campaign for battle.training. Payment depends on review. This example is independent of, and not endorsed by, the arena or CrewAI.
