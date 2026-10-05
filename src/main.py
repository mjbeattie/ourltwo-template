import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, default="FrozenLake-v1")
    parser.add_argument("--episodes", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=0)
    return parser.parse_args()

def main():
    args = parse_args()
    print(f"Running placeholder main with env={args.env}, episodes={args.episodes}, seed={args.seed}")

if __name__ == "__main__":
    main()
