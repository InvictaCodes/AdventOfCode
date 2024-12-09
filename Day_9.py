import inputs


def perform_checksome(filesystem):
    return sum([block * i for i, block in enumerate(filesystem) if block != '.'])


def first_method(file_sizes, spaces, compressed_individual_blocks):
    filesystem = []
    for block in range(len(compressed_individual_blocks) + sum(spaces)):
        file = [compressed_individual_blocks.pop(0) for i in range(file_sizes.pop(0))]
        filler = [compressed_individual_blocks.pop(-1) for i in range(spaces.pop(0))]
        file = file + filler
        if len(compressed_individual_blocks) <= file_sizes[0]:
            file = file + compressed_individual_blocks
            filesystem += file
            break
        if len(spaces) == 0:
            filesystem += compressed_individual_blocks
            break
        filesystem += file

    return filesystem


def second_method(files, spaces, filesystem):
    for file_start, file_size in files[::-1]:
        for space_start, space_size in spaces:
            # write the last file in the filesystem into the first space that will fit it, but only if that's to the left
            if space_start > file_start:
                break
            if space_size >= file_size:
                filesystem[space_start: space_start + file_size] = filesystem[file_start: file_start + file_size]
                # replace where the file was with space
                filesystem[file_start: file_start + file_size] = ["."] * file_size
                i = spaces.index((space_start, space_size))
                # reduce or delete the space
                if file_size < space_size:
                    spaces[i] = (space_start + file_size, space_size - file_size)
                else:
                    spaces.pop(i)
                break

    return filesystem


def compact_disk(data):
    filesystem = [int(datum) for datum in data]
    file_sizes = filesystem[::2]
    compressed_blocks = [datum * [str(i)] for i, datum in enumerate(filesystem[::2])]
    compressed_individual_blocks = [int(digit) for number in compressed_blocks for digit in number]  # convert to single ints
    spaces = [digit for digit in filesystem[1::2]]

    compacted_filesystem = first_method(file_sizes[:], spaces[:], compressed_individual_blocks[:])
    print(f' The file checksum using the first method is {perform_checksome(compacted_filesystem)}')

    # need a different setup of data for the second method
    filesystem = []
    files = []  # going to be (index, length)
    spaces = []  # going to be (index, length)

    file_index = 0
    for i, block_len in enumerate(map(int, data.strip())):
        if i % 2 == 0:
            files.append((len(filesystem), block_len))
            filesystem += [file_index] * block_len
            file_index += 1
        else:
            spaces.append((len(filesystem), block_len))
            filesystem += ["."] * block_len

    compacted_filesystem = second_method(files, spaces, filesystem)
    print(f"The file checksum using the second method is : {perform_checksome(compacted_filesystem)}")


compact_disk(inputs.day_9_data)
