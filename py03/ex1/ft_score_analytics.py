import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    try:
        scores: list[int] = [int(x) for x in sys.argv[1:]]
        if len(scores) == 0:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        else:
            print(f"Scores processed:: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores)/len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        print()

    except ValueError:
        print("Error: all arguments must be integers.")


if __name__ == "__main__":
    main()
