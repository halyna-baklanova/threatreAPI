from theatre.models import Play


def create_sample_plays(**kwargs) -> Play:
    defaults = {
        "title": "Test Play",
        "description": "Test Play",
    }
    defaults.update(kwargs)
    return Play.objects.create(**defaults)
