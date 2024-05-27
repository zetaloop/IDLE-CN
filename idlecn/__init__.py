def patch():
    from sys import version_info, path
    from pathlib import Path

    version = f"{version_info.major}.{version_info.minor}"
    idcn_path = Path(__file__).resolve().parent / "releases" / version
    path.insert(0, str(idcn_path))
