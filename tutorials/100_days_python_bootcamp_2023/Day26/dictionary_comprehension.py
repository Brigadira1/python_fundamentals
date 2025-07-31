from pathlib import Path

import pandas as pd


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words_list = sentence.split()
#
# words_dict = {name: len(name) for name in words_list}
# print(words_dict)
def main() -> None:
    base_dir = Path(__file__).resolve().parent
    nato_file_path = base_dir / "nato_alphabet.csv"
    nato_data_frame = pd.read_csv(nato_file_path)
    print(nato_data_frame)

    while True:
        word: str = (input("Enter a word: ")).upper()
        nato_dict = {
            row.letter: row.code for (index, row) in nato_data_frame.iterrows()
        }
        nato_list = [nato_dict[letter] for letter in word]
        print(nato_list)


if __name__ == "__main__":
    main()
