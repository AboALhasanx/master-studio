"""Allow ``python -m telegram`` when ``90_Shared_Toolbox`` is on sys.path."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
