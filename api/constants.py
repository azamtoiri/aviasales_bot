from typing import cast, TypeVar, NewType, overload, Union, Callable, Optional

from decouple import config


T = TypeVar("T")
V = TypeVar("V")
Sentinel = NewType("Sentinel", object)
_MISSING = cast(Sentinel, object())


@overload
def _get_config(search_path: str, cast: None = None, default: Union[V, Sentinel] = _MISSING) -> Union[str, V]:
    ...


@overload
def _get_config(search_path: str, cast: Callable[[str], T], default: Union[V, Sentinel] = _MISSING) -> Union[T, V]:
    ...


def _get_config(
        search_path: str,
        cast: Optional[Callable[[str], object]] = None,
        default: object = _MISSING,
) -> object:
    """Wrapper around decouple.config that can handle typing better."""
    if cast is None:
        cast = lambda x: x

    if default is not _MISSING:
        obj = config(search_path, cast=cast, default=default)
    else:
        obj = config(search_path, cast=cast)

    return obj


class Settings:
    API_TOKEN = _get_config("API_TOKEN", str)