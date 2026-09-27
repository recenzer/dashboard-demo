from src.stats import load_stats


def main() -> None:
    stats = load_stats("config.json")
    print(f"users today: {stats['users']}")


if __name__ == "__main__":
    main()
