import argparse

from module.algorithm import Algorithm
from module.handler import FileHandler


def main():
    parser = argparse.ArgumentParser(description="Custom File Compressor")
    parser.add_argument("mode", choices=["compress", "decompress"])
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    file_handler = FileHandler(args.input_file)
    compressor = Algorithm()

    output_chunks = []
    for chunk in file_handler.read_chunks():
        print("line {}".format(chunk))
        if args.mode == "compress":
            output_chunks.append(compressor.compress(chunk))
        else:
            output_chunks.append(compressor.decompress(chunk))

    # FileHandler.write_chunks(args.output_file, output_chunks)
    # print(f"{args.mode.capitalize()}ion completed successfully!")

if __name__ == "__main__":
    main()
