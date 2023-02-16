from dataclasses import dataclass

from bc.core.utils.string_utils import trunc


class AlwaysBlankValueDict(dict):
    """Just return blank, regardless of the key"""

    def __getitem__(self, key):
        return ""


@dataclass
class MastodonTemplate:
    str_template: str
    link_placeholders: list[str]
    max_characters: int = 500

    def __len__(self):
        """Returns the length of the template without the placeholders

        All links count as 23 characters in mastodon no matter how long
        they really are.
        """
        return 23 * len(self.link_placeholders) + self.count_fixed_characters()

    def count_fixed_characters(self):
        """Returns the number of fixed characters

        this method removes all the placerholders in the str_template
        using a dictionary that returns a blank string for each key
        and then computes the len of the new string.
        """
        clean_template = self.str_template.format_map(AlwaysBlankValueDict())
        return len(clean_template)

    def _available_space(self, *args, **kwargs) -> int:
        """Returns the number of available characters

        this method ignores all the links in the str_template because Mastodon
        uses a fixed length for them.
        """
        excluded = self.link_placeholders.copy()
        excluded.append("description")

        placeholder_characters = sum(
            [
                len(str(val))
                for key, val in kwargs.items()
                if key not in excluded
            ]
        )

        return self.max_characters - len(self) - placeholder_characters

    def format(self, *args, **kwargs) -> str:
        if "description" in kwargs:
            available_space = self._available_space("description", **kwargs)
            if len(kwargs["description"]) > available_space:
                kwargs["description"] = trunc(
                    kwargs["description"], available_space, "…"
                )

        return self.str_template.format(**kwargs)


POST_TEMPLATE = MastodonTemplate(
    link_placeholders=["pdf_link", "docket_link"],
    str_template="""New filing in {docket}
Doc #{doc_num}: {description}

PDF: {pdf_link}
Docket: {docket_link}""",
)


MINUTE_TEMPLATE = MastodonTemplate(
    link_placeholders=[],
    str_template="""New minute entry in {docket}: {description}""",
)