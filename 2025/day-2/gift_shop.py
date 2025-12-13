class InvalidIDRange(Exception):
    pass

class IDChecker:
    def check_id_file(self, file_name: str):
        ranges: list[tuple[int, int]] = self._get_ranges_from_file(file_name)
        self.invalid_IDs: list[int] = self._get_invalid_IDs(ranges)

    def _get_invalid_IDs(self, ranges) -> list[int]:
        invalid_IDs = []
        for begin, end in ranges:
            for i in range(begin, end + 1):
                if self._is_invalid_id:
                    invalid_IDs.append(i)

        return invalid_IDs

    def  _is_invalid_id(self, id: int) -> bool:
        return bool(id) #TO-DO: Adicionar verificação

    def _get_ranges_from_file(self, file_name: str) -> list[tuple[int, int]]:
        ranges: list[tuple[int,int]] = []
        
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_content = file.read().strip()
                raw_pairs = file_content.split(',')

                for pair in raw_pairs:
                    parts = pair.split('-')
                    try:
                        if ( parts[0][0] == "0" ) or ( parts[1][0] == "0" ):
                            continue

                        start = int(parts[0])
                        end = int(parts[1])
                        ranges.append((start, end))
                    except(ValueError, IndexError):
                        raise InvalidIDRange("An error has occoured on attempt to read a pair : pair=", {pair})

        except FileNotFoundError:
            print(f"Error: '{file_name}' is not a valid file name")
        
        return ranges

if __name__ == "__main__":
    invalid_product_ID = []
    id_checker = IDChecker()
    id_checker.check_id_file("input.txt")

    sum = 0
    for i in id_checker.invalid_IDs:
        sum += i

    print(sum)

