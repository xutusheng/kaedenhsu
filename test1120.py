def transfer_text(origin_file, target_file):
    # 读取 origin_file.txt 所有行
    with open(origin_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 检查源文件是否有内容
    if lines:
        first_line = lines[0].strip()

        # 将第一行内容追加到 target_file.txt
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write(first_line + '\n')

        # 把剩下的内容写回 origin_file.txt
        with open(origin_file, 'w', encoding='utf-8') as f:
            f.writelines(lines[1:])

        return first_line
    else:
        print("⚠️ 源文件已空，无需操作！")
        return None
