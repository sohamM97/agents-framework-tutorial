from pathlib import Path
from typing import Annotated

from agent_framework import tool
from pydantic import Field


@tool(approval_mode="always_require")
def write_to_file(
    # TODO: is annotation required for the LLM? Or just for us?
    filename: Annotated[str, Field(description="The name of the file to create")],
    contents: Annotated[str, Field(description="The contents to write in the file")],
    filepath: Annotated[
        str, Field(description="The path at which to write the file")
    ] = "outputs",
):
    file_loc = Path(filepath) / filename
    with open(file_loc, "w") as f:
        f.write(contents)
