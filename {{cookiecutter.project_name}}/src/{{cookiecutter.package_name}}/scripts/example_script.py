"""
Application entry point using components.
"""

import argparse
import logging
import random

from {{cookiecutter.package_name}}.components.example_component import calculate_exponential_decay


def main() -> None:
    """
    Main function for the script. Generates a random number and computes its
    exponential decay, with behavior modified by command-line arguments.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Exponential decay demonstration.")
    parser.add_argument(
        "--range",
        type=float,
        default=10.0,
        help="The upper limit for the random input value (default: 10.0).",
    )
    
    args, _ = parser.parse_known_args()

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    input_value = random.uniform(0, args.range)
    result = calculate_exponential_decay(input_value)
    logging.info(f"Exponential Decay Result: {result:.4f}")


if __name__ == "__main__":
    main()
