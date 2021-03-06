"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(
        self,
        video_title: str,
        video_id: str,
        video_status: str,
        video_tags: Sequence[str],
    ):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._video_status = video_status

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def video_status(self) -> str:
        """Returns the video status if its playing or not."""
        return self._video_status

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
