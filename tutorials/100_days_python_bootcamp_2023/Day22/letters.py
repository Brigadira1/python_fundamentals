from pathlib import Path
from typing import Iterator

PLACEHOLDER = "[Name]"


def read_name(file: Path) -> Iterator[str]:
    with file.open("r", encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name:
                yield name


def generate_letter(name: str, template: str, output_dir: Path) -> None:
    content = template.replace(PLACEHOLDER, name)
    output_file = output_dir / f"letter_{name}.txt"
    output_file.write_text(content)


def main() -> None:

    current_path: Path = Path(__file__).resolve().parent
    name_file: Path = current_path / "names.txt"
    template_file: Path = current_path / "template.txt"
    template_file_contents: str = template_file.read_text()

    for person_name in read_name(name_file):
        generate_letter(
            output_dir=current_path, template=template_file_contents, name=person_name
        )


if __name__ == "__main__":
    main()
