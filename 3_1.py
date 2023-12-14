def compress(data:bytes):
    result = bytearray()
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result += count.to_bytes(1)
            result.append(data[i - 1])
            count = 1
    
    result += count.to_bytes(1)
    result.append(data[-1])
    
    return result


with open("testc.ppm", "rb") as f:
    data = f.read()
    c = compress(data)
    print(len(data) / len(c))