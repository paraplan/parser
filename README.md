# VGPK schema parser

## Develop

1. Install dependencies:
    - with [rye](https://rye-up.com/) (modern Python package manager) 

    ```sh
    rye sync
    source .venv/bin/activate
    ```
    - with pip

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.lock
    ```

2. Save schema to `schedule.json`
3. Run `python3 -m src`
