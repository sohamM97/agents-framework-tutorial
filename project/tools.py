from pathlib import Path
from typing import Annotated

from agent_framework import tool
from pydantic import Field

BASE_DIR = Path(__file__).parent


@tool(approval_mode="always_require")
def write_to_file(
    # TODO: is annotation required for the LLM? Or just for us?
    filename: Annotated[str, Field(description="The name of the file to create")],
    contents: Annotated[str, Field(description="The contents to write in the file")],
    filepath: Annotated[
        str, Field(description="The path at which to write the file")
    ] = "outputs",
) -> Path:
    file_abs_path: Path = BASE_DIR / filepath

    if not file_abs_path.exists():
        file_abs_path.mkdir(parents=True, exist_ok=True)

    file_loc = file_abs_path / filename
    file_loc.write_text(contents)
    return file_loc


@tool(approval_mode="always_require")
def read_from_file(
    file_location: Annotated[
        str, Field(description="The full location of the file to be read")
    ],
) -> str:
    return Path(file_location).read_text()
