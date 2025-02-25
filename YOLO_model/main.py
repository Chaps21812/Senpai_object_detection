import sys
import json
from train import train_model
from eval import evaluate_model
from convert import convert_data

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <command> <input_file> [output_file]")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else "output.json"

    # Read input data
    with open(input_file, "r") as f:
        data = json.load(f)

    if command == "train":
        result = train_model(data)
    elif command == "eval":
        result = evaluate_model(data)
    elif command == "convert":
        result = convert_data(data)
    else:
        print("Invalid command. Use 'train', 'eval', or 'convert'.")
        sys.exit(1)

    # Write output to file
    with open(output_file, "w") as f:
        json.dump(result, f)

    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    main()
