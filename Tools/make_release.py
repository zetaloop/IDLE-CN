import os
import shutil
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
    errorno = 0
    release_version_dir = release_tmp_dir / version

    if release_version_dir.exists():
        print(f"Directory '{version}' already exists.")
        raise Skip
    release_version_dir.mkdir(parents=True)
    os.chdir(release_version_dir)

    errorno += os.system("git init")
    errorno += os.system("git remote add upstream ../../../cpython")
    errorno += os.system("git fetch upstream --no-tags")
    if errorno:
        raise GitException(f"Failed to init {version} repo")

    errorno += os.system(f"git checkout -t upstream/{version}")
    if errorno:
        raise GitException(f"Failed to checkout {version} from cpython@{version}")

    for patch_file in (patch_dir / patch).glob("*.patch"):
        errorno += os.system(f"git apply --reject --recount {patch_file}")
        errorno += os.system("git add .")
        errorno += os.system(f'git commit -m "Backport patch {patch_file.name}"')
    if errorno:
        rej_count = len(list(release_version_dir.rglob("*.rej")))
        if rej_count:
            raise GitException(f"{rej_count} patches failed to apply")
        else:
            raise GitException("During patching, some error occurred")

    print()
    print(f"tmp_release/{version}/idlelib ==copying=> release/{version}/idlelib")
    shutil.copytree(
        "idlelib",
        release_dir / version / "idlelib",
        dirs_exist_ok=True,
    )
    print(f"tmp_release/{version}/turtledemo ==copying=> release/{version}/turtledemo")
    shutil.copytree(
        "turtledemo",
        release_dir / version / "turtledemo",
        dirs_exist_ok=True,
    )


def find_closest_patch(version: str):
    patches = sorted(
        (
            tuple(map(int, version.split(".")))
            for version in patch_branches
            if version != "main"
        )
    )
    version = tuple(map(int, version.split(".")))
    for patch in patches:
        if patch >= version:
            return ".".join(map(str, patch))
    else:
        return "main"


# ==== Main ====

# Path: idcn_build/IDLE-CN/Tools/make_release.py
build_dir = Path(__file__).resolve().parent.parent.parent
base_dir = build_dir / "IDLE-CN" / "base"
patch_dir = build_dir / "IDLE-CN" / "patches"
release_dir = build_dir / "IDLE-CN" / "idcn" / "releases"
release_tmp_dir = build_dir / "IDLE-CN" / "tmp_releases"

os.chdir(build_dir)
if "idcn_build" not in os.getcwd():
    print(f"{ERROR}Please run this script in the idcn_build directory!{END}")
    exit(1)
print(f"\n{INFO}>>> Current directory: {Path.cwd()}{END}")

print(f"\n{INFO}>>> Creating patches...{END}")
os.chdir(base_dir)
os.system("git remote add upstream ../../cpython")
os.system("git fetch upstream --no-tags")
os.system("git checkout main")
patch_branches = [
    ln.strip().split(" ")[0].split("/")[1]
    for ln in os.popen("git branch -r").read().split("\n")
    if "origin" in ln and "HEAD" not in ln
]
for branch in patch_branches:
    print(f"  {INFO}origin/{branch}{END}")
for branch in patch_branches:
    print(
        f"\n{INFO}>>>{END} Creating patch for "
        f"{INFO}cpython@{branch} -> base@{branch}{END}..."
    )
    patch_dir_branch = patch_dir / branch
    patch_dir_branch.mkdir(parents=True, exist_ok=True)
    os.system(f"git checkout origin/{branch}")
    os.system(f"git format-patch upstream/{branch} -o {patch_dir_branch}")

print(f"\n{INFO}>>> Creating releases...{END}")
with open(build_dir / "IDLE-CN" / "Tools" / "release_versions.txt") as file:
    for line in file:
        version = line.strip()
        patch = find_closest_patch(version)
        try:
            os.chdir(build_dir)
            print(
                f"\n{INFO}>>>{END} Making release for "
                f"{INFO}{version} <- base@{patch}{END}..."
            )
            make_release(version, patch)
            os.chdir(build_dir)
        except Skip:
            print(f"{WARNING}>>> Release {version} skipped.{END}")
        except GitException as e:
            print(f"{ERROR}>>> Release {version} <- Patch {patch} failed: {e}{END}")
        else:
            print(
                f"{SUCCESS}>>> Release {version} <- Patch {patch} "
                f"finished with no errors.{END}"
            )
print(f"\n{INFO}>>> Finished making releases :){END}\n")
