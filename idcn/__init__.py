def patch():
    from sys import version_info, path
    from pathlib import Path

    releases = Path(__file__).resolve().parent / "releases"
    ver = (version_info.major, version_info.minor)
    main_dir = None
    max_ver = None

    for d in releases.iterdir():
        if d.is_dir():
            if d.name == "main":
                main_dir = d
            else:
                try:
                    v = tuple(map(int, d.name.split(".")))
                    if len(v) == 2 and (max_ver is None or v > max_ver):
                        max_ver = v
                except ValueError:  # 忽略无法解析的目录
                    pass

    # 如果当前Python版本大于已打包的最高版本且存在main目录 => 跳转到main
    if max_ver and ver > max_ver and main_dir:
        path.insert(0, str(main_dir))
    else:
        # 如果与当前版本号同名的目录存在 => 跳转到对应版本
        candidate = releases / f"{ver[0]}.{ver[1]}"
        if candidate.is_dir():
            path.insert(0, str(candidate))
