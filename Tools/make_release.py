import os
from pathlib import Path

ERROR = "\033[91m"
WARNING = "\033[33m"
SUCCESS = "\033[92m"
INFO = "\033[96m"
END = "\033[0m"


class Skip(Exception):
    pass


class GitException(Exception):
    pass


def make_release(version: str, patch: str):
    print(
        f"\n{INFO}>>>{END} Making release for {INFO}{version}{END}"
        f" from {INFO}base@{patch}{END}..."
    )
    errorno = 0
    release_dir = build_dir / "IDLE-CN" / version

    if release_dir.exists():
        print(f"Directory '{version}' already exists.")
        raise Skip
    release_dir.mkdir(parents=True)
    os.chdir(release_dir)

    errorno += os.system("git init")
    errorno += os.system("git remote add upstream ../../cpython")
    errorno += os.system("git fetch upstream --no-tags")
    if errorno:
        raise GitException(f"Failed to init {version} repo")

    errorno += os.system(f"git checkout -t upstream/{version}")
    if errorno:
        raise GitException(f"Failed to checkout {version} from cpython@{version}")

    for patch_file in (patch_dir / patch).glob("*.patch"):
        errorno += os.system(
            f"git apply --ignore-whitespace --reject --recount {patch_file}"
        )
        errorno += os.system("git add .")
        errorno += os.system(f'git commit -m "Backport patch {patch_file.name}"')
    if errorno:
        rej_count = len(list(release_dir.rglob("*.rej")))
        if rej_count:
            raise GitException(f"{rej_count} patches failed to apply")
        else:
            raise GitException("During patching, some error occurred")


# ==== Main ====

# Path: idlecn_build/IDLE-CN/Tools/make_release.py
build_dir = Path(__file__).resolve().parent.parent.parent
base_dir = build_dir / "IDLE-CN" / "base"
patch_dir = build_dir / "IDLE-CN" / "patch"

os.chdir(build_dir)
if "idlecn_build" not in os.getcwd():
    print(f"{ERROR}Please run this script in the idlecn_build directory!{END}")
    exit(1)
print(f"\n{INFO}>>> Current directory: {Path.cwd()}{END}")

print(f"\n{INFO}>>> Creating patches...{END}")
os.chdir(base_dir)
os.system("git remote add upstream ../../cpython")
os.system("git fetch upstream --no-tags")
os.system("git branch")  # Just to show the current branch
patch_branches = [
    ln.replace("*", "").strip()
    for ln in os.popen("git branch").read().split("\n")
    if ln
]
for branch in patch_branches:
    print(f"\n{INFO}>>>{END} Creating patch from {INFO}base@{branch}{END}...")
    patch_dir_branch = patch_dir / branch
    patch_dir_branch.mkdir(parents=True, exist_ok=True)
    os.system(
        f"git format-patch --ignore-all-space upstream/{branch} -o {patch_dir_branch}"
    )

print(f"\n{INFO}>>> Creating releases...{END}")
with open(build_dir / "IDLE-CN" / "Tools" / "release_versions.txt") as file:
    for line in file:
        version = line.strip()
        try:
            os.chdir(build_dir)
            make_release(version, version if version in patch_branches else "main")
            os.chdir(build_dir)
        except Skip:
            print(f"{WARNING}>>> Release {version} skipped.{END}")
        except GitException as e:
            print(f"{ERROR}>>> Release {version} failed: {e}{END}")
        else:
            print(f"{SUCCESS}>>> Release {version} finished with no errors.{END}")
print(f"\n{INFO}>>> Finished making releases :){END}\n")
