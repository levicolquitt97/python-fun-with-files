from dataclasses import dataclass
from array import *
from abc import ABC, abstractclassmethod


@dataclass
class SectionItem:
    description: str
    checked: bool = True

    def __str__(self):
        return f"[{'x' if self.checked else ' '}] {self.description}"

@dataclass
class Section:
    header: str
    items: list

    def __str__(self):
        items_str = "\n".join(f"    {item}" for item in self.items)
        return f"**{self.header}**\n{items_str}"


class SectionGenerator(ABC):
    @abstractclassmethod
    def generate_section(self) -> Section:
        pass

class Requirements(SectionGenerator):
    def generate_section(self) -> Section:
        return Section(
            header="Requirements",
            items=[
                SectionItem(
                    description=" Req notes"
                ),
                SectionItem(
                    description=" Req components"
                ),
                SectionItem(
                    description=" Validated images"
                )

            ]
        )

class History(SectionGenerator):
    def generate_section(self) -> Section:
        return Section(
            header="History",
            items=[
                SectionItem(
                    description=" History of development"
                ),
                SectionItem(
                    description=" History of components"
                ),
                SectionItem(
                    description=" History of images"
                ),
                SectionItem(
                    description=" History of codebase"
                )
            ]
        )

class ContentMapperOutput():
    def generateOutput(self, filename:str, sections: list[Section]):
        with open(filename, "w") as file:
            file.write("\n\n".join(str(section) for section in sections))

class ContentMapper:
    @staticmethod
    def content_mapper():
        sections = [Requirements().generate_section(), History().generate_section()]
        ContentMapperOutput().generateOutput("funnyFile.md", sections)
ContentMapper.content_mapper()
