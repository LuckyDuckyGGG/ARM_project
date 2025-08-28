def abs_path_from_project(relative_path: str):
    import arm_project
    from pathlib import Path

    return (
        Path(arm_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )