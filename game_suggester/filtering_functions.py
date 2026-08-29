from core.gamenode import GameNode

def filter_games_by_platform(games: list[GameNode], platform: str) -> list[GameNode]:
	return list(filter(lambda game: game.has_platform(platform), games))

def filter_games_by_status(games: list[GameNode], status: str) -> list[GameNode]:
	return list(filter(lambda game: game.has_status(status), games))

def filter_games_by_genres(games: list[GameNode], genres: list[str]) -> list[GameNode]:
	return list(filter(lambda game: game.has_any_genres(genres), games))

def filter_games_by_tags(games: list[GameNode], tags: list[str]) -> list[GameNode]:
	return list(filter(lambda game: game.has_any_tag(tags), games))

def filter_games(games: list[GameNode], platform: str, status: str, genres: list[str], tags: list[str]) -> list[GameNode]:
	filtered = filter_games_by_platform(games, platform)
	filtered = filter_games_by_status(filtered, status)
	if len(genres) > 0:
		filtered = filter_games_by_genres(filtered, genres)
	if len(tags) > 0:
		filtered = filter_games_by_tags(filtered, tags)
	return filtered
